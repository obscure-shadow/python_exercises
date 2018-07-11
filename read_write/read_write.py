# Permission options: r: read, w: write, a: append, r+: read and write
# with open(filename, permission)
with open('text.txt','w') as testfile:
    testfile.write("Hello, C25. Hope your're having a great day." + '\n')


with open('text.txt','a') as testfile:
    testfile.write("Hello, C25. Hope you are awake.")

#it will make a new instance if it is not there... when it appends there will be no formatting.

nickset = {"the mooch", "knuckles", "Burninator", "Kneecap", "ole red", "bubba", "og", "kitkat", "spanky",
    "Monkeybutt","L'il Devil","bird person", "fancy slacks"}

nameset = {"bob smith", "Charles Anderson", "henry goldberg", "kimmi bird", "jissi david","steve brownlee"}

with open("data/nicknames.txt", "w") as nicknames:
    for nick in nickset:
        nicknames.write(nick + '\n')

with open("data/names.txt", "w") as names:
    for name in nameset:
        names.write(name + '\n')

#later, back at the batcave...

namelist= []
nick_list = []

with open("data/names.txt", "r") as names:
    namelist = names.readlines()
    print(namelist)

with open("data/nicknames.txt", "r") as names:
    nick_list = names.readlines()
    print(nick_list)

mob_names = [f"{name.strip().split(' ')[0]} \"{nick_list[i].strip()}\" {name.strip().split(' ')[1]}"
    for i, name in enumerate(namelist)]

print(mob_names)