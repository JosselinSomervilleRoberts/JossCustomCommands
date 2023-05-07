# Custom commands
This repository contains my personal commands.

# Installation
To install the commands, follow these steps:
1. Clone this repository: `git clone <URL>`
2. Add the following line to your `.profile`: `export PATH=$PATH":<PATH_TO_THIS_REPO>"`
3. Make sure that the commands are executable: `chmod +x <PATH_TO_THIS_REPO>/*`
4. Reload `.profile` with: `source ~/.profile`
5. Install the required python packages *(Python 3)*: `pip install -r requirements.txt`

## Current commands
Right now there are:
* `hello`: prints "Hello, World!" *(test command)*
* `aws-start <NAME>`: starts the AWS EC2 instance with the given name
* `aws-stop <NAME>`: stops the AWS EC2 instance with the given name

## Adding a new command
When you want to add a command `command`, follow these steps:
1. Create a new file `command` in this directory
2. Make it executable: `chmod +x command`
3. Reload `.profile` with: `source ~/.profile`