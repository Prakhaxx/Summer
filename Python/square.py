from fun import square
# for importing function from another file 
# Do "from file name import name of function"
for i in range (10):
  print(f"The square of {i} is {square(i)}")
#or we can do 
# import file name but then 
# we have to do some modification in print line like;
#  print(f"The square of {i} is {file name.square(i)}")  