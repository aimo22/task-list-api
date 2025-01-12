from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.id"))
    
    def to_dict_with_goal(self):
        if not self.completed_at:
            self.is_complete = False
        return (dict(
                id=self.id,
                title=self.title,
                description=self.description,
                is_complete=self.is_complete,
                goal_id=self.goal_id
            ))
    def to_dict(self):
        if not self.completed_at:
            self.is_complete = False
        return (dict(
                id=self.id,
                title=self.title,
                description=self.description,
                is_complete=self.is_complete,
            ))

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict["title"],
            description = data_dict["description"],
            is_complete = data_dict["completed_at"]
        )
