Laptop={
    "name":"MacBook Air (M4, 13.6‑inch)",
    "price":899,
    "color":"Silver"
}
Pencil={
    "name":"Dixon Ticonderoga 2B Graphite Pencil, Wood-Cased, Yellow, 12-Pack",
    "price":2.50,
    "color":"orange"
}
Gun={
    "name":"AK-47 7.62×39mm Semi-Automatic Rifle",
    "price": 2.00,
    "color":"black"
}
Basketball={
    "name":"Wilson Evolution Game Basketball, Official Size 29.5",
    "price":99.99,
    "color":"black"
}
def breh():
    Cart=[]
    Num=0
    idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
    for i in idk:
        if idk == "Basketball":
            print(Basketball["name"])
            bre=input("Would you like to add to cart?")
            pric=Basketball["price"]
            if bre=="Yes" or "yes":
                Num+=pric
                Cart.append(Basketball["name"])
                idk=0
        elif idk == "Gun":
            print(Gun["name"])
            bre=input("Would you like to add to cart?")
            pric=Gun["price"]
            if bre=="Yes" or "yes":
                Num+=pric
                Cart.append(Gun["name"])
                idk=0
        elif idk == "Laptop":
            print(Laptop["name"])
            bre=input("Would you like to add to cart?")
            pric=Laptop["price"]
            if bre=="Yes" or "yes":
                Num+=pric
                Cart.append(Laptop["name"])
                idk=0
        elif idk == "Pencil":
            print(Pencil["name"])
            bre=input("Would you like to add to cart?")
            pric=Pencil["price"]
            if bre=="Yes" or "yes":
                Num+=pric
                Cart.append(Pencil["name"])
                idk=0
        Ask=input("Would you like to buy more?")
        if Ask=="No" or Ask=="no":
            print(Num)
            print(Cart)
        else:        
            idk=input("What would you like to buy Items include: Basketball, Pencil, Gun, Laptop")
breh()