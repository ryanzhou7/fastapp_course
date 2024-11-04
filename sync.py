import json
import os
import argparse

def write_newlines(md_file, n):
    for _ in range(n):
        md_file.write('\n')

def write_question_bookend(md_file):
    md_file.write('\n---\n\n')

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
                md_file.write(item.replace('\\n', '\n'))
                write_newlines(md_file, 1)
            elif isinstance(item, dict):
                question = item['question']
                choices = item['answer']['choices']
                correct_index = item['answer']['correct_choice_index']
                explanation = item['answer'].get('explanation', '')
                write_newlines(md_file, 1)
                md_file.write('###### Question\n\n')
                replaced = question.replace("\\\\n", "\n")
                md_file.write(replaced)
                write_newlines(md_file, 2)
                for i, choice in enumerate(choices):
                    md_file.write(f'- {chr(65+i)}: {choice}')
                    write_newlines(md_file, 1)
                write_newlines(md_file, 2)
                md_file.write('<details><summary><b>Answer</b></summary>\n<p>')
                write_newlines(md_file, 2)
                md_file.write(f'#### Answer: {chr(65 + correct_index)}')
                write_newlines(md_file, 2)
                if explanation:
                    replace = explanation.replace("\\n", "\n")
                    md_file.write(replace)
                    write_newlines(md_file, 1)
                md_file.write('</p>\n</details>\n')
                write_question_bookend(md_file)
'''
---

###### Question

{question_content}

- A: {Answer A}
- B: {Answer B}
- C: {Answer C}
- D: {Answer D}

<details><summary><b>Answer</b></summary>
<p>

#### Answer: {correct_letter_of_answer}

{optional_explanation_content}

</p>
</details>
---
'''
def convert_md_to_json(md_filename):
    with open(md_filename, 'r') as md_file:
        lines = md_file.readlines()
    
    data = []
    question = None
    choices = []
    correct_choice_index = None
    explanation = None

    for line in lines:
        line = line.strip()
        if line.startswith('###### Question'):
            if question and choices:
                data.append({
                    'question': question,
                    'answer': {
                        'choices': choices,
                        'correct_choice_index': correct_choice_index,
                        'explanation': explanation
                    }
                })
            question = None
            choices = []
            correct_choice_index = None
            explanation = None
        elif line.startswith('- A:'):
            choices.append(line[4:].strip())
        elif line.startswith('- B:'):
            choices.append(line[4:].strip())
        elif line.startswith('- C:'):
            choices.append(line[4:].strip())
        elif line.startswith('- D:'):
            choices.append(line[4:].strip())
        elif line.startswith('#### Answer:'):
            correct_choice = line.split(': ')[1].strip()
            correct_choice_index = ord(correct_choice) - ord('A')
        elif line.startswith('<details><summary><b>Answer</b></summary>'):
            explanation = ""
        elif line.startswith('</p></details>'):
            explanation = explanation.strip()
        elif explanation is not None:
            explanation += line + "\n"
        elif not question:
            question = line

    if question and choices:
        data.append({
            'question': question,
            'answer': {
                'choices': choices,
                'correct_choice_index': correct_choice_index,
                'explanation': explanation
            }
        })
    
    json_filename = md_filename.replace('.md', '.json')
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

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