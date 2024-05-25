# `title()` method makes each word in a string begin with a capital letter
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
# These strings are called f-strings.The f is for format, because Python formats the string by replacing the name of any
# variable in braces with its value.
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(quote)
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)
famous_person = " albert einstein "
strip_famous_person = famous_person.strip()
title_famous_person = strip_famous_person.title()
print(f'{title_famous_person} once said,\n\t"A person who never made a mistake never tried anything new."')

file_name = 'python_notes.txt'
print(file_name)
remove_suffix_file_name = file_name.removesuffix(".txt")
print(remove_suffix_file_name)