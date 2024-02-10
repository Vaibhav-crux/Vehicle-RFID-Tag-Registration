from sqlalchemy.orm import sessionmaker
from db.models import DoNumber
from sqlalchemy import create_engine

def fetch_wb_code(do_no):
    # Fetch the wb_code corresponding to the given do_no from the database

    engine = create_engine('sqlite:///example.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the wb_code based on the selected do_no
    result = session.query(DoNumber.wb_code).filter(DoNumber.do_no == do_no).first()

    # Close the session
    session.close()

    # Extract the wb_code from the result
    if result:
        return result[0]
    else:
        return ""
