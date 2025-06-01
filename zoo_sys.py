from datetime import datetime

class Animal:
    all_animals = {}

    def __init__(self, species, name, age, feeding_schedule):
        self.species = species
        self.name = name
        self.age = age
        self.feeding_history = []   # list of strings
        self.health_records = []    # list of strings
        self.health_status = "Healthy"
        self.feeding_schedule = feeding_schedule

        Animal.all_animals[name.lower()] = self

    def __str__(self):
        return f"{self.name}"

    def feed(self, food):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{now}: Fed with {food}"
        self.feeding_history.append(log_entry)
        print(f"{self.name} has been fed.")

    def check_health(self):
        print(f"{self.name}'s current health: {self.health_status}")
        self.show_health_records()


    def update_health(self, health_info):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.health_status = health_info
        log_entry = f"{now}: Health updated to {health_info}"
        self.health_records.append(log_entry)

    def show_feeding_history(self):
        print(f"\nFeeding history of {self.name}:")
        for record in self.feeding_history:
            print(record)

    def show_health_records(self):
        print(f"\nHealth records of {self.name}:")
        for record in self.health_records:
            print(record)

    def manage_animal_info(self, species='', name='', age=''):
        Animal.all_animals[name.lower()] = self
        del Animal.all_animals[self.name]
        if species:
            self.species = species
        if name:
            self.name = name
        if age:
            self.age = age
        if species or name or age:
            print(f'Animal info updated: species - {self.species} | name - {self.name} | age - {self.age}')


class Enclosure:
    all_enclosures = {}

    def __init__(self, enclosure_id, name, enclosure_type):
        self.enclosure_id = enclosure_id
        self.name = name
        self.enclosure_type = enclosure_type
        self.assigned_animal = None
        self.cleanliness_status = "Clean"

        Enclosure.all_enclosures[name.lower()] = self

    def __str__(self):
        return f"""Enclosure number: {self.enclosure_id} 
                | Name : {self.name} 
                | Type: {self.enclosure_type} 
                | Animal: {self.assigned_animal}
                | Status: {self.cleanliness_status}"""

    def assign_animal(self, animal):
        self.assigned_animal = animal
        print(f"{animal.name} assigned to {self.name}.")

    def clean(self):
        self.cleanliness_status = "Clean"
        print(f"{self.name} has been cleaned.")

    def change_status(self, new_status):
        self.cleanliness_status = new_status
        print(f"{self.name} status changed to {new_status}.")


class FeedingSchedule:
    def __init__(self, food, time_to_feed):
        self.food = food
        self.time_to_feed = time_to_feed

    def check_schedule(self):
        return f"Schedule: \n{self.time_to_feed} - {self.food}"
    
    def update_schedule(self, food, time_to_feed):
        self.food = food
        self.time_to_feed = time_to_feed



class Keeper:
    def __init__(self, name):
        self.name = name



class Vet:
    def __init__(self, name):
        self.name = name


class Manager:
    def __init__(self, name):
        self.name = name



# Sample data
keeper = Keeper("Nick")
vet = Vet("Tom")
manager = Manager("Jerry")


Animal("Lion", "Leo", 5, FeedingSchedule("meet", "08:00")),
Animal("Elephant", "Ella", 10, FeedingSchedule("Bananas", "09:00")),
Animal("Giraffe", "Gigi", 7, FeedingSchedule("Leaves", "10:00")),
Animal("Zebra", "Zack", 4, FeedingSchedule("Grass", "11:00"))



Enclosure(1, "Savannah Habitat", "Open Field"),
Enclosure(2, "Jungle Zone", "Dense Forest"),
Enclosure(3, "Elephant Plains", "Mud Zone"),
Enclosure(4, "Giraffe Heights", "Tall Trees"),
Enclosure(5, "Zebra Run", "Grassland"),
Enclosure(6, "Health Check Station", "Medical")



def manager_animal_menu():
    all_animals = [name.lower() for name in Animal.all_animals.keys()]

    print("What do you want to do?")
    print("1. Add new animal")
    print("2. Show all the animals")

    choice = input("Write a number: ")

    if choice == "1":
        species = input("Write species: ").lower()
        while True:
            name = input("Write name: ").lower()
            if name in all_animals:
                print("Such a name is take already. Try again")
            else:
                break
        age = input("Write age: ")
        food = input("Write food: ")
        time_to_feed = input("Write time to feed: ")
        Animal(species, name, age, FeedingSchedule(food, time_to_feed))

        print("Animal was successfuly added")
        manager_animal_menu()

    elif choice == "2":
        
        print(f"At this point in the zoo are these animals: {", ".join(all_animals)}")
        name = input("Choose the animal or write 'exit':").lower()
        if name == "exit":
            manager_animal_menu()
        else:
            if name in all_animals:
                print("What do you want to do?")
                print("1. Edit animal")
                print("2. Delete animal")
                print("3. Edit feeding schedule")

                choice = input("Write your choice: ")
                if choice == "1":
                    animal = Animal.all_animals[name]
                    print("Current animal info: ")
                    print(f"Species: {animal.species}")
                    print(f"Name: {animal.name}")
                    print(f"Age: {animal.age}")

                    new_species = input("Write new species: ")
                    new_name = input("Write new name: ")
                    new_age = input("Write new age: ")

                    animal.manage_animal_info(new_species, new_name, new_age)


                elif choice == "2":
                    animal = Animal.all_animals[name]
                    del animal
                    del Animal.all_animals[name]
                    print(f"Animal {name} was successfuly deleted")

                    
            elif choice == "3":
                food = input("Write new food: ")
                time_to_feed = input("Write new time to feed: ")
                animal.feeding_schedule.update_schedule(food, time_to_feed)

            else:
                print("No such animal")

            manager_animal_menu()


