cities={
    "Cairo":{"population:":"10 million","distance:":"0 km"},
    "Alexandria":{"population:":"6 million","distance:":"219 km"},
    "Faiyum":{"population:":"3.8 million","distance:":"99.6 km"},
    "Damietta":{"population:":"0.34 million","distance:":"237 km"},
    "Asyut":{"population:":"0.39 million","distance:":"369 km"},
    "Rasheed":{"population:":"0.058 million","distance:":"168.5 km"},
    "Arish":{"population:":"0.16 million","distance:":"316 km"},
    "Aswan":{"population:":"1.568 million","distance:":"832 km"},
    "Beni suef":{"population:":"0.233 million","distance:":"150 km"},
    "Giza":{"population:":"8.8 million","distance:":"5.7 km"}
    }

def listing():
    for key,value in cities.items():
        print(key)
        for x,y in value.items():
            print(x,y)

def add():
    num=int(input("Enter the number of cities you want to add\n"))
    for i in range(num):
        city=input("Enter the name of the city\n")
        population=input("Enter the population of the city\n")
        print("Enter the distance between ",city," and Cairo\n")
        distance=input()
        cities[city]={}
        cities[city]["population"]=population
        cities[city]["distance:"]=distance

choice=int(input("Choose a number:\n1: View all cities\n2: Add a new city\n3: Close\n"))
while choice>=1 and choice<3:
    if choice ==1:
        listing()
    elif choice==2:
        add()
    else:
        choice=int(input("Choose a number:\n 1: View all cities\n2: Add a new city\n"))
    choice=int(input("Choose a number:\n1: View all cities\n2: Add a new city\n3: Close\n"))
    