command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            started = False
            print("Car is already stopped!")
        else:
            print("Car Stopped.")
    elif command == "help":
        print("""
start - to start the card
stop - to stop the card
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that!")
