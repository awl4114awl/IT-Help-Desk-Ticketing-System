# database.py

from pymongo import MongoClient
from bson.objectid import ObjectId

class Database:
    def __init__(self, uri="mongodb+srv://awl4114awl:fF9glIQpu1xDQcT6@ithelpdeskticketingsyst.mo9od.mongodb.net/?retryWrites=true&w=majority&appName=ITHelpDeskTicketingSystem", db_name="ITHelpDesk"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.tickets = self.db.tickets

    def create_ticket(self, title, description):
        ticket = {
            "title": title,
            "description": description,
            "status": "Open",
            "created_at": None,  # You can add timestamps if needed
            "updated_at": None
        }
        result = self.tickets.insert_one(ticket)
        return str(result.inserted_id)

    def get_all_tickets(self):
        return list(self.tickets.find())

    def get_ticket(self, ticket_id):
        return self.tickets.find_one({"_id": ObjectId(ticket_id)})

    def update_ticket(self, ticket_id, update_data):
        result = self.tickets.update_one(
            {"_id": ObjectId(ticket_id)},
            {"$set": update_data}
        )
        return result.modified_count

    def delete_ticket(self, ticket_id):
        result = self.tickets.delete_one({"_id": ObjectId(ticket_id)})
        return result.deleted_count
