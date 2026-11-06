tickets = []


def CreateTicket():
    print("--------------------------------")
    problem = input("Write a problem: ")
    stato = input("Quale lo stato di problema? Basso/Normale/Alto/Critico: ")
    persona = input("A chi assegnato il problema?: ")

    id = len(tickets) + 1

    tickets.append({
        "ID": id,
        "Problema": problem,
        "Assegnato": persona,
        "Stato problema": stato
    })


def ShowTickets():
    print("=================================================")
    print("-Tickets-")

    if len(tickets) == 0:
        print("No tickets found")

    for ticket in tickets:
        print(ticket["ID"],"|",ticket["Problema"],"|",ticket["Stato problema"],"|",ticket["Assegnato"])

    print("=================================================")


def CloseTicket():
    try:
        SearchID = int(input("Write an ID: "))
        found = False

        for ticket in tickets:

            if ticket["ID"] == SearchID:
                found = True

                for value in ticket.values():
                    print(value)

                print("1 to close | 0 to exit")

                ans = int(input("Answer: "))

                if ans == 1:
                    ticket["Stato problema"] = "Closed"
                    print("Ticket has been closed")

                break

        if not found:
            print("Nothing found")

    except:
        print("Close ticket error")


def SearchTicket():
    try:
        SearchID = int(input("Write an ID: "))
        found = False

        for ticket in tickets:

            if ticket["ID"] == SearchID:
                found = True

                for value in ticket.values():
                    print(value)

                break

        if not found:
            print("Ticket not found")

    except:
        print("Search Ticket error")


def strt():
    print("--------------------------------")
    print("1 - Create Ticket")
    print("2 - Show Tickets")
    print("3 - Close Ticket")
    print("4 - Search Ticket")
    print("5 - Exit")

    try:
        start = int(input("Choose: "))

        if start in [1, 2, 3, 4, 5]:
            return start

        print("You chose a wrong option!")

    except:
        print("Choose a number between 1,2,3,4 or 5")

    return strt()


options = {
    1: CreateTicket,
    2: ShowTickets,
    3: CloseTicket,
    4: SearchTicket
}


while True:

    start = strt()

    if start == 5:
        print("Bye!")
        break

    options[start]()