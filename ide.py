import time, os, sys

def clear():
  os.system('clear')

clear()
user = os.environ['REPL_OWNER']
try:
  print(f'Welcome {user} to the Python IDE!')
  time.sleep(2)
  clear()
except:
  print('It seems like you dont have a REPL account... Heres more info: ',sys.exc_info())
  os.environ['REPLIT_DB_URL']
  time.sleep(2)
  clear()

IDE=True
file = True
while file:
  print('Python IDE')
  print('\t[1] Make a file\n\t[2] Edit a file\n\t[3] Read a file\n\t[4] Delete a file')
  file2 = input('  >>> ')
  clear()

  if file2 == '1':
    print('FILE')
    print('What will be the name of your file? (Dont enter the .py)')
    file_name=input('>>> ')

    py_file=open(file_name+'.py','a')
    py_file.close()
    clear()

  elif file2 == '2':
    print('FILE')
    print('What is the name of the file? (Dont enter the .py)')
    file_name2 = input('>>> ')
    clear()

    while IDE:
      print("What do you want to put in the file?\nNote: Enter 'quit' to quit out of writing in the file\nNote: Everything that has indentation is currently unavailable")
      put_in=input('\n>>> ')
      clear()

      if put_in == 'quit':
        IDE=False
      if put_in[-1:] == ':':
        with open(file_name2+'.py') as file:
          file.write(put_in+'\n  ')
          file.close()
      elif put_in[-1:] == ']':
        with open(file_name2+'.py') as file:
          file.write(put_in+'\n  ')
          file.close()
      elif put_in[-1:] == '}':
        with open(file_name2+'.py') as file:
          file.write(put_in+'\n  ')
          file.close()
      else:
        with open(file_name2+'.py','a') as file:
          file.write(put_in+'\n')
          file.close()

  elif file2 == '3':
    print('FILE')
    print('What is the name of the file? (dont enter the .py)')
    file_name3=input('>>> ')
    clear()

    with open(file_name3+'.py','r') as file:
      print(file.read())
      file.close()
    
    time.sleep(6.5)
    clear()

  elif file2 == '4':
    print('FILE')
    print('What is the name of the file? (dont include the .py)')
    file_name4 = input('>>> ')
    clear()

    try:
      os.remove(file_name4+'.py')
      print('File Removed!')
      time.sleep(2)
      clear()
    except:
      print('No such file exists!')
      time.sleep(2)
      clear()

  else:
    print('Invalid Choice!')
    time.sleep(2)
    clear()
