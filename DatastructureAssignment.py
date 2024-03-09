# Q1
#  a deque is faster pop & append from both the sides we can add new things at left side and at same time we aslo pop the things.

from collections import deque
fruits = deque(["apple" ,"banana", "orange"])

fruits.appendleft("Mango")
fruits.pop()
print(fruits)

#  Q2
# real world examples :- Browsing History & Open any folder and their is multiple folder inside it so at last you open a folder which is pop first

History=[]
History.append("Pwskills")
History.append("data_analyst_course")
History.append("python")
History.append("excel")
print(History)
print(History.pop())
print(History)

# Q3
# it will give you a unique value so, there is no Duplication of any value & we can compare to data Sheet either it is matching or not
a={1,2,3,1,2,3,4,6,7}
print(a)

#4
# in array we can store only single or same type of data type like int, string it is faster than list and there is no limit to storing the data
# we need to import module from python liberary
import array

student_roll_no=array.array('i',[1,2,3,4,5,6,7])
for a in student_roll_no:
    print(a)

# in list we can add different type of data type
b=[1,2.3,"vikrant"]
print(b)

# Q5
# in list we take the element by the help of index value but in dictonry we take the element by the help of key
# list is in sequence but dictonary is random
list=[1,3.4,"vikrant"]
c=list[2]       # we are using index value
print(c)

dic={1:"vikrant",2:"rai"}
print(dic[1])    # we are using key for getting the value

# another example (List)

temp=[53,65,73.6,83,24,52.6,98]

days=input("enter your day 'sun' , 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', to get temp")

if days=="sun":
    print(f'the temp on {days} is' , temp[0])

elif days=="mon":
    print(f'the temp on {days} is' , temp[1])

elif days=="tue":
    print(f'the temp on {days} is' , temp[2])

elif days=="wed":
    print(f'the temp on {days} is' , temp[3])

elif days=="thu":
    print(f'the temp on {days} is' , temp[4])

elif days=="fri":
    print(f'the temp on {days} is' , temp[5])

elif days=="sat":
    print(f'the temp on {days} is' , temp[6])

else:
    print("invalid day")
    
# Dict example

dict1={'sun':34.2 , 'mon': 55.2 ,'tue': 65.2 ,'wed': 76.2}
days=input("enter your day 'sun' , 'mon', 'tue', 'wed', to get temp")
print(f'the temp on {days} is' ,dict1[days])
print(dict1[days])