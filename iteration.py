#Write a program which repeatedly reads integers until the user enters “done”. 
#Once “done” is entered, print out the total, count, and average of the integers. 
#If the user enters anything other than a integers,
#detect their mistake using try and except and print an error message and skip to the next integers.
totalValue = 0
count = 0

print("Enter an integer (or 'done' to finish):")

while True:
    try:
        value = input()
        if value == 'done':
            break
        value = int(value)  # Convert input to an integer
        totalValue += value
        count += 1
    except ValueError:
        print('Enter only integer values. Skipping this input.')

if count > 0:
    average = totalValue / count
    print(f'Total sum: {totalValue}')
    print(f'Count of integers entered: {count}')
    print(f'Average: {average:.2f}')
else:
    print('No valid integers entered.')
