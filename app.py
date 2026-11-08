class Ticket: #base class for all tickets
    _ticket_id_count = 1 #for incrementing ticket IDs
    def __init__(self, description, priority):
        self._ticket_id = Ticket._ticket_id_count
        self._description = description
        self._priority = priority
        self._assigned_to = None
        self._status = "Pending"

        Ticket._ticket_id_count += 1 #increments ID

    def show_details(self):
        return (
            f"Ticket ID: {self._ticket_id}\n"
            f"Description: {self._description}\n"
            f"Priority: {self._priority}\n"
            f"Assigned To: {self._assigned_to}\n"
            f"Status: {self._status}"
        )

    def update_status(self): #each ticket type to progress status differently
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
        self._fulfilment_status = "Pending Fulfilment"

    def update_status(self):
        if self._status == "Pending":
            self._status = "Awaiting Approval"

        elif self._status == "Awaiting Approval":
            self._status = "Approved"
        else:
            return "The ticket has already been approved"

    def show_details(self):
        return(
            super().show_details()
            + f"\nFulfilment Status:{self._fulfilment_status}\n"
        )

    def update_fulfilment_status(self):
        if self._status != "Approved": #will only allow updating once ticket status is approved
            print("The ticket must be approved to progress fulfillment")

        elif self._fulfilment_status == "Pending Fulfillment":
            self._fulfilment_status = "In Progress"

        elif self._fulfilment_status == "In Progress":
            self._fulfilment_status = "Complete"

        else:
            print("Fulfillment is already complete")

class Technician:
    def __init__(self, name, department):
        self._name = name
        self._department = department

    def get_technician_name(self):
        return self._name

    def view_technician_details(self):
        return(
            f"Technician: {self._name}\n"
            f"Department: {self._department}"
        )

incident = IncidentTicket( "Internet Outage", "High", "Network")
request = RequestTicket( "New Laptop Required", "High")
technician = Technician("John", "General Support")

tickets = [incident, request]

