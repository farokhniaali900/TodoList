from app import db

class TaskData(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(30))
    task = db.Column(db.Text())
    done = db.Column(db.Boolean() , default=False)
    
    def __repr__(self):
        return f"{self.title} - {self.done}"