def keeper_animal_menu():
    all_animals = [name.lower() for name in Animal.all_animals.keys()]

    print(f"At this point in the zoo are these animals: {", ".join(all_animals)}")
    name = input("Choose the animal or write 'exit':").lower()
    if name == "exit":
        return
    else:
        if name in all_animals:
            animal = Animal.all_animals[name]
            print("Current animal info: ")
            print(f"Species: {animal.species}")
            print(f"Name: {animal.name}")
            print(f"Age: {animal.age}")


            print("\nWhat do you want to do?")
            print("1. Check schedule")
            print("2. Feed animal")
            print("3. Exit")

            choice = input("Write your choice: ")
            if choice == "1":
                print(animal.feeding_schedule.check_schedule())
            
            elif choice == "2":
                food = input("Write what food you are going to give to the animal: ")
                animal.feed(food)
            elif choice == "3": 
                keeper_animal_menu()
            else:
                print("Invalid choice")



def keeper_menu():
    while True:
        print("\n--- Keeper Menu ---")
        print("1. Animals")
        print("2. Enclosures")
        print("3. Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            keeper_animal_menu()


        elif choice == "2":

            all_enclosures = [name.lower() for name in Enclosure.all_enclosures.keys()]
            print(f"Choose one of enclosure names: {", ".join(all_enclosures)}")
            name = input("Write the name: ").lower()
            if name in all_enclosures:
                enclosure = Enclosure.all_enclosures[name]
                print(enclosure)
                choice = input("\nWant to clean it? (Yes/No)").lower()
                if choice == "yes":
                    enclosure.clean()

            



        elif choice == "3":
            break
        else:
            print("Invalid choice.")

def vet_menu():
    while True:
        all_animals = [name.lower() for name in Animal.all_animals.keys()]
        print("\n--- Veterinarian Menu ---")
        print(f"Choose one animal from the list: {", ".join(all_animals)}")
        name = input("Write the name: ").lower()
        if name in all_animals:
                animal = Animal.all_animals[name]
                print(f"Animal info:")
                print(f"Species: {animal.species}")
                print(f"Name: {animal.name}")
                print(f"Age: {animal.age}")

                animal.check_health()

                choice = input("What to change health status? (Yes/No): ").lower()

                if choice == "yes":
                    new_health = input("Write new health status: ")
                    animal.update_health(new_health)
                    print("Successfuly updated.")
                
        
        else:
            print("No such animal name")


def manager_menu():
    while True:
        print("\n--- Manager Menu ---")
        print("1. Animals")
        print("2. Enclosures")
        print("3. Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            manager_animal_menu()

        elif choice == "2":
            # =======================================write enclosures===========================
            all_enclosures = [name.lower() for name in Enclosure.all_enclosures.keys()]
            print(f"Choose one of enclosure names: {", ".join(all_enclosures)}")
            name = input("Write the name: ").lower()
            if name in all_enclosures:
                enclosure = Enclosure.all_enclosures[name]
                print(enclosure)

                print("\nWhat do you want to do?")
                print("1. Change cleanliness status")
                print("2. Assign animal")
                response = input("Write the number: ")

                if response == "1":
                    status = input("Write new status: ")
                    enclosure.change_status(status)
                elif response == "2":
                    all_animals = [name.lower() for name in Animal.all_animals.keys()]
                    animal_name = input(f"Write the name of the animal from the list: \n*{"\n*".join(all_animals)} \n").lower()
                    

                    if animal_name in all_animals:
                        animal = Animal.all_animals[animal_name]
                        enclosure.assign_animal(animal)
                    else:
                        print("No such animal")
                
                    
                else: 
                    print("Invalid answer")
            pass
        elif choice == "3":
            break
        else: 
            print("Invalid choice")
        

        
      




print("Welcome to the Zoo Management System!")
username = input("Enter your name: ").strip()

if username.lower() == "nick":
    keeper_menu()
elif username.lower() == "tom":
    vet_menu()
elif username.lower() == "jerry":
    manager_menu()
else:
    print("Access denied. Unknown user.")



