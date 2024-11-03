Per the [mise quickstart](https://github.com/jdx/mise?tab=readme-ov-file#quickstart) the first command to install mise is `$ curl https://mise.run | sh`.

###### Question. What do you see when you visit [https://mise.run](https://mise.run) ?

###### Question. What does the `$ curl https://mise.run` do?

Now let's look at the second command, `sh`.

Create this file

```sh
# hello.sh
echo 'hello'
```

###### Question. What happens when you `$ sh hello.sh` ?

We understand both the `$ curl` and the `$ sh` but to understand what `|` does, it is better to see a different example.

Let's set up the example. We want to create 3 files with different file names.
The easiest way to do this is `$ touch file1`, which creates file with name `file1`. You can also pass it multiple arguments at once, i.e. `$ touch file2 file3 smallfile3`. Do this now.

###### Question. What does `$ ls` do when you run it?

###### Question. What does `$ ls` do, generally?

###### Question. What does `$ grep file` do?

We need pass or pipe `$ grep` something, that's what `|` does.

###### Question. What does `$ ls | grep file` do?

###### Question. What does `$ curl https://mise.run | sh` do then?

###### Question. Speaking of `sh` what is that?

###### Question. How is `sh` different from `bash` ?

###### Question. What is apple's default shell for macOS?

###### Question. How is `bash`, `sh`, `zsh` different?

But sometimes `bash`, `sh`, `zsh` are the same...

###### Question. What is the command to create a file called `hello.sh` ?

```bash
# hello.sh
echo 'hello'
```

###### Question. What are the commands to run `hello.sh` with `bash`, `sh`, `zsh` ? (Then run them)

Okay, getting back to the mise installation...
Step 1 was `$ curl https://mise.run | sh`
Step 2 says

> Hook mise into your shell (pick the right one for your shell):

```bash
echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc
echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc
echo '~/.local/bin/mise activate fish | source' >> ~/.config/fish/config.fish
```

###### Question. What's the right command to execute?

Let's understand this command `$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc`

###### Question. What happens when you run `$ echo 'hey' >> result`

###### Question. What happens when you run `$ cat result`

###### Question. What happens when you run it again?

###### Question. What happens when you run `$ echo 'hey' > result`

###### Question. What happens when you run `$ echo 'hey' > result` again?

Now you've seen your 2nd operator, 1st being `|` and 2nd being `>>`.

We can skip the in depth understanding of `'eval "$(~/.local/bin/mise activate zsh)"` because we know what `echo` expects, what is that?

So `$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc` is taking some string and appending to the `~/.zshrc` file.

###### Question. What is location is `$ ~` by the way? What's the command to change directory to that location and show the files there?

###### Question. What's the command to show the files there without changing directory?

Open the `~/.zshrc` file in Vscode.

Add `echo "hello"` to the bottom of the file, save it, and open another terminal
You might see some warning text, but you do see the output message. Delete the echo and save the file. You should not see the output message now.

For this text command, DO NOT test it. Check your answer first.

###### Question. How do you add the `echo "hello"` to the bottom of file `~/.zshrc` in one command?

We did not want to test this command because `>` replaces the entire file, but `>>` appends to it.

###### Question. What if we wanted to for the `~/.zshrc` code to be executed in the current terminal we're on and we don't want to open another one? We can use, `$ source ~/.zshrc`. How would you test this out?

We're ready to execute Step 2 of the mise installation.

See how the contents of `~/.zshrc` changes after you run `$ echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc`

What `eval "$(/Users/ryanzhouOld/.local/bin/mise activate zsh)"` does is just makes sure mise is activate and available for use in every new zsh terminal.

What is the mise command to install a version of python?

Run

```python
# main.py
print('Hello World')
```

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

{optional_explanation}

</p>
</details>

---
