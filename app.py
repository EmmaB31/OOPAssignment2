class Ticket:
    def __init__(self, ticket_id, description, priority, assigned_to):
        self.ticket_id = ticket_id
        self.description = description
        self.priority = priority
        self.assigned_to = assigned_to
        self.status = "Pending"

    def show_details(self):
        return (
            f"Ticket ID: {self.ticket_id}\n"
            f"Ticket Type: {self.ticket_type}\n"
            f"Description: {self.description}\n"
            f"Priority: {self.priority}\n"
            f"Assigned To: {self.assigned_to}\n"
            f"Status: {self.status}"
        )

    def update_status(self):
        pass


class IncidentTicket(Ticket):
    def __init__(self, ticket_id, description, priority, assigned_to, urgent, affected):
        super().__init__(ticket_id, description, priority, assigned_to)
        self.ticket_type = "Incident"
        self.urgent = urgent
        self.affected = affected


    def update_status(self):
        if self.status == "Pending":
            self.status = "In Progress"
        elif self.status == "In Progress":
            self.status = "Resolved"
        else:
            return "Ticket Resolved"


class RequestTicket(Ticket):
    def __init__(self, ticket_id, description, priority, assigned_to, approved):
        super().__init__(ticket_id, description, priority, assigned_to)
        self.ticket_type = "Request"
        self.approved = approved
    def update_status(self):
        if self.status == "Pending":
            self.status = "Awaiting Approval"
        else:
            self.status = "Approved"



#ticket = Ticket(1, "Ticket 1", "High", "Person 1", "Active")

incident = IncidentTicket(2, "Internet Outage", "High", "User 2", True, "HR")
request = RequestTicket(1, "New Laptop Required", "High", "User 1", False)

tickets = [incident, request]

for ticket in tickets:
    print(ticket.show_details())
    ticket.update_status()
    print("_____")
    print(ticket.show_details())
    print("_____")
