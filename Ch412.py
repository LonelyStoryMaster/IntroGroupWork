auto_services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}

print("Davy's auto shop services")
for service in auto_services:
    print("%s -- $%d" % (service, auto_services[service]))
