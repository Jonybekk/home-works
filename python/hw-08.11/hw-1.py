#Level 1
#1
names_b = ("Abu", "Dias", "Sherhan", "Ibrahim")
print(names_b)
names_s = ("AIman", "Sholpan", "Malika")
print(names_s)
#2
names_f = names_b + names_s
print(names_f)
#3
len_names_b = len(names_b)
print(f"I have {len_names_b} brothers")
len_names_s = len(names_s)
print(f"I have {len_names_s} sisters")
#4
names_bs = ("Sherhan", "Ibrahim", "Malika")
family_members = list(names_bs)
family_members.append("Arman")
family_members.append("Tolganai")
family_members = tuple(family_members)
print(family_members)

#Level 2
#1
family_members = ("Sherhan", "Ibrahim", "Malika", "Arman", "Tolganai")
brother1, brother2, sister1, father, mother = family_members
print(brother1)
print(brother2)
print(sister1)
print(father)
print(mother)
#2
fruits = ("apple", "avocado", "banana")
vagetables = ("onion", "chives", "peppers")
animal_products = ("cashmere", "kumis", "meat")
food_stuff_tp = (fruits + vagetables + animal_products)
print(food_stuff_tp)
#3
food_stuff_tp = ('apple', 'avocado', 'banana', 'onion', 'chives', 'peppers', 'cashmere', 'kumis', 'meat')
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)
#4
food_stuff_tp.pop(4)
print(food_stuff_tp)
#5
print(food_stuff_tp[3: -3])
#6
food_stuff_tp.clear()
print(food_stuff_tp)
#7
print("Estonia" in food_stuff_tp)
print("Iceland" in food_stuff_tp)
print("chives" in food_stuff_tp)