import json
import os

def write_newlines(md_file, n):
    for _ in range(n):
        md_file.write('\n')
  

def validate_and_convert_json_to_md(json_filename):
    # Load and validate JSON
    with open(json_filename, 'r') as file:
        data = json.load(file)
    
    if not isinstance(data, list):
        raise ValueError("JSON must contain an array at the root.")
    
    for item in data:
        if isinstance(item, dict):
            if 'question' not in item or 'answer' not in item:
                raise ValueError(f"Question {item} does not have 'question' and 'answer' attributes.")
            if 'choices' not in item['answer'] or 'correct_choice_index' not in item['answer']:
                raise ValueError("Each answer must have 'choices' and 'correct_choice_index'.")
            if not isinstance(item['answer']['choices'], list) or len(item['answer']['choices']) != 4:
                raise ValueError("Each 'choices' must be an array of 4 strings.")
        elif not isinstance(item, str):
            raise ValueError("Each item in the array must be either a string or a question object.")
    
    # Convert to Markdown
    md_filename = os.path.splitext(json_filename)[0] + '.md'
    with open(md_filename, 'w') as md_file:
        for item in data:
            if isinstance(item, str):
                md_file.write(item.replace('\\n', '\n') + '\n')
            elif isinstance(item, dict):
                question = item['question']
                choices = item['answer']['choices']
                correct_index = item['answer']['correct_choice_index']
                explanation = item['answer'].get('explanation', '')
                write_newlines(md_file, 2)
                md_file.write('###### Question\n\n')
                replaced = question.replace("\\\\n", "\n")
                md_file.write(replaced)
                write_newlines(md_file, 2)
                md_file.write(f'-   A: {choices[0]}')
                write_newlines(md_file, 1)
                md_file.write(f'-   B: {choices[1]}')
                write_newlines(md_file, 1)
                md_file.write(f'-   C: {choices[2]}')
                write_newlines(md_file, 1)
                md_file.write(f'-   D: {choices[3]}')
                write_newlines(md_file, 2)
                md_file.write('<details><summary><b>Answer</b></summary>\n<p>')
                write_newlines(md_file, 2)
                md_file.write(f'#### Answer: {chr(65 + correct_index)}')
                write_newlines(md_file, 2)
                if explanation:
                    replace = explanation.replace("\\\\n", "\n")
                    md_file.write(replace)
                    write_newlines(md_file, 1)
                md_file.write('</p>\n</details>\n\n---\n')


# Example usage
validate_and_convert_json_to_md('ch2_mise.json')