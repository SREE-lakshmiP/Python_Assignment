
size = int(input("Enter dictionary size: "))

input_dict = {}
for i in range(size):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for key '{key}': ")
    input_dict[key] = value


sorted_dict = dict(sorted(input_dict.items()))
print("Sorted Dictionary:")
for key, value in sorted_dict.items():
    print(f"{key}: {value}")