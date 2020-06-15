print("Hello World")

degisken = 11
print(degisken)
print(type(degisken))

print("--------------------------------")

degisken2 = "Kodluyoruz"
print(degisken2)
print(type(degisken2))


degisken2 = 50
print(degisken2)
print(type(degisken2))



print("--------------------------------")

number1 = 15
number2 = 20
total = number1 + number2
print(total)
print(type(total))

total = 25+38
print(total)
print(type(total))

number3 = 15/3
print(number3)
print(type(number3))


print(type(9//4))
print(18%4)
print("Serkan Dağlıoğlu")

print("--------------------------------")


str1 = "Kodluyoruz python&flask bootcamp"
print("str1 uzunluğu = ",len(str1))
print("& index = ", str1.index("&"))
str2 = "Test2"
str3 = "Test3"
strjoin1 = ",".join([str1,str2,str3])
print(strjoin1)
strplus1 = str1+","+str2+","+str3
print(strplus1)
dizistrsplit1 = strplus1.split(",")
print(dizistrsplit1)


print(str1.replace("&","|"))
print(str1.replace("python&flask","test"))




print("--------------------------------")



print("TUPLE")
tuple1 = ("item1","item2","item3")
print(tuple1)
print(type(tuple1))
tuple2 = ("test",10,15)
print(tuple1[1])
print(len(tuple1))
tuple3 = (1991, 2.37, ("TR", "TBMM"))
# tuple3[1] = 2 # hata verir, tuple da eleman değiştirilemez

tuple31 = tuple3[2]
print(tuple31)
print(type(tuple31))
print(tuple31[1])
print(tuple3[2][1])



print("LIST")

list1 = ["item1","item2","item3"]
print(list1)
print(type(list1))
print(list1[1]) # item2
print(list1[-1]) # item3
list1.append("item4")
list1.append("item5")
print(list1)
print(list1[-1]) # item5

# del list1[3] # diziden bir eleman silme
list1.remove(list1[3]) # diziden bir elaman silme
print(list1)
print("#")

# print(dir(list1)) # değişken içindeki özellikleri metodları vs listeler


list2 = ["item1", 2,34.5, [1,2]]
print(list2)
print(list2[3][0])

print("#")
list3 = ["Itirazım", "Var", "Ölümlü", "Dünya"]
splitList3 = list3[:2]
print(splitList3)
splitList4 = list3[1:3]
#splitList4 = list3[1:-1]
#splitList4 = list3[-4:3]
print(splitList4)

print("#")

extendlist1 = [6,8,9]
extendlist2 = extendlist1 + [3,7] # [6,8,9,3,7]
print(extendlist2)

extendlist2.pop() # [6,8,9,3]
print(extendlist2)

extendlist2.reverse()
print(extendlist2)

extendlist2.sort()
print(extendlist2)

#print(extendlist1)
#extendlist1.extend([3,7])
#print(extendlist1)

list3 = [1,2,3,4,5,6]
list3.insert(2,15)
print(list3)


# print(dir(list3)) # list3 içindeki metodları listeler



print("#")

#sozluk = dict()
sozluk = {
	"mektup" : "Bir şey haber vermek",
	"makine" : "Herhangi bir enerji türünü başka bir enerjiye dönüştürmek",
	"ilaç" 	 : "Çare, önlem.",
	"yasa" 	 : "Kanun"
}
print(type(sozluk))
print(sozluk["makine"])
print(sozluk["yasa"])

print(sozluk.values())
print(sozluk.keys())
print(dir(sozluk))

sozluk2 = {
	"a" : "A",
	"b" : "B",
	"c" : "C",
}

sozluk.update(sozluk2)
print(sozluk)


sozluk["yasa"] = "herhangi bir anlam"
print(sozluk)

del sozluk["yasa"] # sozlukten eleman silme
print(sozluk)


#sozlukTanimlama2 = dict(a="A", b="B")
#print(sozlukTanimlama2)

sozlukTanimlama3 = dict()
sozlukTanimlama3["a"] = "A"
sozlukTanimlama3["b"] = "B"
print("sozlukTanimlama3 = ")
print(sozlukTanimlama3)


# yorum satırı

"""
coklu yorum satiri
coklu yorum satiri
coklu yorum satiri
coklu yorum satiri
"""

strUzun = """safasdf
asdfasdf
asdfasdf
asdfasdf
asdfasdf
"""



print("KOŞULLAR")

a = 33
b = 200

if b>a:
	print("b, a dan büyüktür")
elif a==b:
	print("a ve b birbirine eşittir")
elif a==b+1:
	print("a 201 sayısına eşittir")
else:
	print("else")



if b>a: print("oneline = b, a dan büyüktür")


c = 1
c = 100 if a>b else 500
# if a>b:
# 	c = 2
# else:
# 	c = 3
print(c)

#if b>a:
#	pass


# a = 33 , b = 200, c=500
# b = 600
if b>a and b<c:
	print("b, a'dan büyük c'den küçük" )
else:
	print("b>a and b<c koşulu sağlanmıyor" )


#b = 600
if b>a or b<c:
	print("b a'dan büyük veya c'den küçük" )


#nested if
print("nested if")
if b>a:
	if b>c:
		print("b, c'den küçüktür")
	print("b, a'dan büyüktür")





print("SET")
set1 = { "apple", "banana", "cherry" }
# set1 = set(("apple", "banana", "cherry")) # üstteki satır ile aynı işi yapar
print(set1)

appleSetIcindeVarmi = "apple" in set1
print(appleSetIcindeVarmi)

set1.add("orange")
print(set1)


set1.update(["orange","mango","grapes"])
print(set1)

print("set1 uzunluğu >> " , len(set1))

set1.remove("orange")
print(set1)

set1.discard("orangee") # eleman kümede olmadığı halde hata vermedi. remove ile aynı şeyi yapar
print(set1)

#del set1 # set1 i komple siler
#print(set1)


set2 = {"a", "b" , "c"}
set3 = {1, 2, 3}
setBirlesim1 = set2.union(set3)
print(setBirlesim1)
print(set2)


set2.update(set3)
print(set2)


print(set2,set3)
setDifference1 = set2.difference(set3)
print("setDifference1 = ")
print(setDifference1)



#setNoktaTest = {"a","b","c","d","e"}
#print(setNoktaTest[::-1])
#print(setNoktaTest[2:5:4])
# stringin x indexinden y indexine kadar z karakter atlayarak git
noktaTest = "kodluyoruz test1 test2 test3 test4"
print(noktaTest[:-1])
print(noktaTest[2::4])























