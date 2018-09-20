#Jared's Part
services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}

print("Davy's auto shop services")
for service in services:
    print("%s -- $%d" % (service, services[service]))

#Gathering Inputs
service1 = input("\nSelect first service:\n")
service2 = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")

#Zach's Part

#Checking inputs and printing invoice
if service1 == '-': 
    print('Service 1: No service')
    print('Service 2:', service2 + ', $' + str(services[service2]))
    print()
    print('Total: $'+ str(services[service2]))
elif service2 == '-':
    print('Service 1:', service1 + ', $' + str(services[service1]))
    print('Service 2: No service')
    print()
    print('Total: $'+ str(services[service1]))
else:
    print('Service 1:', service1 + ', $' + str(services[service1]))
    print('Service 2:', service2 + ', $' + str(services[service2]))
    print()
    print('Total: $'+ str(services[service1] + services[service2]))
