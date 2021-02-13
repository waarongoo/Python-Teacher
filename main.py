import turtle
from termcolor import colored
import sys
import time

def lesson3():
  print("Time to practice that you just learned")
  user = input("How do you print something in the console ")
  if user =="print()":
    print("Good Job!")
  else:
    print("Huh it seem you forgot\n")
    print("The answer is print()")

def lesson2():
  print("Ok so for this next lesson we are gonna use something called turtle. What is turtle? It is like the animal turtle you may ask? No, its a python package for drawing. Is it slow? No its very fast depending on REPLs computer resources\n\n\n")
  print("In this package, we can do many different things with the turtle. Now choose what do you want to do with the turtle.\n\n\n")


  print("Welcome to the Python Turtle IDE\n\n\n\n")
  go = True
  while go == True:
    choice = input("Enter 1 to move the turtle forward, 2 to move backwards, 3 to turn left, 4 to turn right, 5 to clear your drawing. 6, to stop drawing\n")
    if choice == "1":
      length = input("How far do you want to move forward?")
      turtle.forward(int(length))
    if choice == "2":
      length = input("How far do you want to move backwards?")
      turtle.backward(int(length))
    if choice == "3":
      length = input("How many degrees do you want to turn left?")
      turtle.left(int(length))
    if choice == "4":
        length = input("How many degrees do you want to turn right?")
        turtle.right(int(length))
    if choice == "5":
      print("Your have cleared your drawing!")
      turtle.clear()
    if choice == "6":
      go=False
      print("Did you have fun? If so great! Lets go to the next lesson")
      lesson3()


      
      

def startlesson1():
  print('Now lets learn how to print stuff in the console. What is the console? The console is the black box that tells you stuff. How do I print stuff? Well to do that use this print("Hello World"). Here try it yourself.\n>>>')
  user = input()
  if user == 'print("Hello World")':
    print("Hello World")
    print("Nice job! Alright lets go to the next lesson")
    lesson3()
  else:
    print("Please enter the exact values above")
    startlesson1()

for x in colored("Welcome To the Online Python Teacher\n", "white"):
	sys.stdout.write(x)
	sys.stdout.flush()
	time.sleep(0.05)
name = input("Hello my name is Robert your virtual teacher. What is your name?\n>>>")
doing = input("Hello " + name + " how are you doing?\n>>>")
print("This project was inspired by COVID-19 Distance Learning Copyright awdev.")
for x in colored("\nAll rights reserved.\n", "red"):
	sys.stdout.write(x)
	sys.stdout.flush()
	time.sleep(0.00)
startlesson1()



  






