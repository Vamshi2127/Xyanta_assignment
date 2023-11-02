#question 1 
height = int(input())

for i in range(1,height+1):
    print("#"*i)


#alignment as parameter.

def print_pattern(height,alignment):
    if alignment == "Left":
        for i in range(1,height+1):
            print("#"*i)
    elif alignment == "Right":
        for i in range(1,height+1):
            spaces = " "*(height-i)
            print(spaces+("#"*i))
    else:
        print("Invalid alignment")


height = int(input())
alignment = input()

print_pattern(height,alignment)