from datetime import date
name = input()
date = date.today()
letter = f'''
Dear {name},
You are selected
date:- {date}
'''
print(letter)
