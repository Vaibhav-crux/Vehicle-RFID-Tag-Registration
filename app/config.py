from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import your model from mode.py
from db.models import Base, Details, VehicleReg, VehicleMaster, User, DoNumber, Time

# Create an SQLite engine (replace 'sqlite:///example.db' with your desired database file)
engine = create_engine('sqlite:///example.db')

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create a session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create the tables
Base.metadata.create_all(engine)

# Commit the changes and close the session
session.commit()
session.close()
