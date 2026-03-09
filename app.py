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
def breh():
    Cart=[]
    idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
    Num=0
    if idk == "Basketball":
        print(Basketball["name"])
        bre=input("Would you like to add to cart?")
        pric=Basketball["price"]
        price=float(pric)
        if bre=="Yes" or "yes":
            Num+=price
            Cart.append(Basketball["name"])
            Ask=input("Would you like to buy more?")
            if Ask=="Yes" or "yes":
                idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
    elif idk == "Gun":
        print(Gun["name"])
        bre=input("Would you like to add to cart?")
        pric=Gun["price"]
        price=float(pric)
        if bre=="Yes" or "yes":
            Num+=price
            Cart.append(Gun["name"])
            Ask=input("Would you like to buy more?")
            if Ask=="Yes" or "yes":
                idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
    elif idk == "Laptop":
        print(Laptop["name"])
        bre=input("Would you like to add to cart?")
        pric=Laptop["price"]
        price=float(pric)
        if bre=="Yes" or "yes":
            Num+=price
            Cart.append(Laptop["name"])
            Ask=input("Would you like to buy more?")
            if Ask=="Yes" or "yes":
                idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
    elif idk == "Pencil":
        print(Pencil["name"])
        bre=input("Would you like to add to cart?")
        pric=Pencil["price"]
        price=float(pric)
        if bre=="Yes" or "yes":
            Num+=price
            Cart.append(Pencil["name"])
            Ask=input("Would you like to buy more?")
            if Ask=="Yes" or "yes":
                idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
    print(Num)
    print(Cart)