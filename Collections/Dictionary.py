dic1={"song":"adi penne","love":"mom","fav":"Tea","missing":"home"}
print("1.Display the elements \n2.Display the datatype \n3.Length of a dictionary \n4.Adding items to the dictionary \n5.Updating the value of a key \n6.Creating a copy of the dictionary \n7.Removing items from the dictionary \n8.Removing all the items from the dictionary \n9.Displaying only keys \n10.Displaying only values \n11.Display full dictionary using for loop \n12.To Check whether an element exists or not" )
n=int(input("Enter your choice:"))
if(n==1):
    print("Displaying dictionary elements:",dic1)
elif(n==2):
    print("Datatype of the elements:",type(dic1))
elif(n==3):
    print("Length of the dictionary:",len(dic1))
elif(n==4):
    print("Adding elements in the dictionary:",dic1)
    dic1["series"]="Stranger Things"
    print("After adding elements in the dictionary:",dic1)
elif(n==5):
    print("Updating the value in the dictionary:",dic1)
    dic1["fav"]="cofi"
    print("After updating the value in the dictionary",dic1)
elif(n==6):
    print("Creating copy of a dictionary:")
    dic2=dic1.copy()
    print ("dictionary1:",dic1)
    print ("dictionary2 :",dic2)
elif(n==7):
    print("Removing items from the dictionary")
    del dic1["fav"]
    print("After removing:",dic1)
elif(n==8):
    print("Removing all items from the dictionary")
    dic1.clear()
    print(dic1)
elif(n==9):
    print("Displaying only keys:")
    for a in dic1.keys():
      print("Keys are:",a)
elif(n==10):
    print("Displaying only Values:")
    for a in dic1.values():
       print("Values are:",a)
elif(n==11):
    print("Display full dictionary using for loop:")
    for x,y in dic1.items():
      print(x," == ", y)
elif(n==12):
    print("To Check whether an element exists or not:")
    if dic1.get("song")==None:
      print ("No such element")
    else:
      print("Element exists")
else:
    print("Invalid Input!!!!")
