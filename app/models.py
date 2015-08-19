from app import db
from datetime import datetime
class EventLog(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    source = db.Column(db.String(64))
    action = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime)

    def __init__(self, source, action, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        self.timestamp = timestamp
        if source is not 'WebUI' and source is not 'Timer':
            source = 'Invalid Source'
        if action is not 'TurnOn' and action is not 'TurnOff':
            action = 'Invalid Action'
        self.source = source
        self.action = action
    def __repr__(self):
        return '<Log %r %r %r %r>' % (self.id, self.timestamp, self.action, self.source)
