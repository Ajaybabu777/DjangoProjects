#Type casting in tuple
#1
# tup=(1,2,3,4,5,99,55)
# print(type(tup))

#2
# tup=(1,20,50,58,92,23)
# t1=(1,20,53,87,12,37)
# print(id(tup))
# print(id(t1))

#3
# words=["ram","ajay","babu","prabhas"]
# s=tuple(words)
# print(s)
# print(type(s))

#4
# num=[55,67,"ram",75,"babu",54,76]
# print(type(num))
# s=tuple(num)
# print(type(s))

#5
# num=10,60,70,100,66,94
# print(type(num))

#6
# tup=(1,20,50,58,92,23)
# t1=(1,20,50,58,92,23)
# print(id(tup))
# print(id(t1))

#Slicing by using for loop
#1
# tup=tuple(range(1,20))
# indexing=tup[o:10:1]
# print(tup)

#2
# tup=tuple(range(1,20))
# indexing=tup[-1:11:-2]
# print(indexing)

#3
# tup=tuple(range(1,20))
# indexing=tup[-1:]
# print(indexing)

#4
# tup=tuple(range(1,20))
# indexing=tup[-1]
# print(indexing)

#5
# tup=tuple(range(1,20))
# indexing=tup[:-1]
# print(indexing)

#Adding elements to tuple
#1
# tup=(1,20,50,58,92,23)
# li=list(tup)
# li[3]=77
# s=tuple(li)
# print(s)

#2
# tup=(1,20,50,58,92,23)
# t1=(87,34,56,82)
# add=tup+t1
# print(add)

#3
# tup=("apple",65,32,"banana","mango",91)
# t1=(45,39,"ram",27,49,"ajay")
# add=tup+t1
# print(add)

#4
# tup=(1,20,"bahubhali",50,58,92,"KGF",23,"BRO")
# li=list(tup)
# li[3]="power star"
# s=tuple(li)
# print(s)

#5
# tup="apple",65,32,"banana","mango",91
# t1=45,39,"ram",27,49,"ajay"
# add=tup+t1
# print(add)

#len function in tuple
#1
# tup=(1,20,50,58,92,23)
# print(len(tup))

#2
# tup=(1,20,50,58,92,23)
# t1=(87,34,56,82)
# leng=len(tup)-len(t1)
# print(leng)

#3
# tup=(1,20,50,58,92,23)
# t1=(87,34,56,82)
# leng=len(tup)+len(t1)
# print(leng)

#4
# tup="apple",65,32,"banana","mango",91
# t1=45,39,"ram",27,49,"ajay"
# leng=len(tup)+len(t1)
# print(leng)

#5
# tup="apple",65,32,"banana","mango",91
# t1=45,39,"ram",27,49,"ajay"
# leng=len(tup)-len(t1)
# print(leng)

#Count method in tuple
#1
# tup=(1,20,50,58,92,23,20)
# print(tup.count(20))

#2
# tup="apple",65,32,"banana","mango",91
# t1=45,39,"ram",27,49,"ajay","apple"
# add=(tup)+(t1)
# print(add.count("apple"))

#3
# tup=("apple",65,32,"banana","mango",91,45,65)
# t1=(45,39,"ram",27,49,"ajay",45)
# print(tup.count(65),t1.count(45))

#4
# tup=("apple",65,32,"banana","mango",91,45,65)
# t1=(45,39,"ram",27,49,"ajay",45,"ram")
# print(tup.count(65),t1.count(45),t1.count("ram"))

#5
# tup=("apple",65,32,"banana","mango",91,45,65)
# t1=(45,39,"ram",27,49,"ajay",45,"ram")
# print(tup.count(65)+t1.count(45)-t1.count("ram"))

#Index method in tuple
#1
# tup=(1,20,50,58,92,23,20)
# print(tup.index(20))

#2
# tup="apple",65,32,"banana","mango",91
# t1=45,39,"ram",27,49,"ajay","apple"
# add=(tup)+(t1)
# print(add.index("apple"))

#3
# tup=("apple",65,32,"banana","mango",91,45,65)
# t1=(45,39,"ram",27,49,"ajay",45)
# print(tup.index(65),t1.index(45))

#4
# tup=("apple",65,32,"banana","mango",91,45,65)
# t1=(45,39,"ram",27,49,"ajay",45,"ram")
# print(tup.index(65),t1.index(45),t1.index("ram"))

5
# tup=("apple",65,32,"banana","mango",91,45,65)
# t1=(45,39,"ram",27,49,"ajay",45,"ram")
# print(tup.index(65)+t1.index(45)-t1.index("ram"))

#sorted and reverse sorted in the tupel
#1
# tup=(8,7,3,9,10,3,1,12,0)
# print(sorted(tup))

#2
# tup=("a","x","c","g","b","q")
# print(sorted(tup))

#3
# tup=("apple",65,32,"banana","mango",91,45,65)
# print(sorted(tup)) # "<" not supported between instances of int and str

#4
# tup=("prabhas","zebra","apple","cat","ram charan")
# print(sorted(tup))

#5
# tup=(8,7,3,9,10,3,1,12,0)
# t1=tuple(sorted(tup,reverse=True))
# print(t1)

#6
# tup=("a","x","c","g","b","q")
# t1=tuple(sorted(tup,reverse=True))
# print(t1)

#7
# tup=tuple(range(1,20))
# t1=tuple(sorted (tup,reverse=True))
# print(t1)

#8
# tup=("prabhas","zebra","apple","cat","ram charan")
# t1=tuple(sorted (tup,reverse=True))
# print(t1)

#9
# tup=("apple",65,32,"banana","mango",91,45,65)
# t1=tuple(sorted (tup,reverse=True))
# print(t1)   # "<" not supported between instances of int and str

#10
tup="apple",65,32,"banana","mango",91
t1=45,39,"ram",27,49,"ajay","apple"
add=(tup)+(t1)
t2=tuple(sorted (add,reverse=True))















