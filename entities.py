from google.appengine.ext import db


"""
Data type representing a factory
"""
class Factory(db.Model):
	producers = db.ListProperty(db.Key)
	workers = db.ListProperty(db.Key)
	name = db.StringProperty(required=True)
	address = db.PostalAddressProperty()
	location = db.GeoPtProperty()
    
"""
Data type representing a product with a BeneTag
"""
class Product(db.Model):
    name = db.StringProperty(required=True)
    picture = db.BlobProperty()
    producerName = db.StringProperty()
    factoryMade = db.ReferenceProperty(Factory)
    badges = db.ListProperty(db.Key)

"""
Data type representing a producer
"""
class Producer(db.Model):
    factories = db.ListProperty(db.Key)
    name = db.StringProperty(required=True)
    email = db.StringProperty()
    profileOwner = db.UserProperty(required=True)
    description = db.TextProperty()
    verifiedProducer = db.BooleanProperty()
    companyLogo = db.BlobProperty()

"""
Data type representing a worker
"""
class Worker(db.Model):
	name = db.StringProperty()
	factory = db.ReferenceProperty(Factory)
	profile = db.TextProperty()
	picture = db.BlobProperty()

"""
Data type representing a badge
"""
class Badge(db.Model):
    name = db.StringProperty(required=True)
    icon = db.BlobProperty()
    description = db.StringProperty() 
