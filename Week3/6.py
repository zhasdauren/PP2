class Building:
	pass

class House(Building):
  height = 3
  length = 10
  width = 5
  
  def area(self):
  	return self.length * self.width
    
class JerUi(House):
 color = 'White'
 garden = [1,2]
 numOfFloors = 1
  

print(House)

h1 = House()
print(h1)
print(h1.area())
h1.width = 2
print(h1.area())

h2 = House()
print(h2.area())

j1 = JerUi()
print(j1.area())
print(j1.color)
print(j1.garden)