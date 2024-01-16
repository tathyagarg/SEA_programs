# Prigram to find the sum of the first 10 odd numbers
ODD_COUNT = 10  # Constant
total = 0

for i in range(1, ODD_COUNT*2, 2):  
    """ 
    Start: We use 1 as starting point since we need odd numbers. Keeping start as 0 would give even numbers. 
    Stop: Stop is set to ODD_COUNT*2 since we need to iterate over '2n' numbers to get first 'n' odd numbers. 
    Step: Step is used as 2 in order to skip over even numbers 
    """
    total += i
print(f"Total is: {total}")
