###### Question

How much faster do you think mise is at install a version of python compared to pyenv?

- A: Up to 10 times faster
- B: Up to 5 times faster
- C: Up to 3 times faster
- D: Up to 2 times faster

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

According to the `mise` GitHub repository, it can be up to 10 times faster than `pyenv` for installing Python versions.
</p>
</details>

---

###### Question

What is the first step to install mise per it's [GitHub repository quick-start](https://github.com/jdx/mise?tab=readme-ov-file#quickstart) guide?

- A: Clone the repository
- B: `$ curl https://mise.run | sh`
- C: `$ mise init`
- D: `$ mise install`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

</p>
</details>

---

Now, the following might feel a bit like a tangent, but it is important because learning these commonly used unix commands is very helpful for backend server management / deployment scripts / day to day use cases.

###### Question

What does the `$ curl https://mise.run` do?

- A: It downloads the content of the URL and saves it to a file, then executes it
- B: It downloads the content of the URL and executes it
- C: It downloads the content of the URL and saves it to a file
- D: It downloads the content of the URL and prints it to the terminal

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

</p>
</details>

---

Now let's look at the second command, `sh`. Run `$ sh` at the terminal, what does it do?

###### Question

What does the `$ sh` command do?

- A: It opens a new shell interpreter
- B: It executes the content of the file
- C: It prints the content of the file
- D: It saves the content of the file

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

</p>
</details>

---

Let's try to pass code to the `$ sh` interpreter in the same two ways like we did with the python command. Create a file with `$ touch hi.sh` and add `echo 'Hi'` to it.

###### Question

How do we give the `$ sh` interpreter the code `echo 'Hi'` via all at once as a script?

- A: You need to first setup a virtual environment
- B: `$ sh` then type `echo 'Hi'`
- C: `$ sh hi.sh`
- D: A and C

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

</p>
</details>

---

###### Question

How do we give the `$ sh` interpreter the code `echo 'Hi'` via one command at a time?

- A: `$ sh` then type `echo 'Hi'`
- B: `$ sh -c "'echo 'Hi'"`
- C: `$ echo 'echo "hi"' | sh`
- D: All of the above

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

Though all of these work we want understand the `$ echo 'echo "hi"' | sh` the most. This is because it is a common pattern to pipe the output of one command to another command as `$ curl https://mise.run` | sh does. Why doesn't `$ echo 'hi' | sh` not work? The error you get is `sh: 1: hi: not found`. This is because echo outputs 'hi', which is not a valid command. Hence, we need to double echo
</p>
</details>

---

Now that we know `$ curl https://mise.run` downloads the content of the URL and outputs it, `|` passes the output to `$ sh`, which runs the commands. We see how `mise` is installed. Some code is given to the `sh` interpreter to run.

###### Question

The next step to install mise per it's [GitHub repository quick-start](https://github.com/jdx/mise?tab=readme-ov-file#quickstart) guide? is: Hook mise into your shell (pick the right one for your shell): ... which is the right choice?

- A: `$ echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc`
- B: `$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc`
- C: `$ echo ''~/.local/bin/mise activate fish | source'' >> ~/.config/fish/config.fish`
- D: None of the above

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

If you are on a macOS, `$ zsh` is set as your default shell.
</p>
</details>

---

Let's go piece by piece to understand the`$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc` command. Starting with `$ eval`, an built-in shell command that takes a string as an argument and evaluates it as if it were a command

###### Question

Which is the simplest, correct usage of the `eval` command?

- A: `$ eval $(echo echo 'hi')`
- B: `$ eval 'hi'`
- C: `$ eval $(echo 'hi')`
- D: `$ eval echo 'hi'`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

Even though `$ eval $(echo echo 'hi')` also works, it is not the simplest usage of the `eval` command.
</p>
</details>

---

For `$(...)`: This is command substitution. It runs the command inside the parentheses and replaces the $(...) with the output of that command

###### Question

What is the simplest correct usage of the `$(...)` syntax?

- A: `$ $(ls)`
- B: `$ $(pwd)`
- C: `$ echo $(echo 'hi')`
- D: `$ echo $(cd)`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

Though some of these may not give you errors, `$ echo $(echo 'hi')` as we know the evaluation of echo 'hi' is 'hi', so then we have `$ echo 'hi', which prints 'hi'.
</p>
</details>

---

We will not cover `$(~/.local/bin/mise activate zsh)` but know that it will output some valid command to be evaluated. That evaluate is a string as that is what echo expects. Now, we had simplify it to `$ echo 'some string...' >> ~/.zshrc`?. Let's test what the `>>` operator does.

###### Question

What does `$ echo 'test1' >> test.txt` do?

- A: It overwrites the content of the file
- B: It appends the content to the file
- C: It creates a new file and writes 'test1' to it
- D: It deletes the file

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

The `>>` operator appends the content to the file. If the file does not exist, it creates a new file and writes 'test1' to it.
</p>
</details>

---

###### Question

What is the ultimate result of running `$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc`?

- A: It overwrites the `.zshrc` file with the `mise` activation command
- B: It appends the `mise` activation command to the `.zshrc` file
- C: It creates a new `.zshrc` file with the `mise` activation command
- D: It deletes the `.zshrc` file

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

The `>>` operator appends the `mise` activation command to the `.zshrc` file. This ensures that the `mise` environment is activated every time a new terminal session is started.
</p>
</details>

---

###### Question

What is the purpose of the `.zshrc` file?

- A: It is a configuration file for the bash shell
- B: It is a configuration file for the zsh shell
- C: It is a configuration file for the fish shell
- D: It is a configuration file for the sh shell

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

The `.zshrc` file is a configuration file for the zsh shell, where you can set environment variables, aliases, and other settings. Basically, it is a script that runs every time a new terminal session is started.
</p>
</details>

---

###### Question

DO NOT TEST OUT ALL OF THESE COMMANDS AS some may delete your configuration file. How do you ensure 'hi' prints every time a new terminal is opened?

- A: `$ echo 'echo "hi"' > ~/.zshrc`
- B: `$ echo 'echo "hi"' | ~/.zshrc`
- C: `$ echo 'echo "hi"' < ~/.zshrc`
- D: `$ echo 'echo "hi"' >> ~/.zshrc`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

The `>>` operator appends the command `echo 'hi'` to the `.zshrc` file, so it will be executed every time a new terminal is opened. The dangerous command is >, which overwrites the file. You can test this out with a simple command like `$ echo 'echo "hi"' > test.txt` then `$ cat test.txt` to see the contents, then `$ echo 'echo "bye"' > test.txt`
</p>
</details>

---

Finish your mise installation, in the next chapter we will begin using it

