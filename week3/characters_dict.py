#character is the dictionary, which is based off naruto
Character = {
    "Name": "Naruto",
    "Hp": 100,
    "Attack": "Shadow Clone"
}
Character["Attack"] = "Rasengan"
#the "attack" key is changed to rasengan using "Change value"

for key in Character:
    print(Character[key])
#Used a for loop to print all values one by one