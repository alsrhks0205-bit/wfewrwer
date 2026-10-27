# dictionary


x = {
    "name": None,
    "atk": 10,
    "hp": 100
}
print(x)

x["hp"] = 200

print(x.get("atk"))

print(x["name"])

print(x["hp"])

print("atk" in x)

for elem in x:
    print(elem)
    print(type(elem))

for elem in x.items():
    print(elem)
    print(type(elem))
