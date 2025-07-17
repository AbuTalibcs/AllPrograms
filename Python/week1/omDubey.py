print("            Text Analyzer Tool                          ")
print("-----------------------------------------------------------------")
a=input("Enter the paragraph : ")
b=a.split( )
vow="aeiou"
f={ }
dis={ }
count=0
space=1
print("------------------------------------------------------------------")
for i in a:
	if i.isspace( ):
		space=space+1
print("Count total words : ",space)
print("-----------------------------------------------------------------")
for i in reversed(b):
	c=a.count(i)
	freq={ }
	freq.update({i:c})
	for t in freq:
		print(t,"=>",freq[t])
f.update({i:c})
dis.update({c:i})
d=max(dis)
if d > 1:
	print("most frequent word :",dis[d])
	print("--------------------------------------------------------------")
else:
	print("No frequent word ")
for i in vow:
	for l in b:
		if i in l:
			count=count+1
print("-------------------------------------------------------------------")
print("total vowel in the paragraph :",count)
print("------------------------------------------------------------------")
print("             Thankyou so much ; -)                ")