# Python 2025

- [ ] Basics
  - [x] Installing Python in system
  - [x] "Hello, World" program
  - [x] Python's inner working
    - [x] Source code -> Byte code -> Runs on Python Virtual Machine
    - [x] Byte Code
      - Byte code is not machine code
      - Generally byte codes are hidden
      - Byte codes are also called frozen binaries
      - byte codes or .pyc files are only generated for files that are importing some modules not for top level files
      - Names of byte codes are in this format [name].[python implimentaion].[version].pyc
      - Standard implementation of python is cpython
      - Other implementaion of python are jython, iron python, pypy, stackless etc.
    - [x] Python Virtual Machine (PVM)
      - Code loop that executes byte code or direct python code from top to bottom
      - Also called run time engine for python
      - Also called python interpreter
