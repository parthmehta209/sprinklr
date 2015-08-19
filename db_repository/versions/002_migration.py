from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event_log = Table('event_log', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('source', String(length=64)),
    Column('action', String(length=64)),
    Column('timestamp', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event_log'].columns['action'].create()
    post_meta.tables['event_log'].columns['timestamp'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event_log'].columns['action'].drop()
    post_meta.tables['event_log'].columns['timestamp'].drop()
