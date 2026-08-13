import json
import uuid

def create_escalation():
    ticket_id = f"SS-{uuid.uuid4().hex[:6].upper()}"

    data = {
        "ticket_id": ticket_id,
        "name": "Radhika",
        "issue": "Exam stress",
        "urgency": "High",
        "language": "English",
        "follow_up": "Email",
        "status": "OPEN"
    }

    with open("escalations.json", "r") as f:
        tickets = json.load(f)

    tickets.append(data)

    with open("escalations.json", "w") as f:
        json.dump(tickets, f, indent=2)

    print("Request Created")
    print("Reference ID:", ticket_id)

create_escalation()