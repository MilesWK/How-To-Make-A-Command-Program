# How-To-Make-A-Command-Program
This repository will help you learn how to make a program in Python that receives user input and gives output.  

To start, we need a new program called "command prompt," or whatever you want to call it. 

In the beginning of that program, we need to define the variables and import modules:
```python
import time #Comes with python: no module install needed ;)
command = '' #Sets this variable in the very beginning so our "while" loop isn't confused. 
```

...Wow. That's not a lot of variables. Now we need to give a nice little "intro" to our program:
```python
print('Hello and welcome to my command prompt program')
while command != 'exit': #Repeats this until the user enters "exit."
  print('Enter a command or enter "help" for a list of commands.')
  command = input()
  command = command.lower() #makes the input the user entered lowercase so the commands aren't case sensitive.
```
That will make it so the user can enter a command, and after the command is done running, the user can enter another command. If the user enters "exit" as their command, this loop will stop running and end the program. 

**Next**, we need to set up our "help" command under the ```command = input()``` line. This should be indented one tab:
```python
  if command == "help": #Make sure the word in parentheses is lowercase since we turn their input into a lowercase input. 
    print('Here is a list of commands:')
    print('help - shows this message')
    print('date - displays the current date')
    print('time - displays the current time')
    print('exit - closes this program')
```
Now if the user enters "help," it will show them three commands they can enter and what each command will do. 

Next we need to add our "date" command using the "time" module we imported in the very beginning of our program. This will be under the "if" statement of our "help" command: 
```python
  elif command == "date":
    print("The current date is " + time.strftime("%Y-%m-%d")) # strftime is a function of the "time" module
```
Now for our final command that we need an "if" statement for: the time command! This is just like our "date" command:
```python
  elif command == "time":
    print("The current time is " + time.strftime("%H:%M"))
```
We have now fininshed the script with our commands. Now we need to add the "else" statement for if the user enters an invalid command:

```python
  else:
    print(command + " is an invalid command")
```
**We have finished the program!**

Here is the completed program:
```python
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
 ```
 
 If you want more commands, just add more "elif" statments! Just be sure the input to activate that command is lowercase, because in the beginning, of our program, we set the user input to lowercase. 
 Please be sure give credit to me if you use it publicly. 
