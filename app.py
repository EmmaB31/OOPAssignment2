class TicketManager:
    def __init__(self):
        self._tickets = []

    def store_ticket(self, ticket):
        self._tickets.append(ticket)


class Ticket:
    _ticket_id_count = 1
    def __init__(self, description, priority):
        self._ticket_id = Ticket._ticket_id_count
        self._description = description
        self._priority = priority
        self._assigned_to = None
        self._status = "Pending"

        Ticket._ticket_id_count += 1

    def show_details(self):
        return (
            f"Ticket ID: {self._ticket_id}\n"
            f"Description: {self._description}\n"
            f"Priority: {self._priority}\n"
            f"Assigned To: {self._assigned_to}\n"
            f"Status: {self._status}"
        )

    def update_status(self):
        pass

    def update_priority(self, update_priority):
        valid_priorities = ["high", "medium", "low"]
        if update_priority in valid_priorities:
            self._priority = update_priority
        else:
            print("Invalid priority")

    def assign_technician(self, technician):
        if self._assigned_to is None:
            self._assigned_to = technician
            print(f"Technician {technician} has been assigned")
        else:
            print("Technician has already been assigned")

    def reassign_technician(self, new_technician):
        if self._assigned_to is not None and self._assigned_to != new_technician:
            self._assigned_to = new_technician
            print(f"Technician reassigned successfully to {new_technician}")
        else:
            print("Unable to reassign. This technician is already assigned or there is no assigned technician")


class IncidentTicket(Ticket):
    def __init__(self, description, priority, incident_type):
        super().__init__(description, priority)
        self._incident_type = incident_type
        self._urgency = "Standard"

    def update_status(self):
        if self._status == "Pending":
            self._status = "In Progress"
        elif self._status == "In Progress":
            self._status = "Resolved"
        else:
            return "Ticket Resolved"

    def update_urgency(self, new_urgency):
        valid_urgency = ["Immediate", "Urgent", "Standard", "Non-urgent"]
        if new_urgency in valid_urgency:
            self._urgency = new_urgency
            print(f"Urgency has been updated to {self._urgency}")
        else:
            print("Invalid urgency")
            
    def show_details(self):
        return(
            super().show_details()
        + f"\nUrgency: {self._urgency}"
        )

class RequestTicket(Ticket):
    def __init__(self, description, priority):
        super().__init__(description, priority)
        self._approved = False
        self._fulfilment_status = "Pending Fulfilment"

    def show_details(self):
        return(
            super().show_details()
            + f"\nFulfilment Status:{self._fulfilment_status}\n"
            + f"Approved: {self._approved}")

    def update_status(self):
        if self._status == "Pending":
            self._status = "Awaiting Approval"
        else:
            self._status = "Approved"
            self._approved = True

    def update_fulfilment_status(self):
        if self._status == "Approved" and self._fulfilment_status != "Complete":
            self._fulfilment_status = "In Progress"
        elif self._status == "Approved" and self._fulfilment_status == "In Progress":
            self._fulfilment_status = "Complete"
        elif self._status != "Approved":
            print("The ticket must be approved to progress fulfillment")
        else:
            print("Fulfillment is already complete")



class Technician:
    def __init__(self, name, department):
        self._name = name
        self._department = department

    def get_name(self):
        return self._name

    def view_technician_details(self):
        return(
            f"Technician: {self._name}\n"
            f"Department: {self._department}"
        )

test_tech = Technician("Emma", "General Support")
test_ticket = Ticket("Test general ticket", "Low")
test_ticket.assign_technician(test_tech.get_name())

print(test_tech.view_technician_details())


incident = IncidentTicket( "Internet Outage", "High", "Network")
request = RequestTicket( "New Laptop Required", "High")

tickets = [incident, request]

print(incident.show_details())
incident.update_priority("medium")
incident.update_urgency("Urgent")
print(incident.show_details())
print("_____")

request.update_status()
request.update_status()
request.update_fulfilment_status()
print(request.show_details())
print("_____")


for ticket in tickets:
    print(ticket.show_details())
    ticket.update_status()
    print("_____")
    print(ticket.show_details())
    print("_____")

print("Please make a choice:")
print("1. Report an Incident")
print("2. Make a Request")

while True:
    try:
        user_choice = int(input("Enter number: "))
        break
    except ValueError:
        print("Invalid Input")


if user_choice == 1:
    new_ticket = IncidentTicket( "Test", "High", "Network")
    print("Ticket Created!")
    print(new_ticket.show_details())

else:
    new_ticket = RequestTicket( "Request Test", "High")
    print("Ticket Created!")
    print(new_ticket.show_details())

print(tickets)


