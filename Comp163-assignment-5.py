# COMP 163 Assignment 5 - Loop Mastery (Example)
# By: Clayan Ariaga


# Challenge 1: Collatz Sequence
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")
if current_number == 1:
    print(current_number, end=" ")
else:
    while current_number != 1:
        print(current_number, end=" ")
        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            current_number = 3 * current_number + 1
        step_count += 1
    print(current_number, end=" ")

print()
print("Steps:", step_count)
print()  # blank line for spacing


