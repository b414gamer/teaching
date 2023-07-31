#Loop For
#range(3) is the same as [0, 1, 2]

#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  #output: apple, banana, cherry


#info = ['ชื่อ', 'นามสกุล', 'อายุ', 'เพศ']
#data = ['สมชาย', 'ใจดี', '25', 'ชาย']

#make loop that display 1-10

#ex2
#example for loop with continue
for x in range(10):
    if x == 5:
        continue
    print(x)
    #output: 0, 1, 2, 3, 4, 6, 7, 8, 9

#ex3
#example for loop with break
for x in range(10):
    if x == 5:
        break
    print(x)
    #output: 0, 1, 2, 3, 4

#ex4
#example for loop with else
for x in range(10):
    print(x)
else:
    print("Finally finished!")
    #output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, Finally finished!

