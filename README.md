# Python Control Flow with if, elif and else conditions

- Syntax - `if variable -condition:`
```Python
weather = "sunny"

if weather == "sunny":  # If this condition is true, the next line would execute
    print("Enjoy the weather!")

elif weather != "sunny":
    print("Might need to bring an umbrella")
else:
    print("Have a nice day!")
```
- Ensure the contents of the condition is inside the if code block -  it needs to be indented

###Lets create a ticket age criteria
```Python
age = 16

if age <18:  # Checking age provided
    print("You are not eligible to watch this movie, please choose an age appropriate movie")
else:
    print("Enjoy the movie!")
```

# Loops - for loops and while loops