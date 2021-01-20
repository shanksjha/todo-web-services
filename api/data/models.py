from api import db


class Bucket(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    bucket_name = db.Column(db.String(100),unique=True)
    status = db.Column(db.Boolean(),default=True)
    misc_details = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())

    def __init__(self,bucket_name,status=None,created_at=None,updated_at=None):
        self.bucket_name = bucket_name
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create_bucket(bucket_obj):
        db.session.add(bucket_obj)
        db.session.commit()

    @staticmethod
    def get_bucket_details():

        return db.session.query(Bucket).outerjoin(ToDoDetails,Bucket.id == ToDoDetails.bucket_id).\
            with_entities(Bucket.id,Bucket.bucket_name,
                          ToDoDetails.id,ToDoDetails.to_do_name,ToDoDetails.status).all()


class ToDoDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to_do_name = db.Column(db.String(100), unique=True)
    bucket_id = db.Column(db.Integer, db.ForeignKey('bucket.id'))
    status = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())

    def __init__(self,to_do_name,bucket_id,status=None,created_at=None,updated_at=None):
        self.to_do_name = to_do_name
        self.bucket_id = bucket_id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create_todos(todo_obj):
        db.session.add(todo_obj)
        db.session.commit()

    @staticmethod
    def update_todo(todo_id, todo_status):
        todo_details = ToDoDetails.query.get_or_404(todo_id)
        todo_details.status = todo_status
        db.session.commit()










