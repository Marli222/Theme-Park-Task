class Attraction:
  def __init__(self,name, capacity,status):
    self._name = name
    self._capacity = capacity
    self._status = status
        
  def get_details(self):
    print(f"Attraction: {self._name}, Capacity: {self._capacity}, Status: {self._status}")
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
       if attraction.is_eligible(self._age,self._height) == True and attraction._status == True:
        print(f"{self._name} is riding {attraction._name}")
        self._ride.append(attraction._name)
       else:
          print(f"{self._name} is not eligible to ride {attraction._name}")
    def view_history(self):
       print(self._ride)

class Manager(Staff):
    def __init__(self,name):
      self._name = name
      self._role = "Manager"
      self._team = []
    def add_staff(self,staff):
      self._team.append(staff)
    def get_team_summary(self):
       for x in self._team:
        print(x._name,":",x._role)
            
Dragon = ThrillRide("Dragon Coaster",20,True,140)
Dragon.start()
Dragon.get_details()

Merry = FamilyRide("The Merry",30,True,4)
Merry.start()
Merry.get_details()

Armeen = Vistor("Armeen",17,150)
Armeen.ride(Merry)
Armeen.ride(Dragon)
Armeen.view_history()

Merry.close_attraction()
Dragon.close_attraction()

Armeen.ride(Merry)
Armeen.ride(Dragon)

Riley = Staff("Riley","Customer Service")
John = Staff("John","Customer Service")
Alice = Staff("Alice","Customer Service")

Lily = Manager("Lily")
Lily.add_staff(Riley)
Lily.add_staff(John)
Lily.add_staff(Alice)
Lily.get_team_summary()
