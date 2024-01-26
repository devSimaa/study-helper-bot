from peewee import (
    SqliteDatabase,
    Model, CharField, DateField, PrimaryKeyField, JSONField
)
db = SqliteDatabase(f'database/test.sqlite')

class User(Model):
    id = PrimaryKeyField()
    name = CharField()
    group = CharField()
    status = CharField(default='user')

    class Meta:
        database = db

class Schedule(Model):
    Group = CharField
    Lessons = JSONField()
    class Meta:
        database = db
User.create_table()
Schedule.create_table()

User.create(id='123123',
            name='d').save()