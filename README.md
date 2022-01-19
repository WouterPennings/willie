# Willie

Wilie is a discord bit written in [Python](https://python.org). He is made for the [Loop Discord Server](https://discord.gg/T3tqQBTyJA) so people can play around with Loop without needing the compiler. Willie needs to be **very** simple, basicly only one command: _!Run_

## What is Loop
Loop is a programming language that is implemented in Rust. It is trying to tackle the problems of needing C to develop fast programs in Python. The goal is to make [Loop](https://looplang.org) blazing fast **and** easy, so a secondary language is unnecessary. 

Where to find Loop:
- [Website](https://looplang.org)
- [GitHub](https://github.com/looplanguage)

## How to run

It has three commands for you to run:
 - ``!Run <LOOP CODE>`` Runs your program and send results back
 - ``!Source`` Send the link to GitHub repository
 - ``!Help`` Sends all the commands that the bot can do

## How to run Willie

### Installed

You need to have installed these things:

- Python 3.x
- Pip

### Steps

1. Run: `git clone https://github.com/WouterPennings/willie.git`, in your terminal
2. Navigate to the folder: `cd willie`
3. Create you own Discord bot in the [developer-portal](https://discord.com/developers/)
4. Create a `.env`, and paste it this: `TOKEN="<YOUR BOT TOKEN>"`
5. Run: `pip install -r requirements.txt`, in your terminal
6. Run: `python3 willie.py`, in the terminal 

These are all the steps to run your own Willie!

## Folder Structure

 - ``willie.py`` Is the entrypoint of the bot, there are all the requests it can handle
 - ``commands/`` All the commands that Willie executes will be in there
 - ``logic/`` Some extra functions that are needed

## Contribute

All contributions are welcome and appreciated. Create an issue if you have a bug, question, enhancement, etc. If you have an addition, create a pull-request.
