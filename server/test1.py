

name = "Blake"
last = "Turner"

print(name)

list
prices = [12,32,44,55.23,45.03]

print(prices)

print(prices[0])

total = 0
for price in prices:
    #print(price)
    total += price
    
print(total)

#dictionary
me = {
    "name": "Blake",
    "last": "Turner",
    "age": "28"
}

print(me)

#read
print(me["name"])

#Modify
me["age"] = 99

#add
me["email"] = "mrbturner2013@yahoo.com"

print(me)

#opt 1 -Check]
if "hobbies" in me:
    hobbies = me["hobbies"]
    print(hobbies)

#opt 2 - read or default
hob2 = me.get("hobbies", "No hobbies")
print(hob2)

print("should work")