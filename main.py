import json

menu = ["pizza","soda","energy drink"]
print(menu)
input1 = input("Hi. Welcome to debonaiz. Choose any of the category above:  ")

with open('products.json','r') as a:
    data = json.load(a)
    for dub in data[input1]:
        print(dub['name'],dub['price'])
