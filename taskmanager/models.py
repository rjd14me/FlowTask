class Task:
    def __init__(self, id, description, status="To Do"):
        self.id = id
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
        }
