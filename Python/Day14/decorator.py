#example for decorater 
def status(a):
    def result():
        a()
        print("processing")
        print("Updated")
    return result
   
@status  
def greet():
    print("Welcome Back!")

greet()


#realtime example
def ride_Begin(nav):
    def route():
        nav()
        print("Go 500m and Turn left")
        print("Go straight for 1200m")
        print("Take left and travel for 300m ")
        print("Destination Reached")
    return wish

@ride_Begin
def nav():
    print("Your Destination is 2km far away")

route()

