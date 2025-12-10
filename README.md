Hangman Game – Project Documentation
CodeAlpha Python Programming Internship

Task 1 – Word Guessing Game

1. Introduction

This document explains the design, logic, and implementation of the Hangman Game, developed as part of the CodeAlpha Python Programming Internship (10 Dec 2025 – 10 Jan 2026).
The goal of the task is to build a simple, console-based word guessing game using only basic Python concepts.

2. Project Overview

Hangman is a classic guessing game where the player tries to identify a hidden word by guessing one letter at a time.
The player has six incorrect attempts before the game is over.

This project focuses on:

Logic building

User input handling

Loops and conditionals

Random module usage

3. Objectives

Select a random word from a list of predefined words

Display the word in masked format (_ _ _ _)

Allow user to guess one letter at a time

Track guessed letters

Limit wrong attempts to six

Detect win/loss conditions

Display appropriate messages

4. Technologies Used

Python 3

Built-in Python libraries:

random for word selection

Core Concepts:

Strings

Lists

Loops (while)

Conditional logic (if-else)

User input validation

5. Game Flow

Program starts and greets the user

A secret word is selected randomly

User sees blank placeholders (_ _ _)

User enters letter guesses

If the guess is correct → reveal letters

If incorrect → decrease attempts

Game ends when:

ALL letters are guessed → Win

Attempts reach zero → Lose

Secret word is revealed at the end

6. Features

Random word selection

Simple and clean console interaction

Input validation

Prevention of repeated guesses

Win/Loss detection

Easy-to-understand logic

7. How to Run
Step 1: Clone the repository
git clone https://github.com/vatsnandini5-cloud/CodeAlpha_HangmanGame

Step 2: Run the Python file
python hangman.py

8. Future Improvements

Add hint system

Support full word guessing

Add scoring system

Load words from external file

Create GUI (Tkinter / PyQt) version

9. Conclusion

This project successfully meets the requirements of Task 1 of the CodeAlpha internship. The Hangman Game demonstrates practical knowledge of Python fundamentals, input handling, and basic game logic.

This project helped strengthen:

Problem-solving skills

Logical thinking

Core Python understanding

10. Acknowledgment

This project was completed as part of the CodeAlpha Python Programming Internship.
Thanks to CodeAlpha for the opportunity to learn and build practical applications.
