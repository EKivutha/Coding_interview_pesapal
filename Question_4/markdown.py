import markdown2
print ("Enter markdown path")
file = input()
markd = open(file, "r")
output = markdown2.markdown(markd)
print (output)