import json
import os
import argparse
import tempfile

def write_newlines(md_file, n):
    for _ in range(n):
        md_file.write('\n')

def write_question_bookend(md_file):
    md_file.write('---\n\n')

def create_temp_file_without_newlines(md_filename):
    with open(md_filename, 'r') as md_file:
        content = md_file.read().replace('\n\n', '\n')

    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    temp_file.write(content)
    temp_file.close()
    return temp_file.name
  
def validate_and_convert_json_to_md(json_filename):
    # Load and validate JSON
    with open(json_filename, 'r') as file:
        data = json.load(file)
    
    if not isinstance(data, list):
        raise ValueError("JSON must contain an array at the root.")
    
    for item in data:
        if isinstance(item, dict):
            if 'question' not in item or 'answer' not in item:
                raise ValueError(f"{item} does not have 'question' and 'answer' attributes.")
            if 'choices' not in item['answer'] or 'correct_choice_index' not in item['answer']:
                raise ValueError(f"{item} must have 'choices' and 'correct_choice_index'.")
            if not isinstance(item['answer']['choices'], list) or len(item['answer']['choices']) != 4:
                raise ValueError(f"{item} 'choices' must be an array of 4 strings.")
        elif not isinstance(item, str):
            raise ValueError(f"{item} in the array must be either a string or a question object.")
    
    # Convert to Markdown
    md_filename = os.path.splitext(json_filename)[0] + '.md'
    with open(md_filename, 'w') as md_file:
        for item in data:
            if isinstance(item, str):
                md_file.write(item)
                write_newlines(md_file, 2)
            elif isinstance(item, dict):
                question = item['question']
                choices = item['answer']['choices']
                correct_index = item['answer']['correct_choice_index']
                explanation = item['answer'].get('explanation', '')
                md_file.write('###### Question')
                write_newlines(md_file, 2)
                replaced = question.replace("\\\\n", "\n")
                md_file.write(replaced)
                write_newlines(md_file, 2)
                for i, choice in enumerate(choices):
                    md_file.write(f'- {chr(65+i)}: {choice}')
                    write_newlines(md_file, 1)
                write_newlines(md_file, 1)
                md_file.write('<details><summary><b>Answer</b></summary>\n<p>')
                write_newlines(md_file, 2)
                md_file.write(f'#### Answer: {chr(65 + correct_index)}')
                write_newlines(md_file, 2)
                if explanation and explanation != "":
                    replace = explanation.replace("\\n", "\n")
                    md_file.write(replace)
                    write_newlines(md_file, 1)
                md_file.write('</p>\n</details>')
                write_newlines(md_file, 2)
                write_question_bookend(md_file)

def is_choice(line: str) -> bool:
    return line.startswith("- ")

def convert_md_to_json(md_filename):
  
  filename = create_temp_file_without_newlines(md_filename)
  with open(filename, 'r') as file:
    data = []
    line = file.readline()
    while line:
      if line.startswith('###### Question'):
        question_content = file.readline().strip()
        choices = []
        line = file.readline()
        while is_choice(line):
          choice = line.split(": ")[1].strip()
          choices.append(choice)
          line = file.readline()
        while not line.startswith("#### Answer:"):
          line = file.readline()
        letter_choice = line.split(": ")[1].strip()
        correct_index = ord(letter_choice) - ord('A')
        line = file.readline()
        answer = {
          "choices": choices,
          "correct_choice_index": correct_index
        }
        if not line.startswith("</p>"):
          answer["explanation"] = line.strip()
        data.append({
          "question": question_content,
          "answer": answer
        })
        while not line.startswith('---'):
          line = file.readline()
        line = file.readline()
      else:
        data.append(line.strip())
        line = file.readline()
  json_filename = md_filename.replace('.md', '.json')
  with open(json_filename, 'w') as json_file:
    json.dump(data, json_file, indent=2)

# Example usage
convert_md_to_json('ch1_python.md')
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert between JSON and Markdown.')
    parser.add_argument('filename', type=str, help='The file to convert.')
    args = parser.parse_args()
    
    if args.filename.endswith('.json'):
        validate_and_convert_json_to_md(args.filename)
    elif args.filename.endswith('.md'):
        convert_md_to_json(args.filename)
    else:
        raise ValueError("File must be either a .json or .md file.")