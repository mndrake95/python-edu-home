utensils = {"fork","spoon","knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)
# print(utensils.intersection(dishes))

utensils.add("tea spoon")
utensils.discard("tea spoon")
if "tea spoon" in utensils:
    utensils.add("cup")

for x in utensils:
    print(x)

list1 = [1,2,3,1,2,3]
print(list1)
list1set = {1,2,3,1,2,3}
print(list1set)