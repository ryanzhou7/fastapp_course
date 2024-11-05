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

Let's go piece by piece to understand the`$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc` command

###### Question

What does the `>>` operator do in the command `$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc`?

- A: It overwrites the content of the file
- B: It appends the content to the file
- C: It creates a new file
- D: It deletes the file

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

The `>>` operator appends the content to the file, while `>` would overwrite the file.
</p>
</details>

---

###### Question

What does the `~` symbol represent in the command `$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc`?

- A: The root directory
- B: The current directory
- C: The home directory
- D: The previous directory

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

The `~` symbol represents the home directory of the current user.
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

The `.zshrc` file is a configuration file for the zsh shell, where you can set environment variables, aliases, and other settings.
</p>
</details>

---

###### Question

How do you add a command to the `.zshrc` file to see that it is run on every new terminal?

- A: `$ echo 'echo "hi"' >> ~/.zshrc`
- B: `$ echo 'echo "hi"' > ~/.zshrc`
- C: `$ echo 'echo "hi"' | ~/.zshrc`
- D: `$ echo 'echo "hi"' < ~/.zshrc`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

The `>>` operator appends the command `echo 'hi'` to the `.zshrc` file, so it will be executed every time a new terminal is opened.
</p>
</details>

---

