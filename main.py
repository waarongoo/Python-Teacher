import turtle
def lesson2():
  print("Ok so for this next lesson we are gonna use something called turtle. What is turtle? It is like the animal turtle you may ask? No, its a python package for drawing. Is it slow? No its very fast depending on the computer resources\n")
  print("In this package, we can do different things with the turtle. Now choose what do you want to do with the turtle.")

  cont = True
  while cont == True:
    choice = input("Enter 1 to move the turtle forward, 2 to move backwards, 3 to turn left, 4 to turn right, 5 to clear your drawing, and 6 to stop drawing.\n")
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
      print("Your have cleared your drawing! All of your work is now unrecoverable!")
      turtle.clear()


def startlesson1():
  print('Please type in print("Hello World") to print Hello World to the console\n>>>')
  user = input()
  if user == 'print("Hello World")':
    print("Nice job!")
    lesson2()

name = input("Hello my name is Robert. What is your name?\n>>>")
doing = input("Hello " + name + " how are you doing?\n>>>")
  
if doing =="good":
  print("Awesome Lets do our first lesson....")
  startlesson1()
if doing =="bad":
  print("Oh well thats sad. Lets do our first lesson anyways....")
  startlesson1()



