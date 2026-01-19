name = input("type your name: ")
print("welcome", name, "to this adventure!")

answer = input(
    "you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? "
).lower()

if answer == "left":
    answer = input(
        "you come to a river, you can walk around it or swim across. type walk or swim: "
    ).lower()

    if answer == "swim":
        print("you swim in cold water and lose")

    elif answer == "walk":
        print("you walk for many miles and lose")

    else:
        print("not a valid option. you lose")

elif answer == "right":
    answer = input(
        "you come to a bridge, do you want to cross it or head back? (cross/back): "
    ).lower()

    if answer == "back":
        print("you go back and lose")

    elif answer == "cross":
        answer = input(
            "you cross the bridge and meet a stranger. do you talk to them? (yes/no): "
        ).lower()

        if answer == "yes":
            print("you talk to the stranger and they give you gold. you win!")

        elif answer == "no":
            print("you ignore the stranger, they get offended, and you lose")

        else:
            print("not a valid option. you lose")

    else:
        print("not a valid option. you lose")

else:
    print("not a valid option. you lose")

print("thank you for trying,", name)
