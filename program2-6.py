# category winds (mph) damage
# 1 74-95 some
# 2 96-110 extensive
# 3 111-129 devastating
# 4 130-156 catastrophic
# 5 157+ catastrophic

userAnswer = int(input("Please type in the wind speed to find out the potential damage: "))

if userAnswer < 74:
    print("You're fine.")
elif userAnswer < 96:
    print("Some damage.")
elif userAnswer < 111:
    print("Extensive damage.")
elif userAnswer < 130:
    print("Devastating damage.")
elif userAnswer < 157:
    print("Catastrophic damage.")
else:
    print("This is not a hurricane. Chill out.")