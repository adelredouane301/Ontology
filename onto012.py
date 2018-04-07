import owlready2 
from owlready2 import * 

# owlready2.JAVA_EXE = "\\path\\to\\java.exe" 

owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jre1.8.0_111\\bin\\java.exe"
owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jdk1.7.0_55\\bin\\java.exe"

onto=onto_path.append("C:\\Users\\faouzi\\Documents\\ontology\\")
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
## onto = get_ontology("file://C:/Users/Classroom/Desktop/paython_adel/pizza_onto1.owl")

onto.load()
onto.save()

tab="    "
CL={'Store','Book','Title','Author','ISBN','Bicycle'}
for c in CL:
    classString = "class " + c + "(" + "onto.Pizza" + ")"  + ":"
    classString = classString + tab + "equivalent_to" + " = [" + "onto.Pizza" + " ]"
    print(classString)
    exec(classString)

class NonVegetarianPizza(onto.Pizza):
    equivalent_to = [
        onto.Pizza
        & ( onto.has_topping.some(onto.MeatTopping)
        | onto.has_topping.some(onto.FishTopping)
        ) ]
    def eat(self): print("Beurk! I'm vegetarian!")
	
onto.Pizza
test_pizza = onto.Pizza("test_pizza_owl_identifier")
test_pizza1 = onto.Pizza("test_pizza1_owl_identifier")
test_pizza2 = onto.Pizza("test_pizza2_owl_identifier")

test_pizza1.has_topping = [ onto.CheeseTopping(),
    onto.TomatoTopping(),
    onto.MeatTopping() ]
	
onto.save()
test_pizza1.__class__
sync_reasoner()
test_pizza1.__class__
test_pizza1.eat()