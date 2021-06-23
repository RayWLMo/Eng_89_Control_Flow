# # Syntax - if variable -condition age:
#
# weather = "sunny"
#
# if weather == "sunny":  # If this condition is true, the next line would execute
#     print("Enjoy the weather!")  # This line needs to be inside the if code block - indented
#
# elif weather != "sunny":
#     print("Might need to bring an umbrella")
# else:
#     print("Have a nice day!")
# # Let's create a ticket age criteria
#
# age = 16
#
# if age < 18:  # Checking age provided
#     print("You are not eligible to watch this movie, please choose an age appropriate movie")
# else:
#     print("Enjoy the movie!")
#
# # Loops - for loops and while loops
#
# # Loops help us iterate through our data, such as lists, dict, sets etc.
#
# shopping_list = ["eggs", "apples", "milk", "bread", "butter"]
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])
# print(shopping_list[4])
#
# # Syntax - for ___ in ___:
#
# # Using a for loop to iterate through the list
#
# for items in shopping_list:
#     print(items)
#
# Second Iteration with if conditions
# shopping_list = ["eggs", "apples", "milk", "bread", "butter", 1, 2, 3, 4, 5, 6, 7, 8]
# for items in shopping_list:
#     if items == "butter":  # if this condition is true
#         break  # stop the loop
#     print(items)
#
# # Be wary of indefinite loops
#
# Third Iteration with dict
# student_data = {
#     "student_name": "Jim",  # string
#     "course": "DevOps",  # string
#     "course_topics": 5,  # int
#     "topic_names": ["Business Week", "Python", "DevOps", "Virtualisation with Vagrant", "AWS Cloud"]  # List
# }
# print(student_data)
#
# # Iterating through the dict
# for data in student_data.values():
#     if data == "Jim":  # if the condition is True, the loop exits
#         print(data)
#
# # In any case for loop would iterate through the data until the last item of condition is True
#
# # While Loops are essentially used to monitor the data
# # The while statement is used for repeated execution as long as an expression is true
#
# # First Iteration of while loop
# num = 0
#
# while num < 10:
#     print(f"It's working -> {num}")
#     num += 1  # Adds 1 to num value each iteration
#
# # 10th iteration, the loops stops
#
# # Second Iteration
# num = 0
#
# while num < 10:
#     print(f"Its working -> {num}")
#     if num == 5:
#         break
#     num += 1

# # Let's see how a user can interact with while loops in the 3rd iteration
#
# # Activity
# # Prompt the user to input age and restrict the user to enter in digits only
# # Check if the data is in digits, display it back to the user
# # If data is not in digits, prompt the user for data with message to enter in digits
#
# user_prompt = True
# while user_prompt:
#     age = input("Please enter your age:    ")
#     print(age)
#     if age.isdigit() == True and int(age) < 150:
#         print(f"Your age is {age}")
#         user_prompt = False
#     elif int(age) > 150:
#         print(f"your age is obviously not {age}. Please enter a valid age in digits:    ")
#     else:
#         print("Your age entered is invalid. Please enter your age in digits")

