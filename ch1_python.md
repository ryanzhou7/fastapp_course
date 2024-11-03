We start from scratch to learn python/fastapi, etc... as if you just received a new computer. The first thing to do is to install python. Luckily, it is most likely already installed on your computer.


###### Question

From the terminal how do you check if python is installed and it's version?

-   A:  `$ python -v`
-   B:  `$ python --version`
-   C:  `$ python -version`
-   D:  `$ python -V`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

<p>


</p>
</details>

---


</p>
</details>

---


###### Question

You will often see `$ python` and `$ python3`, whats the difference?

-   A: `$ python` refers to Python 3.x, `$ python3` refers to Python 2.x
-   B: `$ python` and `$ python3` are aliases for the same version
-   C: `$ python` refers to Python 2.x, `$ python3` refers to Python 3.x
-   D: `$ python` is for Windows, `$ python3` is for Unix-based systems

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

<p>


</p>
</details>

---

For simplicity we will use `$ python` to refer to Python 3.x in this guide.


</p>
</details>

---


###### Question

How do you determine the location of where the currently active python in your terminal is installed?

-   A: `$ which python`
-   B: `$ where python`
-   C: `$ locate python`
-   D: `$ find python`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

<p>


</p>
</details>

---


</p>
</details>

---


###### Question

What happens when you run `$ python` ?

-   A: `$ python` compiles Python code
-   B: `$ python` opens the Python documentation
-   C: `$ python` starts the Python interpreter
-   D: `$ python` installs Python packages

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

</p>
</details>

---


###### Question

What is an interpreter?

-   A: A program that translates high-level code into machine code all at once
-   B: A program that converts source code into bytecode
-   C: A program that compiles code into an executable file
-   D: A program that executes instructions written in a high-level programming language

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

An interpreter directly executes instructions written in a high-level programming language, without requiring them to be compiled into machine code.
</p>
</details>

---
We'll see another interpreter in the next chapter (sh).


###### Question

Suppose python wasn't installed on your computer, how do we install it?

-   A:  Download from the official Python website
-   B:  Use a package manager like `$ apt` or `$ brew`
-   C:  Install from a third-party website
-   D:  All of the above

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

<p>


All of these methods are valid depending on your OS.

</p>
</details>

---

However, none of these methods of installation allow us to switch between python versions easily.


</p>
</details>

---


###### Question

Why might we need to switch between python versions?

-   A:  Different projects may require different versions
-   B:  To test compatibility with different versions
-   C:  To use features available only in specific versions
-   D:  All of the above

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

<p>


</p>
</details>

---

If you search for the tool to solve this problem you will most likely find [pyenv](https://github.com/pyenv/pyenv) which is very popular and well regarded. But [mise](https://github.com/jdx/mise?tab=readme-ov-file#what-is-it) is a better choice as it is a lightning fast, more general tool that can manage multiple languages and tools, which we'll see next.

</p>
</details>

---
