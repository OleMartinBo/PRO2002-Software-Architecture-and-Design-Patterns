# Managing Technical Debt and Improving Legacy Code
In this work requirement, you will improve the examples of troublesome code from chapter 3.2 Common Challenges in Legacy Systems. You will study the provided snippets, explain why each example is problematic, and propose improvements that would make the code more maintainable, testable, and easier to understand.

## What to Do
Review the following examples from chapter 3.2 Common Challenges in Legacy Systems :

* the undocumented Converter
* the tightly coupled Order class
* the duplicated discount logic
* the process_order method

For each example, analyze what makes the code problematic and suggest concrete improvements. Refactor the code where appropriate and explain your refactoring choices. <br>

For the "tightly coupled Order class" and "the process_order method", use simple placeholders/stubs, or just describe with comments or in the README how the code could be improved

## 1.0 Overall Short reflection

### 2.0 Converter.py problems and improvements
#### 2.1 Checking for problems
1. The class name `Converter` is generic, could benefit from a more descriptive class name.
2. The Method name is reasonable, but could benefit having a comment. 
3. The math equation to convert Fahrenheit to Celsius needs better comments and is difficult to understand.

**_Code metrics_**<br>
Cyclomatic complexity (CC):<br>
C 3:0 Converter - A (2)<br>
M 5:4 Converter.__init__ - A (1)<br>
M 9:4 Converter.convert - A (1)<br>

Maintainability index (MI):<br>
converter.py - A (92.20) <br>

The relative indicators of Cyclomatic complexity and Maintainability index did not indicate any long term issues.

**_From Pylint:_**<br>
`C0114:missing-module-docstring`<br>
`C0115:missing-class-docstring`<br>
`C0116:missing-function-docstring`<br>
`C0304:missing-final-newline`<br>

#### 2.2 Suggestion to fix problems
1. Fix the Pylint warnings in the terminal by adding the docstring and final newline to the module.
2. Add short but descriptive comment where necessary to explain the code.
3. Possibly change class name to a more descriptive class name.

#### 2.3 The improvements i made and why
1. 

### 3.0 Order.py problems and improvements

### 4.0 discount.py problems and improvements

### 5.0 process_order.py problems and improvements


