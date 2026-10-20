choice = int(input("Enter your choice 1-4: "))
match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case 4:
        print("Fried Rice")
    case _:
        print("Invalid choice")


district = input("Enter the district name: ")
match district:
    case "Chennai":
        print("Filter coffee")
    case "Madurai":
        print("Jigarthanda")
    case "Tirunelveli":
        print("Halwa")
    case "Thoothukudi":
        print("Macaroons")
    case "Dindigul":
        print("Biryani")
    case "Coimbatore":
        print("Kothu Parotta")
    case _:
        print("District not added yet")
