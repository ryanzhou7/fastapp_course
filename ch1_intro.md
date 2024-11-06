# Chapter 1 The python interpreter

We learn by starting from scratch, as if you just received a new computer. The first thing to do is to install python. Luckily, it is most likely already installed on your computer.

###### Question

From the terminal how do you check if python is installed and it's version?

- A: `$ python -v`
- B: `$ python --version`
- C: `$ python -version`
- D: `$ python -V`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

If python was not installed, `$ python --version` would yield an error.
</p>
</details>

---

###### Question

You will often see `$ python` and `$ python3`, what is the difference?

- A: `$ python` refers to Python 3.x, `$ python3` refers to Python 2.x
- B: `$ python` and `$ python3` are aliases for the same version
- C: `$ python` refers to Python 2.x, `$ python3` refers to Python 3.x
- D: `$ python` is for Windows, `$ python3` is for Unix-based systems

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

For simplicity we will use `$ python` to refer to Python 3.x in this guide. Also, you can set it so both `$ python` and `$ python3` point to python3.
</p>
</details>

---

###### Question

How do you determine the location of where the currently active python in your terminal is installed?

- A: `$ which python`
- B: `$ where python`
- C: `$ locate python`
- D: `$ find python`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

This is a commonly used command. Even if `$ python --version` results in what you expected, the current python may not be where you expect it to be.
</p>
</details>

---

###### Question

What happens when you run `$ python` ?

- A: `$ python` compiles Python code
- B: `$ python` opens the Python documentation
- C: `$ python` starts the Python interpreter
- D: `$ python` installs Python packages

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

</p>
</details>

---

###### Question

What is an interpreter?

- A: A program that translates high-level code into machine code all at once
- B: A program that converts source code into bytecode
- C: A program that compiles code into an executable file
- D: A program that executes instructions written in a high-level programming language

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

An interpreter directly executes instructions written in a high-level programming language.
</p>
</details>

---

We can give interpreters instructions / code 1). one command at a time or 2). all at once as a script.

###### Question

Given the code `print('Hi')`, how do we give the python interpreter this code via one command at a time?

- A: `$ python print('Hi')`
- B: `$ python` then type `print('Hi')`
- C: `$ python -c "'print('Hi')'"`
- D: B and C

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

With `$ python`, you find yourself at a python REPL (Read-Eval-Print Loop) which is an interactive shell that allows you to execute Python commands one at a time and see the results immediately."
</p>
</details>

---

###### Question

Given the code `print('Hi')`, how do we give the python interpreter this code via all at once as a script.?

- A: You need to first setup a virtual environment
- B: `$ python` then type `print('Hi')`
- C: Create a file called `file.py` with the code and run `$ python file.py`
- D: All of the above

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

Although setting up a virtual environment is best practice, this doesn't need to be done. There is nothign special the filename `file.py` by the way.
</p>
</details>

---

###### Question

Suppose python wasn't installed on your computer, how do we install it?

- A: Download from the official Python website
- B: Use a package manager like `$ apt` or `$ brew`
- C: Install from a third-party website
- D: All of the above

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

All of these methods are valid depending on your OS. However, none of these methods of installation allow us to switch between python versions easily.
</p>
</details>

---

###### Question

Why might we need to switch between python versions?

- A: Different projects may require different versions
- B: To test compatibility with different versions
- C: To use features available only in specific versions
- D: All of the above

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

</p>
</details>

---

If you search for the tool to solve this problem you will most likely find [pyenv](https://github.com/pyenv/pyenv) which is very popular and well regarded. But [mise](https://github.com/jdx/mise?tab=readme-ov-file#what-is-it) is a better choice as it is a lightning fast, more general tool that can manage multiple languages and tools, which we'll see next.

