num = int(input("Enter a number:"))
while num == 7:
    print(num)
    if num == 7:
        print("7 is the lucky number!")
        break
while num != 7:
    print("you are currently in a loop!")
    continue
