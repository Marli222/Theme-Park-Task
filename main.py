class Attraction:
  def __init__(self,name, capacity,status):
    self._name = name
    self._capacity = capacity
    self._status = status
        
  def get_details(self):
    print(f"Attraction: {self._name}, Capacity: {self._capacity}")
  def start(self):
    if self._status == True:
        print("The attraction is starting.")
  def open_attraction(self):
     self._status = True
  def close_attraction(self):
     self._status = False
    
        
class ThrillRide(Attraction):
  def __init__(self,name,capacity,status,min_height):
    super().__init__(name,capacity,status)
    self._min_height = min_height
  def start(self):
    print(f"Thrill Ride {self._name} is now starting. Hold on tight!")
  def is_eligible(self,age,height):
      if height > self._min_height:
        return True
      else:
         return False
    
class FamilyRide(Attraction):
    def __init__(self,name,capacity,status,min):
        super().__init__(name,capacity,status)
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
        self._ride = []
    def ride(self,attraction):
       if attraction.is_eligible(self._age,self._height) == True:
        print(f"{self._name} is riding {attraction._name}")
        self._ride.append(attraction._name)
       else:
          print(f"{self._name} is not eligible to ride {attraction._name}")
    def view_history(self):
       print(self._ride)

class Manager(Staff):
    def __init__(self,name,role,team):
      super.__init__(name,"Manager")
      self._team = []
    def add_staff(self,staff):
      self._team.append(staff._name)
    def get_team_summary(self):
       print(self._team)
            
Drag = ThrillRide("Dragon Coaster",20,140,True)
Merry = FamilyRide("Merry-Go-Round",30,4,False)
Armeen = Vistor("Armeen",17,155)
Armeen.ride(Drag)
Armeen.ride(Merry)
Drag.start()
Merry.start()
visitor = Vistor("Alice", 10, 130)
coaster = ThrillRide("Dragon Coaster",20,140,True)

print(coaster.start())  # Output: "Thrill Ride Dragon Coaster is now starting. Hold on tight!"
visitor.ride(coaster)  # Output: "Alice is not eligible for Dragon Coaster."

carousel = FamilyRide("Merry-Go-Round",30,4,True)
visitor.ride(carousel)  # Output: "Alice is enjoying the Merry-Go-Round!"
visitor.view_history()  # Output: ["Merry-Go-Round"]
            
Drag = ThrillRide("Dragon Coaster",20,140)
Merry = FamilyRide("Merry-Go-Round",30,4)
Armeen = Vistor("Armeen",17,155)
Armeen.ride(Drag)
Armeen.ride(Merry)
