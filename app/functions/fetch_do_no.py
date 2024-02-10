from sqlalchemy.orm import sessionmaker
from db.models import DoNumber
from sqlalchemy import create_engine

def fetch_do_numbers():
    # Fetch DO Numbers from the DoNumber table

    engine = create_engine('sqlite:///example.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all DO Numbers from the DoNumber table
    do_numbers = session.query(DoNumber.do_no).all()

    # Close the session
    session.close()

    # Extract the DO Numbers from the result
    do_numbers_list = [str(do_number[0]) for do_number in do_numbers]

    return do_numbers_list
