input_str = input("Enter a string: ")
input_str = input_str.replace(" ", "").lower()

if len(set(input_str)) == len(input_str):
    print(True)
else:
    print(False)


