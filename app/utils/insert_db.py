import sys
import os

# Add the parent directory of 'app' to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, VehicleMaster, DoNumber


# Create an SQLite engine (replace 'sqlite:///example.db' with your desired database file)
engine = create_engine('sqlite:///example.db')

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create a session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create the tables if they don't exist
Base.metadata.create_all(engine)

# Data to be inserted into the vehicle_master table
data_to_insert = [
    {"do_no": "3001402031", "do_name": "durga", "wb_code": "bna01"},
    {"do_no": "3001402011", "do_name": "laddu", "wb_code": "bna05"},
    # ... (insert the remaining data in the same format)
]

"""
3001402031	durga	bna01
3001402011	laddu	bna05

"""

# Insert the data into the vehicle_master table
for data in data_to_insert:
    vehicle = DoNumber(**data)
    session.add(vehicle)

# Commit the changes and close the session
session.commit()
session.close()
