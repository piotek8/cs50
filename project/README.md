
# 🐍 Automated robot for sending CVs
#### Video Demo: https://clipchamp.com/watch/ASgLBjeZGLf
#### Description: I have created a project that automatically sends me a CV. This is a tool that helps me manage my professional resume. This tool is extremely useful, especially if you are looking for a job. Thanks to this, I can focus on other important tasks, while this program automatically sends me my candidature. This is just one of many ways you can use automation to streamline daily tasks. Thanks to this tool, I can save time that I would normally sending a CV. Instead, I can focus on developing my skills, learning new things, and undertaking other important tasks. Finally, this tool is proof of how powerful programming can be. Thanks to programming skills, I was able to create a tool that greatly facilitates the management of my professional resume. This is just one of many examples of how programming can be used to solve real problems.

## 👨‍💻 The project
A program that automatically logs into the portal once a day, completes the appropriate data and sends job applications.

## 🤔 How it works in practice?
#### Pracuj.pl


## 💬 Installation instruction
At the beginning, you must install the software that is mandatory to start the project, it is presented below.
 - [Python 3+ version](https://realpython.com/installing-python/#how-to-install-python-on-windows)
 - [Google Chrome](https://www.google.com/intl/pl_pl/chrome/)
 - [Chrome driver to Chrome](https://chromedriver.chromium.org/getting-started)
 - [Install Poetry](https://github.com/piotek8/Poetry-windows-instruction)

You need to install the necessary libraries in the terminal in your environment (pycharm is recommended by me):

```bash
  poetry install
```


## 📜 Selenium Python Bindings Documentation

Use this documentations for learning and finding solutions to problems.

- [Selenium with Python Documentation](https://selenium-python.readthedocs.io/)
- [Stack Overflow](https://stackoverflow.com/)



## 🔗 Run Locally

Clone the project

```
git clone git@github.com:piotek8/auto-sender.git
```
Go to the project directory

```
cd auto-sender
```
Install dependencies

```
poetry install
```
Start the app

```
You can use Shift+f10 in Pycharm or run with command in terminal like: python main.py
```


## 📁 How to entering data into the program

    Create an .env file in the main folder and enter the necessary data in the login and password (your data to log in to the Pracuj.pl portal)
    There is an example in the .env.example file
