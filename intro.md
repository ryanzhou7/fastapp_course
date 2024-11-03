# Introduction

## Conventions

- If there is a `$` then it means it is meant to be typed at the command line, for example `$ python --help`

```python
# src/__init__.py
# ^means that the code contents below are from the __init__.py file in the src folder
print('Hello World')
```

```python
# src/__init__.py
print('Hello World')
# ... <- means that extra lines may occur between these 2 print statements but
# we omit them for brevity / they are not the focus
print('Hello World again!')
```

For all questions whose details are not fill out, give me 4 multiple choice answers that are difficult to discern from the correct answer. You may include, all of these, A and B, none of those, and the like choices. Also fill in the correct_choice_index and add explanation if needed. If something is meant to typed at the command line make such it is enclosed in a back tik and a $ proceeds the command. For example `$ which python`

In python write me a function that takes as input the name of the .json file like ch1_python.json. First it validates that the .json has the correct attributes, which are. There is one array object. The elements are either string or question objects. The question objects must have question, and answer. The answers must have choices, which is an array of 4 strings, and correct_choice_index. Explanation is optional. If the input is valid, then it will output a file of the same input name but with extension .md
For all strings, replace \n with an actual new line.
For string attributes at the root, simplify output the string verbatum then a new line. For question json, it should be in the form of (where {} designates replacements are needed).

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
