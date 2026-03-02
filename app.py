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

idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
if idk == "Basketball":
    print(Basketball["name"])
if idk == "Gun":
    print(Gun["name"])
if idk == "Laptop":
    print(Laptop["name"])
if idk == "Pencil":
    print(Pencil[0]["name"])