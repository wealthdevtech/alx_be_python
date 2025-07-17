#1 Get input from the user for the size of the pattern
user_input = int(input("Enter the size of the pattern: "))

#2 Create i to control row iterations in the while loop
i = 0
while i < user_input:
    #3 Create j in for loop to control asterick iterations
    for j in range(user_input):
        #4 Print an asterick for j
        print("*", end="")
    #5 Print a newline at the end of each row iteration and add 1 to i
    print()
    i += 1