mycode = 'print("hello world")'
exec(mycode)
# to be readed fron T2
T2parent="Book"
T2child="Title"
T2min=0
T2Max=5
tab="    "
# properties types to be readed from DB
equiv="equivalent_to"
equiv2="equivalent_to"

classString = "class " + T2child + "( " + T2parent + "):"

classString = classString + tab + "equivalent_to" + " = [" + T2parent + " & "
print(classString)

# C:\Python36-32\python.exe -i "$(FULL_CURRENT_PATH)" C:\Users\faouzi\Documents\ontology\autogen.py