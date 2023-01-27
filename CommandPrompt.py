import time #Comes with python: no module install needed ;)
command = '' #Sets this variable in the very beginning so our "while" loop isn't confused. 

print('Hello and welcome to my command prompt program')
while command != 'exit': #Repeats this until the user enters "exit."
  print('Enter a command or enter "help" for a list of commands.')
  command = input()
  command = command.lower() #makes the input the user entered lowercase so the commands aren't case sensitive.
  if command == "help": #Make sure the word in parentheses is lowercase since we turn their input into a lowercase input. 
    print('Here is a list of commands:')
    print('help - shows this message')
    print('date - displays the current date')
    print('time - displays the current time')
    print('exit - closes this program')
  elif command == "date":
    print("The current date is " + time.strftime("%Y-%m-%d")) # strftime is a function of the "time" module
  elif command == "time":
    print("The current time is " + time.strftime("%H:%M"))
