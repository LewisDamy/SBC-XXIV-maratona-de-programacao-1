# Python Do-While loop to catch upper and lower boundaries levels
while True:
    N = int(input("Type the number of competitors: "))
    if 2 <= N <= 10000:
        break

# create an list
lst = []

# append the values into the list by iterating with the range of the numbers of competitors
for i in range(N):
    numbers = int(input())
    lst.append(numbers)
    # catch upperbound limit values
    if sum(lst) >= 100000:
        break

num = max(lst) # def num as the biggest number in the list

# def a function that check if all the values are the same
def all_same(items):
    return len(set(items)) < 2
    # use the set function and the length to see if there are equal values

for i in range(N):
    # check if the biggest number in the list is the first one
    if num == lst[0]:
        print("S")
        break
    # call the all_same function and check if there are an equal
    elif all_same(lst) == True:
        print("S")
        break
    else:
        print("N")
        break

