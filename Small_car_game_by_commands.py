## A car game just using command 
command=""
started=False

while True:
    command=input("Enter your comand: ")
    if command=="start":
        if started:
            print("The car is already started...\n")
        else:
            started=True
            print("Car Started.....\n")

    elif command=="stop":
        if not started:
            print("The car is already stopped.\n")
        else:
            started=False
            print("Car Stopped.\n")
        

    elif command=="help":
        print("""
        start -> to start the car
        stop -> to stop the car
        exit -> to exit  
        """)

    elif command=="exit":
        print('Exiting..')
        break

    else:
        print("Sorry, invalid command")
        break
