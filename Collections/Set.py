s1={23,37,91.8,10,"python",(10,20,30)}
s2=set([3,8,1,9,10])
print("\n1.Print set elements\n2.Datatype of t1\n3.Add an element to s1\n4.Update elements\n5.Discard\n6.Remove\n7.Clear s1\n8.Union of s1 and s2\n9.Intersection of s1 and s2\n10.Difference of s1 and s2\n11.Symmetric difference of s1 and s2\n12.Check  s2 is disjoint of s1\n13.Check  s2 is subset of s1\n14.Pop operation\n15.Copy\n16.Display elements in s1 using for loop\n17.Display maximum value\n18.Display minimum value\n19.Sum of elements in set\n20.Sort operation\n21.Length of the set")
n=int(input("\nPress any number : "))
if(n==1):
  print("s1 elements : ",s1)
  print("s1 elements : ",s2)
elif(n==2):
  print("datatype of s1 : ",type(s1))
  print("datatype of s2 : ",type(s2))
elif(n==3):
  e=str(input("Enter a string element to be added to the s1 : "))
  s1.add(e)
  print(s1)
elif(n==4):
  s2.update([15,20,25,30,35])
  print("Updated elements in s2 : ",s2)
#remove,discard and clear opartions
elif(n==5):
  s2.discard(3)
  print("3 in s2 is discarded",s2)
elif(n==6):
  s2.remove(8)
  print("Element 8 is removed from s2",s2)
elif(n==7):
  s1.clear()
  print("s1 is cleared : ",s1)
#Operations
elif(n==8):
  print("Union of s1 and s2 : ",s1|s2)
elif(n==9):
  print("Intersection of s1 and s2 : ",s1&s2)
elif(n==10):
  print("Difference of s1 and s2 : ",s1-s2)
elif(n==11):
  print("Symmetric difference of s1 and s2 : ",s1^s2)
elif(n==12):
  print("Is s2 is disjoint of s1 ? :  ",s1.isdisjoint(s2))
elif(n==13):
  print("Is s2 is superset of s1 ? : ",s1.issuperset(s2))
#general
elif(n==14):
  v=s1.pop()
  print("Poped element from s1 : ",v)
  print("s1 after poping a random element : ",s1)
elif(n==15):
  s3=s1.copy()
  print("s1 is copied to s3 : ",s3)
elif(n==16):
  print("Elements in s1 : ")
  for i in set(s1):
    print(i)
#mathematical operations
elif(n==17):
  print("Maximum value in s2 is : ",max(s2))
elif(n==18):
  print("Minimum value in s2 is : ",min(s2))
elif(n==19):
  print("Sum of elements in s2 : ",sum(s2))
elif(n==20):
  print("Elements of s2 is sorted : ",sorted(s2))
elif(n==21):
  print("Length of s1 is : ",len(s1))
else:
  print("Enter valid input!!!")
