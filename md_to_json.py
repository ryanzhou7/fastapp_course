import json

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
            if question:
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
            choices.append(line[4:])
        elif line.startswith('- B:'):
            choices.append(line[4:])
        elif line.startswith('- C:'):
            choices.append(line[4:])
        elif line.startswith('- D:'):
            choices.append(line[4:])
        elif line.startswith('#### Answer:'):
            correct_choice = line.split(': ')[1]
            correct_choice_index = ord(correct_choice) - ord('A')
        elif line.startswith('<details><summary><b>Answer</b></summary>'):
            explanation = ""
        elif line.startswith('</p></details>'):
            explanation = explanation.strip()
        elif explanation is not None:
            explanation += line + "\n"
        elif not question:
            question = line

    if question:
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

# Example usage
convert_md_to_json('ch1_python.md')