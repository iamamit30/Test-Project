letter = '''Dear <|NAME|>,

Greetings from Ericsson Global Limited. 
We are happy to tell you about your selection.

You are selected!
Have a great day ahead!

Thanks and regards,
Ericsson HR Team
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
from datetime import date
today = date.today()
today = str(today)
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", today)
print(letter)