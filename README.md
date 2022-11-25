# Tugas Pemrograman TBFO - Javascript Parser

Javascript Parser is a parsing program that checks javascript languange with some limitations. This parser utilizes Context Free Grammar and Finite Automata theory. For validation, CYK algorithm is used by changing the CFG into its Chomsky Normal Form.

## Table of Contents

-   [General Info](#general-information)
-   [Team Members](#team-members)
-   [How to Run](#how-to-run)
-   [Program Structure](#program-structure)

## General Information

Within javascript parser you can add javascript file into test folder and check its syntax. If the syntax is correct, the program will print out "Accepted". Meanwhile, when there is a syntax error, the program will print out "Syntax Error". When you have any illegal character in the javascript file, the program will tell there is an illegal character in certain line

## Team Members

| **NIM**  |       **Nama**        |
| :------: | :-------------------: |
| 13521052 |  Melvin Kent Jonathan |
| 13521194 | Angela Livia Arumsari |
| 13521100 |    Alexander Jason    |

## How to Run

1. Clone this repository by running this command in your computer
```
$ git clone https://github.com/melvinkj/Tugas-Besar-TBFO.git
```

2. Put javascript file you want to validate to `test` folder

```
$ pip install -r requirements.txt
```

3. Run main.py with the argument below by changing <filename.js> into your file name

```
$ python main.py test/<filename.js>
```

## Program Structure

```
.
│   .gitignore
│   main.py
│   README.md
|
└───src
    ├───lib
    │   └───CFG.txt
    |       CFGtoCNF.py
    |       CYKparser.py
    |       fa.py
    |       tokenizer.py
    └───test
        test01.js
        test02.js
        test03.js
        test04.js
        test05.js
        test06.js
        test07.js
        test08.js
```