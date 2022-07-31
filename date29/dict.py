from cgi import print_arguments


bookName = {
    "physics": "HC Verma,NCERT",
    "maths": "arihant",
    "age": "nahi batyenge"
}
print(bookName.keys())
print(bookName.values())
bookName.update({"age": 21})
bookName.pop("age")
print(bookName)
