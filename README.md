Directory Tree Analyzer

A clean and modular Python tool to analyze directory structures.

Overview
This project is a Python-based directory tree analyzer designed to scan a folder and provide detailed insights including:
Total number of files
Total number of folders
Total size of files
File type distribution
Maximum folder depth

It is designed to be simple, readable, and robust, handling inaccessible files without crashing, and works safely on any user's Desktop or custom path.

Features:
Recursive folder traversal using os.walk
Modular functions for counting, sizing, and type analysis
Graceful handling of errors (inaccessible or missing files)
Fully testable and maintainable design
Cross-platform path handling with os.path

Usage;
Clone the repository:git clone https://github.com/jamesmbugua781/directory-tree-analyzer.git

Navigate to the project folder:
cd directory-tree-analyzer

Run the program:
python analyzer.py


By default, the program analyzes the Desktop folder of the current user. You can modify the get_target_path() function to analyze a different folder.

Future Improvements

Export results to JSON or CSV

Add a CLI argument parser to allow dynamic folder selection

Visual representation of the directory tree

Technologies

Python 3.11+

Standard library only (os module)

Why this project matters

This project demonstrates:

Clean modular design in Python

Proper separation of logic and output

Practical usage of os.walk and os.path

Basic system-level programming skills
