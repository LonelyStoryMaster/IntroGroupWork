auto_services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}

print("Davy's auto shop services")
for service in auto_services:
    print("%s -- $%d" % (service, auto_services[service]))

#TODO Gather service inputs
selections["Service 1"] = input("\nSelect first service:\n")
selections["Service 2"] = input("Select second service:\n")

#TODO Check if inputs are no service


#TODO Print invoice
