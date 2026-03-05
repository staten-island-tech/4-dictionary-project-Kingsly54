Laptop={
    "name":"MacBook Air (M4, 13.6‑inch)",
    "price":"$899",
    "color":"Silver"
}
Pencil={
    "name":"Dixon Ticonderoga 2B Graphite Pencil, Wood-Cased, Yellow, 12-Pack",
    "price":"$2.50",
    "color":"orange"
}
Gun={
    "name":"AK-47 7.62×39mm Semi-Automatic Rifle",
    "price":"2.00",
    "color":"black"
}
Basketball={
    "name":"Wilson Evolution Game Basketball, Official Size 29.5",
    "price":"99.99",
    "color":"black"
}
Cart=[]
idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
Num=0
if idk == "Basketball":
    print(Basketball["name"])
    bre=input("Would you like to add to cart?")
    price=Basketball["price"]
elif idk == "Gun":
    print(Gun["name"])
    bre=input("Would you like to add to cart?")
    price=Gun["price"]
elif idk == "Laptop":
    print(Laptop["name"])
    bre=input("Would you like to add to cart?")
    price=Laptop["price"]
elif idk == "Pencil":
    print(Pencil["name"])
    bre=input("Would you like to add to cart?")
    price=Gun["price"]
if bre=="Yes" or "yes":
    Cart.append(idk)
    Num+=price

    
print(Cart)
print(Num)