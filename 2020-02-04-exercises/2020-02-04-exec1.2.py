
name = input("Hello, what is your first name? :    ").strip().capitalize()
eye_colour = input(f"{name} huh, what a lovely name! What colour are your eyes? :    ").strip().lower()
hair_colour = input("Beautiful! What about the colour of your hair? :    ").strip().lower()
age = int(input (f"Gorgeous! And finally {name}, how old are you? :    ").strip())


print (f"Hello {name}, you have {eye_colour} eyes and {hair_colour} hair, and you are {age} years old. Have a nice day! :)")
print (f"Also {name}, I predict you were born in {2020 - age} or {2019 - age}, as you said you were {age} years old!")