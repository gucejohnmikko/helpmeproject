from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Store, Base, PetsItem, User

engine = create_engine('sqlite:///petstore.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Animals for PetCo
store1 = Store(user_id=1, name="PetCo")

session.add(store1)
session.commit()

petsItem1 = PetsItem(user_id=1, name="Johnson", description="Pomeranian",
                     price="$2.99", pet_type="Dog", store=store1)

session.add(petsItem1)
session.commit()

petsItem2 = PetsItem(user_id=1, name="Odette", description="Shit-tzu",
                     price="$5.50", pet_type="Dog", store=store1)

session.add(petsItem2)
session.commit()

petsItem3 = PetsItem(user_id=1, name="Nemo", description="Clownfish",
                     price="$3.99", pet_type="Fish", store=store1)

session.add(petsItem3)
session.commit()

petsItem4 = PetsItem(user_id=1, name="Jynx", description="Sphynx",
                     price="$7.99", pet_type="Cat", store=store1)

session.add(petsItem4)
session.commit()

petsItem5 = PetsItem(user_id=1, name="Rudolph", description="Burmese Python",
                     price="$1.99", pet_type="Reptile", store=store1)

session.add(petsItem5)
session.commit()

petsItem6 = PetsItem(user_id=1, name="Spidey", description="Turtle",
                     price="$.99", pet_type="Reptile", store=store1)

session.add(petsItem6)
session.commit()

print "added menu items!"