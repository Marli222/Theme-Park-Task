class Attraction:
  def __init__(self,name, capacity):
    self._name = name
    self._capacity = capacity
        
  def get_details(self):
    print(f"Attraction: {self._name}, Capacity: {self._capacity}")
  def start():
    print("The attraction is starting.")
        
class ThrillRide(Attraction):
  def __init__(self,name,capacity,min_height):
    super().__init__(name,capacity)
    self._min_height = min_height
  def start(self):
    print(f"Thrill Ride {self._name} is now starting. Hold on tight!")
  def is_eligible(self,age,height):
 	  if height > self._min_height:
 	    return True
 	  else:
 	    return False
    
class FamilyRide(Attraction):
    def __init__(self,name,capacity,min):
        super().__init__(name,capacity)
        self._min_age = min
    def start(self):
        print(f"Family Ride {self._name} is now starting. Enjoy the fun!")
    def is_eligible(self,age,height):
        if age > self._min_age:
         return True
        else:
         return False

class Staff:
    def __init__(self,name,role):
        self._name = name
        self._role = role
    def work(self):
     print(f"Staff {self._name} is performing their role: {self._role}.")

class Vistor:
    def __init__(self,name, age, height):
        self._name = name
        self._age = age
        self._height = height
    def ride(self,attraction):
    	if attraction.is_eligible(self._age,self._height) == True:
    	  print(f"{self._name} is riding {attraction._name}")
    	else:
    	  print(f"{self._name} is not eligible to ride {attraction._name}")
            
Drag = ThrillRide("Dragon Coaster",20,140)
Merry = FamilyRide("Merry-Go-Round",30,4)
Armeen = Vistor("Armeen",17,155)
Armeen.ride(Drag)
Armeen.ride(Merry)
