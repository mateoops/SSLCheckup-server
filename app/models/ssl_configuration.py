from run import db

class SSLConfiguration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    port = db.Column(db.Integer, nullable=False)

    def __init__(self, host, address, port, description=None):
        self.host = host
        self.address = address
        self.port = port
        self.description = description
