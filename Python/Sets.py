# Creat a eampty set
s = set()
# Add element to set
s.add(1)
s.add(2)
s.add(3)
s.add (4)
s.add(5)
print (s)
s.add(5)# here it will not be added again because set 
#contains only unique value//
print (s)
# for removeing values from set use "remove function"
s.remove(3)
print(s)
# python gives us builtin fun called "len()" for 
#finding length of String ,List ,Set
print(f"The set has {len(s)} elements")



