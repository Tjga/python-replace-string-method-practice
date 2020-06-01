user_input_string = input("Enter a String: ")
old_char = input("What letter do yo want to replace: ")
new_char = input("with what do you want to replace it with: ")

new_user_string = user_input_string.replace(old_char, new_char)

end_result = "Your new Sentence / word is: " + new_user_string

print(end_result)