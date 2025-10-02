COMP 163 - Assignment 5: Loop Mastery

Challenge 1: Collatz Sequence
I used a while loop because the number of iterations is not known in advance. The Collatz sequence can vary greatly depending on the starting number, so a loop that continues until a stopping condition (`n == 1`) is the right choice.
How it works:
Read a positive integer.
While it is not 1, print it and update it using the rules (even → divide by 2, odd → 3n + 1).
Count the steps until the number reaches 1.
Print the full sequence and the step count.

Challenge 2: Prime Checker
I used a for loop. The loop has a known number of iterations, which makes `for` the correct structure.
How it works:
Read a positive integer greater than 1.
Print which divisors are being tested.
Use a for loop to check each divisor. If one divides evenly, print that the number is not prime and stop.
If no divisor is found, print that the number is prime.

Challenge 3: Multiplication Table
I used nested loops because the table has two rows and columns. The outer loop controls the row, and the inner loop controls the column.
How it works:
Print the header row (1–10).
Use the outer loop to print row numbers (1–10).
Inside it, use the inner loop to calculate and print each product with proper formatting.

AI Assistance
I used ChatGPT for help with:
Breaking down the rubric into clear requirements.
Explaining why each loop type was appropriate.

This assistance helped me structure my work and understand the reasoning behind loop choices.

Git Workflow
Commit 1: Challenge 1: Collatz sequence - while loop for unknown iterations
Commit 2: Challenge 2: Prime checker - for loop for known range
Commit 3: Challenge 3: Multiplication grid - nested loops
Commit 4: Add loop design documentation



