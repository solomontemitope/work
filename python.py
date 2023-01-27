#num = int(input("enter num:"))
#for i in range (1, num + 1):
 #   print(i)

#num = int (input("enter num: "))
#for i in range (1, num + 1):
 #   count = num
  #  count -= i
   # print(count) 


#name = "pynative"
#num_name = len(name)
#for i in range (0, num_name, 2):
   # print(name[i])

#name = "pynative"[::-1]
#num_name = len(name)
#for i in range (1, num_name, 2):
 #   print(name[i])

# enter number 
#number = int(input("enter num: "))
#iterate over number
#for i in range (1, number + 1):
#iterate over i using nested loop 
    #for j in range (i):
     #   print(i, end = " ")
    #print(" ")

#name = "solomonpopoola"
#number_name = len(name)
#for i in range (1, number_name + 1):
 #   count = number_name
  #  count -= i
   # print(name[count], end = "")

#sentence = "Mosh is a programmer. Mosh is writing a program"
#num_name = sentence.count("Mosh")
#print(num_name)
#numbers = [2,3,2,5,3,6,2,8,4,2]
#m = numbers.count(2)
#print(m)

#number = int(input("enter number: "))
#for i in range (number, 0, -1 ):
   # for j in range (0, i):
  #      print(i, end= " ")
 #   print (" ")

#number_row = 5
#iterate over number_row
#for i in range (1, number_row + 1):
    #count = i
    #count *= "*"
    #print (count)

#number_row = 5
#iterate over number_row
#for i in range (number_row, 0, -1):
    #count = i
    #count *= "*"
    #print (count)


#def numbers(num):
  #  count = i
 #   count *= "X"
   # return count 


#num = [5,2,2,5,2,2]
#for i in num:
 #   print(numbers(num))


#def numbers_coverter(numbers):
  #  numbers_words = {
 #       "1": "one",
   #     "2": "two",
     #   "3": "three",
    #    "4": "four",
      #  "5": "five"
    #}
    #output = ""
    #for i in numbers:
     #   output += numbers_words.get(i, "!") + " "
    #return output


#numbers = input("numbers: ")
#print(numbers_coverter(numbers))


#def numbers(num):
 #   count = ""
  #  count += "X"
   # return count 


#num = [5,2,2,5,2,2,5]
#for i in num:
 #   for j in range (i):
 #       print(numbers(num), end = "")
  #  print("")

#def numbers(num):
 #   count = i
  #  count *= "X"
    #return count


#num = 5
#for i in range (1, num + 1):
 #   print(numbers(num))


#def numbers(num):
 #   count = i
  #  count *= "X"
   # return count


#num = 5
#for i in range (num, 0, -1):
 #   print(numbers(num))



#num = 5
#for i in range (num):
 # for j in range(i, num):
  #  print(" ", end = " ")

  #for j in range(i + 1):
   # print("X", end = " ")
  #print()


#num = 5
#for i in range (num):
 # for j in range(i + 1):
  #  print(" ", end = " ")

  #for j in range(i, num):
   # print("X", end = " ")
  #print()

#def numbers(num):
  #for i in range (num):
    #for j in range (i, num):
     # print(" ", end = " ")
    #for j in range (i-1):
    #  print("*", end = " ")
   # for j in range (i):
  #    print("*", end = " ")  
 #   print() 
#num = 5
#numbers(num)

#num = 10
#for i in range(num):
 # for j in range(i):
  #  print(" ", end= " ")
  #for j in range(i, num):
   # print("*", end=" ")
  #for j in range(i, num+1):
   # print("*", end=" ")
  #print("")
#for i in range (num):
 # for j in range(i, num):
  #  print(" ", end = " ")
  #for j in range(i):
   # print("*", end= " ")
  #for j in range(i+1):
   # print("*", end= " ")
  #print()
#num = 4
#for i in range (num):
 # for j in range(i, num):
  #  print("-", end = " ")
  #for j in range (i):
   # print("*", end = " ")
  #for j in range (i-1):
   # print("*", end = " ")
 # for j in range (i,num-1):
  #  print("-", end = " ")
  #for j in range (i, num-1):
   # print("-", end =" ")
  #for j in range (i):
   # print("*", end = " ")
 # for j in range (i-1):
  #  print("*", end = " ")
  #print()
#num = 12
#for i in range(num):
 # for j in range(i):
   # print("-", end= "")
  #for j in range(i, num):
    #print("*", end = " ")
  #print()
