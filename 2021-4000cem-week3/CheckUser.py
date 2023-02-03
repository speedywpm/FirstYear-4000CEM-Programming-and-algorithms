# We see if the user can follow instructions
# 
A_str = input("Please enter a positive number less than 100: ")
A_float = float(A_str)
answer = A_float > 0 and A_float < 100
print("Followed the instructions: " + str(answer))