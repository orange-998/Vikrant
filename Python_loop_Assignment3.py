# Q1 Print no from 1 to 5 ing a while loop.

i=0
while i<5:
    i=i+1
    print(i)

# Q2 Sum of first 10 no using while no

sum, i= 0,0
while i<10:
    i=i+1
    sum=sum+i
print(sum)

# by using for loop to verify answer

sum=0
for i in range(1,11):
    sum=i+sum

print(sum)

#Q3 Factioral by using for loop

original= range(1 ,6)
reserved=list(original[::-1])
rev=1
for i in reserved:
    rev=rev*i

print(rev)

#Q4 count vowel in a string using a for loop

name = "vikrant"
vowels = "aeiouAEIOU"
count=0
print(len(name))
print(len(vowels))
for i in range(0,7):
    for j in range(0,10):
       if name[i]== vowels[j]:
           count=count+len(name[i])
print(count)

#Q5 Print a pattern using nested loop.

for i in range(0 ,3):
    print("*" ' ' * 3)
# right angle triangle
for i in range(0 ,5):
    for j in range(0 , 5):
        if i>=j:
            print("*", end=" ")
    print()

# reverse right angle triangle
for i in range(0 ,5):
    for j in range(0 , 5):
        if j>=i:
            print("*", end=" ")
    print()

# Right side right angle triangle

n= int(input("enter a no"))
for i in range(0 ,n):

    for j in range(0, n):
        if j <= n - i - 1:
             print(" ", end=" ")
    for j in range(0, n):
        if j >= n - i - 1:

             print(("*"), end=" ")

    print()

# Q6 Generate a multiplication table using nested loop.

for i in range(2,11):
    for j in range(1,11):
        print(i * j, end="\t")

    print()