#def num(number):
  #length = (number * 2)- 1
  #space = (length + 1)// 2
  #i = 1
  #while i <= number - 1:
    #print(" " * (space + 1 - i), "*" *(2*i - 1))
   # i +=1 
  #i = number
  #while i > 0:
  #  print(" "* (space + 1 -i ), "*" *(2*i-1))
 #   i -= 1
#count = 1
#number = 5
#while count <= 20:
 # num(number)
  #count+= 1

#def number(num):
  #length = num
  #space = length
  #i = num
  #while i > 1:
    #print(" " * (space + 1-i), "*" *(length))
   # i -= 1
  #i = 1
  #while i <= num - 1:
  #  print(" " * (space-i), "*" *(length - 1))
 #   i+= 1
#count = 1
#num = 20
#while count <= 10:
  #number(num)
 # count+=1

#number = int(input("enter number: "))
#for i in range (2, number):
  #if number % i == 0:
  #  print (number, "is not a prime number")
 #   break
#else:
 #   print(number, "is a prime number")

#def reversed_name(name):
  #num_name = len(name)
  #for i in range(num_name -2, -2,  -2):
  #  print(name[i], end = " ")
 # return num_name
#name = "pynative"
#reversed_name(name)


#def odd_number(num):
 # for i in range (1, num):
  #  count = i -1
 #   count += i
#    print(count)


#num = 10
#odd_number(num)


#def converting_str_list(name):
  #output = []
  #for i in name:
  #  output.append(i)
 # output.pop(1)
  #output.insert(1, "rat")
 # return output
  

#name = "cat", "dog", "fish", "lion"
#n = (converting_str_list(name))
#print(n)


#def converting_str_list(number):
  #output = []
  #for i in number:
 #   output.append(i)
#  return output


#number = 1,2,3,4,5
#print(converting_str_list(number))

# QUIZ GAME
#count = 0
#name = input("enter name: ").upper()
#print("Welcome to who wants to be a millionaire", name)
#question1 = input("(Q1) Who is the first programmer: ")
#question2 = int(input("(Q2) In what year did programming started: "))
#question3 = input("(Q3) Who is the father of computer: ")
#print("\n")
#if question1 == "Ada lovelace":
  #print("(Q1) correct")
 # count += 1
#else:
 # print("(Q1) incorrect")
  
#if question2 == 1883:
  #print("(Q2) correct")
 # count += 1
#else:
 # print("(Q2) incorrect")
  
#if question3 == "Charles babbage":
 # print("(Q3) correct")
 # count += 1

#else:
 # print("(Q3) incorrect")
#print("Thank you, You attempt", 3, "questions")
#print("Total = ", count)
#print ("*" * 20, "CONGRATULATION YOU CAN MOVE TO NEXT LEVEL", name, "*" * 20)
#print("\n")




#def num(n):
 # return random.randrange(n)
#def sum(n):
  #number = num(5)
 # return number + n
#print(sum(5))

#output =[]
#word = "banana"
#length_word = len(word)
#for i in range (length_word):
  #for j in range (length_word -1, i, -1):
   # palindromic_word = word[i:j+1]
  #  if palindromic_word == palindromic_word[::-1]:
 #     output.append(palindromic_word)
#print(output)
#max = output[0]
#for i in output:
 # if len(i) > len(max):
 #   max = i
#print ("the longest palindromic word: ",max)

# To determine leap year
#year  = int(input("year: "))
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
 # print(year, "is a leap year")
#else:
 # print(year, "is not a leap year")

#n = []
#number = [2,3,4,5,7,8,6,4,3,2,1,1,4,6,2]
#for i in number:
  #if i not in n:
  #  n.append(i)
 #   n.sort()
#print(n)


#n = []
#name = "output"
#for i in name:
 # if i not in n:
#    n.append(i)
#print(n)

#print("\n")

##############


temperature = int(input("Temperature: "))
print(""" \n 1.Temperature from Fahrenheit to Celsius \n 2.Temperture from Celsius to Fahrenheit \n""")
specify = int(input("specify: "))
Celsius = (temperature - 32) * 5/9
Fahrenheit = (temperature * 9/5)+32
count = True
while count:
  if specify == 1:
    print(Celsius)
    break
  if specify == 2:
    print(Fahrenheit)
  else:
    print("choose the correct option by inputing (1, 2)")
  break
print("\n")


import calendar
year = 2023
month = 12
for i in range (1, 12 + 1):
  print(calendar.month (year, i))

import time
print(time.ctime(1674130219.8171587))










 
  