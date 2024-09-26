# Sum and Average
#1
# tup=(34,26,67,2,8,12,9)
# sum=0
# for i in tup:
#     sum=sum+i
# print(sum)
# average=sum / len(tup)
# print(average)

#Add method in Sets
#1
# sets={3,3,45,42,56,89,21,56}
# sets.add(200)
# print(sets)

#2
# sets={3,45,42,56,89,21,"ajay"}
# sets.add(200)
# print(sets)

#3
# sets={"ajay","prabhas","ram","suman","prabhas"}
# sets.add("NTR")
# print(sets)

#4
# sets={"ajay",67,36,"prabhas",69,42,"ram","suman",98}
# sets.add("sai")
# print(sets)

#5
# sets={23.5,56.3,44.0,56.1,22.9}
# sets.add(87.0)
# print(sets)

#Update method in sets
#1
# sets={3,3,45,42,56,89,21,56}
# li=[2,45,91,45,2,63,78]
# sets.update(li)
# print(sets)

#2
# sets={3,3,45,42,56,89,21,56}
# li=["ajay","prabhas","ram","suman","prabhas"]
# sets.update(li)
# print(sets)

#3
# sets={3,3,45,42,56,89,21,56}
# li=("ajay","prabhas","ram","suman","prabhas")
# sets.update(li)
# print(sets)

#4
# sets={3,3,45,42,56,89,21,56}
# li=("ajay",67,36,"prabhas",69,42,"ram","suman",98)
# sets.update(li)
# print(sets)

#5
# sets={3,3,45,42,56,89,21,56}
# li={23.5,56.3,44.0,56.1,22.9}
# sets.update(li)
# print(sets)

#Copy method in sets
#1
# sets={3,3,45,42,56,89,21,56}
# li=sets.copy()
# print(id(sets))
# print(id(li))

#2
# sets={3,3,45,42,56,89,21,56}
# li=sets
# print(id(sets))
# print(id(li))

#3
# sets={"ajay",67,36,"prabhas",69,42,"ram","suman",98}
# li=sets.copy()
# print(id(sets))
# print(id(li))

#4
# sets={"ajay",67,36,"prabhas",69,42,"ram","suman",98}
# li=sets
# print(id(sets))
# print(id(li))

#5
# sets={3,3,45,42,56,89,21,56}
# li={"ajay",67,36,"prabhas",69,42,"ram","suman",98}
# set=sets
# copy_li=li.copy()
# print(id(sets))
# print(id(set))
# print(id(li))
# print(id(copy_li))

#pop method in sets
#1
# a={3,89,2,42,81,3,5}
# print(a.pop())

#2
# a={3,89,1,42,81,3,5}
# s=a.pop()
# print(a)

#3
# a={"a","x","s","q","z","h"}
# print(a.pop())

#4
# a={"a","x","s","q","z","h"}
# a.pop()
# print(a)

#5
# a={3,89,1,42,81,3,5}
# a.pop()
# print(a)

#Remove Method
#1
# a={3,89,2,42,81,3,5}
# print(a.remove(89))  #It return None Output

#2
# a={3,89,2,42,81,3,5}
# a.remove(89)
# print(a)

#3
# a={3,89,2,42,81,3,5}
# s=a.remove(89)  #It returns None output
# print(s)

#4
# a={"a","x","s","q","z","h"}
# a.remove("a","x")  #we will pass only one argument
# print(a)

#5
# a={"a",70,"b",50,"a","d",90,"k","a",90}
# a.remove(70)
# print(a)

#Discard()
#1
# n={10,20,40,50,10,70}
# n.discard(20)
# print(n)

#2
# n={10,20,40,50,10,70}
# n.discard(100)
# print(n)

#3
# n={10,20,40,50,10,70}
# n.discard(20,50) #we can pass onle one argument
# print(n)

#4
# s={"a","c","b","z","a","q"}
# s.discard("a")
# print(s)

#5
# s={"a","c","b","z","a","q"}
# print(s.discard("a")) #It returns none

#Union
#1
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# print(n|s)

#2
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# print(n.union(s))

#3
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# a={10,50,20,90,225,76,31}
# print(n|s|a)

#4
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# a={10,50,20,90,225,76,31}
# print(n.union(s,a))

#5
# s={"a","c","b","z","a","q"}
# a={"a","z","d","l","f"}
# n={"a","c","b","t","v","s"}
# print(s|a|n)
# print(s.union(a,n))

#Intersection
# 1
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# print(n&s)

#2
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# print(n.intersection(s))

#3
# s={"apple","bat","ball","cricket","batsman"}
# n={"sachin","ms.dhoni","virat","ball","bat","cricket"}
# print(s & n)

#4
# s={"a","c","b","z","a","q"}
# a={"a","z","d","l","f"}
# n={"a","c","b","t","v","s"}
# print(s & a & n)

#5
# s={"apple","bat","ball","a","c","cricket","batsman"}
# n={"sachin","c","ms.dhoni","virat","ball","bat","cricket","a"}
# a={"a","c","b","t","v","s"}
# print(s.intersection(n,a))

#Difference
#1
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# print(n - s)

#2
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# a={10,50,20,90,225,76,31}
# print(n-s-a)

#3
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# a={10,50,20,90,225,76,31}
# print(n.difference(s,a))

#4
# s={"apple","bat","ball","a","c","cricket","batsman"}
# n={"sachin","c","ms.dhoni","virat","ball","bat","cricket","a"}
# a={"a","c","b","t","v","s"}
# print(s.difference(n,a))

#5
# s={"a","c","b","z","a","q"}
# a={"a","z","d","l","f"}
# n={"a","c","b","t","v","s"}
# print(s - a - n)
# print(s.difference(a,n))

#Symmetric difference
#1
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# print(n ^ s)

#2
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# a={10,50,20,90,225,76,31}
# print(n ^ s ^ a)

#3
# n={10,20,40,50,10,70,124}
# s={10,20,100,50,10,70,90}
# a={10,50,20,90,225,76,31}
# print(n.symmetric_difference(s,a))  #It takes only one argument

#4
# s={"a","c","b","z","a","q"}
# a={"a","z","d","l","f"}
# n={"a","c","b","t","v","s"}
# print(s ^ a ^ n)

#5
# a={"ajay","ram","krishna","eakesh","tarak"}
# s={"ajay","ram","krishna","ball","bat"}
# print(a ^ s)