squares = [i**3 for i in range(1,11)]
print(squares)
print()
original_list = ["january","february","march","april","may","june","july","august","september","october","november","december"]
print("Original list:\n", original_list,"\n")
print("Three-letter abbreviation 1 - 12:")
new_list = []
for i in original_list:
    new_list.append(i[:3].title())
    print(i[:3].upper(),end = "|")
print("\n\nNew list:\n" , new_list)
print()
cubed = range(11)
for i in cubed[1:]:
    print(f'{i**3}')
print()
a = int(input("Enter the number:"))
print(f'{"The Range"} {a} {"Cubed"}')
cubed = range(a+1)
for i in cubed[1:]:
    print(f'{i**3}')