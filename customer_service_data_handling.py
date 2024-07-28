#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

class TicketSystem:
    def __init__(self):
        self.service_tickets = {
            "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
            "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
        }
        self.ticket_counter = len(self.service_tickets)

    def open_ticket(self, customer, issue):
        self.ticket_counter += 1
        ticket_id = f"Ticket{self.ticket_counter:03}"
        self.service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer}.")

    def update_ticket_status(self, ticket_id, status):
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = status
            print(f"Ticket {ticket_id} status updated to {status}.")
        else:
            print(f"Ticket {ticket_id} not found.")

    def display_tickets(self, status=None):
        for ticket_id, details in self.service_tickets.items():
            if status is None or details["Status"] == status:
                print(f"{ticket_id}: Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

# Example usage
ticket_system = TicketSystem()

# Open a new ticket
ticket_system.open_ticket("Charlie", "Network issue")

# Update the status of an existing ticket
ticket_system.update_ticket_status("Ticket001", "closed")

# Display all tickets
print("\nAll Tickets:")
ticket_system.display_tickets()
1
# Display only open tickets
print("\nOpen Tickets:")
ticket_system.display_tickets("open")
