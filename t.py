options = {
    1: CreateTicket(),
    2: ShowTickets(),
    3: CloseTicket(),
    4: SearchTicket(),
    5: "Exit"
}


while True:
    for option in options:
        if option == 5:
            print("hiiiii")
        options[option]