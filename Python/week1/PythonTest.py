print("        Grocery Billing System                 ")
print("-----------------------------------------------------------------")
#all data 
grocery_store={"Potato":35,"Onion":40,"Tomato":30,"Bhindi":45,"Banana":70,"Apple":50,"Rice":40,"Wheat":40,"Dal":85,"Chana Dal":70,"Rajma":100,"Haldi powder":35,"Mirch power":45,"Garam masala":50,"Salt":25,"Sugar":40,"Mustard Oil":120,"Sunflower Oil":110,"Ghee":250,"Tea":100,"Lifebuoy soap":40,"Surf Excel":120,"Shampoo":100,"Colgate":60,"Detergent Bar":20}
print("------------------------------------------------------------------")
print("We have this itme : ")
print("-----------------------------------------------------------------")
print("Fruits&Vegetables : ")
print("-----------------------------------------------------------------")
print("Potato: ₹35 => 1kg")
print("Onion:  ₹40 =>  1kg")
print("Tomato: ₹30 => 1kg")
print("Bhindi: ₹45 => 1kg")
print("Banana: ₹70 => 1Dozen")
print("Apple: ₹50 => 1kg")
print("-----------------------------------------------------------------")
print("Grains&Pulses :")
print("-----------------------------------------------------------------")
print("Rice: ₹40 => 1kg")
print("Wheat: ₹40 => 1kg")
print("Dal: ₹85 => 1kg")
print("Chana Dal: ₹70 => 1kg")
print("Rajma: ₹100 => 1kg")
print("-----------------------------------------------------------------")
print("Spices&Condiments:")
print("-----------------------------------------------------------------")
print("Haldi power: ₹35 => 100g")
print("Mirch power: ₹45 => 100g")
print("Garam masala: ₹50=> 100g")
print("Salt: ₹25 => 1kg")
print("Sugar: ₹40=> 1kg")
print("-----------------------------------------------------------------")
print("Oils&Essentials:")
print("-----------------------------------------------------------------")
print("Mustard Oil: ₹120 => 1litre")
print("Sunflower Oil: ₹110=> 1litre")
print("Ghee: ₹250 => 500g")
print("Tea: ₹100 => 250g")
print("-----------------------------------------------------------------")
print("Household_Toiletries:")
print("-----------------------------------------------------------------")
print("Lifebuoy soap: ₹40 => 125g")
print("Surf Excel: ₹120 => 1kg")
print("Shampoo: ₹100 => 180ml")
print("Colgate: ₹60 => 100g")
print("Detergent Bar: ₹20 => 1bar")
#Logic process
l=[ ]
cal=0
cal1=0
list=[ ]
list1=[ ]
lst=[ ]
lst1=[ ]
while True:
	i=input("Enter the item name : ")
	q=int(input("Enter the quantity : "))
	for f in grocery_store:
		if i==f:
			list.append(i)
			list1.append(q)
			cal=q*grocery_store[f]+cal
	m=input("More items (y/n) : ")
	if m=='y':
		print("Okey ! Enter more items")
		i1=input("Enter the item name : ")
		q1=int(input("Enter the quantity : "))
		m=input("More items (y/n) : ")
		for fru in grocery_store:
			if i1==fru:
				lst.append(i1)
				lst1.append(q1)
				cal1=q1*grocery_store[fru]+cal1
	if m=='n':
		break
#Apply tax or discount or sum 
l.append(cal)
l.append(cal1)
totle=sum(l)
#totle sum
totle1=totle
#GST
gst=5*totle1
tax=gst/100
cost=totle1+tax
#discount
discount=20*cost
dis=discount/100
final=cost-dis
#Display System.
dict1 = dict(zip(list, list1))
dict2=dict(zip(lst,lst1))
dict1.update(dict2)
print("-----------------------------------------------------------------")
print("Display full bill :")
print("-----------------------------------------------------------------")
print("Items, Quantity ")
print("-----------------------------------------------------------------")
for k in dict1:
	print(k,':',dict1[k])
print("-----------------------------------------------------------------")
print("Sub Total : ",totle1)
print("------------------------------------------------------------------")
print("GST 5% :",cost)
print("-----------------------------------------------------------------")
print("Discount 20% :",final)
print("------------------------------------------------------------------")
print("G.TOTAL :- ",final)