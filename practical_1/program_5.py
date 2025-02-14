mass = int(input("Enter the Object's Mass(in Kilogram): "))
velocity = int(input("Enter the Velocity(in meters per second): "))

momentum = mass * velocity
kinetic = (0.5)*mass*velocity**2

print(f"The momentum is {momentum}, The kinetic is {kinetic}")
