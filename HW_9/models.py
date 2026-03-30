from mongoengine import connect, Document, StringField, ListField, ReferenceField


connect(db="quotes_hw9",
        host="mongodb+srv://vladkuznecov271_db_user:admin@vlados.wu6wbvl.mongodb.net/Vlados?retryWrites=true&w=majority")

class Author(Document):
    fullname = StringField(unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    quote = StringField()
    tags = ListField(StringField())
    author = ReferenceField(Author)