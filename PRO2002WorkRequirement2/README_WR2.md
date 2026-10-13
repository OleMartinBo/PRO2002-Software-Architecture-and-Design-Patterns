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
Overall i found the process_order method and the tightly coupled Order class most challenging. For both of these challenges I often found myself going back to reading the OOP and SOLID principles. However, when I found an possible solution I always found myself struggling to communicate what i wanted to do. Further, I also was sometimes unsure if the proposed improvements was how I should confront the problems. I think for me, the reason i found these to most problematic is because I got to caught up trying to follow the principles too much. I should have rather focused more on systemically and incrementally fixing small but valuable code. 
In the end, the learning experience was very good on these two problems. I got to go back to the course material and apply the knowledge I got to the best of my ability. <br>


Below is information on each problem for WR2 --><br>

### 2.0 Converter.py problems and improvements
#### 2.1 Checking for problems
1. The class name `Converter` is generic, could benefit from a more descriptive class name.
2. The Method name is reasonable, but could benefit having a comment. 
3. The math formula to convert Fahrenheit to Celsius needs better comments and is difficult to understand.
4. The method and math formula to convert is correct, but could be simplified for better readability. <br>
E.g: "5/9" is twice as it calculates:<br>
212" X 5/9 = 117.78 <br>
-32 * 5/9 =- 17.78<br>
117.78 + (-17.78) = 100<br>

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
4. Simplify method and math formula to convert for better readability.

#### 2.3 The improvements i made and why
1. Added docstring to the module, class and method to describe their purpose.
2. Added comments to clarify what the double numbers are and why they are specific numbers. 
3. Changed the class name to FahrenheitConverter for better clarification on what the class are. 
4. Improved the formula for the Fahrenheit to Celsius for better readability and simplicity.

### 3.0 Order.py problems and improvements
#### 3.1 Checking for problems
1. The Single Responsibility: The `Order` class handle responsibilities for database persistence.The method of saving could be a area for separation of concerns rather than in the order class. 
2. Open/Closed Principle (OCP): The current state is hard to extend if the saving behavior needs to change. Adding e.g. subclasses of `save` could make it easier to extend without introducing new bugs. 
3. Dependency Inversion Principle: The `Order` class should not depend the current `save`, but rather depend on a abstract class for saving orders. 
4. Order_Id as "123" should not be hardcoded into the INSERT.
5. The order class is also dependent on the internal structure of User, meaning changes in User can affect the order class. 

**_Code metrics_**<br>
Cyclomatic complexity (CC):<br>
C 1:0 Order - A (3)<br>
M 13:4 Order.save - A (2)<br>
M 2:4 Order.__init__ - A (1)<br>
Average complexity: A (2.0)<br>

Maintainability index (MI):<br>
order.py - A (100.00)<br>

#### 3.2 The improvements i would make and why, step by step
1. I would move `save` to it own class that can handle storing of orders. This would follow the The Single Responsibility Principle, as the `Order` class no longer handles the SQL. 
2. I recommend to implement an abstract `orderRepository` class with a save() method, as seen in Module 1.5 in the course. This enables various saving methods to be implemented without modifying the `Order` class, which follows the Open/Closed Principle.
3. Next I would make `Order` depend on a shared abstraction rather than a concrete database implementation. This follows Dependency Inversion Principle, allowing it to be more loosely coupled and easier to maintain. 
4. I would also replace the hardcoded order id `123` with the `order_id`. This is because the order items should be connected to the correct order instead of reusing the same id.
   
### 4.0 discount.py problems and improvements
#### 4.1 Checking for problems
1. The main issues found in `discount.py` is that the the exact same discount logic exist in two places.
2. Changes has to be made both places, else system breaks and will cause inconsistencies. 
3. Docstring and new line also highlighted by Pylint.
4. Comment states that 10% is applied after 50 NOK, but value is set to 5000 in code. Possible mistake

**_Code metrics_**<br>
Cyclomatic complexity (CC):<br>
F 1:0 apply_discount_to_cart - A (3)<br>
F 13:0 generate_invoice - A (3)<br>

Maintainability index (MI):<br>
discount.py - A (91.41)<br>

Even thought the results is not to bad, these are not absolutes truths. <br>
However i found them useful to check before doing any work on the code.<br>

#### 4.2 The improvements i made and why
1. My first improvement is make a shared discount calculation.This ensures that the logic stays stable and easy to maintain 
2. I will keep `apply_discount_to_cart`, but return the new separate calculation function for cart. Thereby both the cart and order can use the same calculation from a shared function. 
3. Comment code and docstring where necessary. This has to be done when i refactor the code.  

### 5.0 process_order.py problems and improvements
#### 5.1 Checking for problems
1. The method have multiple concerns and the readability of the code is difficult.
2. The system can become unmanageable if more notifications and discounts is added. 
3. Testing can be difficult as it is one long method and takes the whole order process from start to finish.
4. Single Responsibility Principle is not followed. Database and notification could be separate concerns. 
5. Discount can also be many forms as of now, but not clearly explained in the code what the difference is.

**_Code metrics_**<br>
Cyclomatic complexity (CC):<br>
F 4:0 process_order - A (5)<br>
Average complexity: A (5.0)<br> 

Maintainability index (MI):<br>
process_order.py - A (86.55)<br>

#### 5.2 The improvements i would make and why, step by step
1. I would separate the logic for Calculate total and Apply discount into functions. This is a refactor approach called Extract Method and makes it more readable (refactoring.guru)
2. The magic numbers could be replaced with symbolic constant. This could be beneficial as the number get a documented meaning for the value in a human readable name (refactoring.guru). 
3. Next, handling the database and notification can be separated from the `process_order` in their own functions. This helps to make `process_order` easier to understand.  
4. Finally the `process_order` only passes the other functions instead of handle everything inside one function. This makes in easier to maintain, separate responsibility, and test. 
