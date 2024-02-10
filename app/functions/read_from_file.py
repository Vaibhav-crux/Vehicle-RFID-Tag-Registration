from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import VehicleMaster
import pathlib

def read_rfid_from_file():
    file_path = pathlib.Path("app/static/file.txt")

    result = None
    rfid_tag_value = None

    try:
        with file_path.open('r') as file:
            content = file.read().strip()

            # Check if the content starts with "[rfid_tag:" and ends with "]"
            if content.startswith("[rfid_tag:") and content.endswith("]"):
                rfid_tag_value = content.split(":")[1].rstrip("]").strip()
                print("File:", rfid_tag_value)

                # Check if the RFID tag is present in the database
                engine = create_engine('sqlite:///example.db')
                Session = sessionmaker(bind=engine)
                session = Session()

                # Query the database
                result = session.query(VehicleMaster.rfid_tag, VehicleMaster.vehicle_no, VehicleMaster.vehicle_type) \
                    .filter_by(rfid_tag=rfid_tag_value).first()

                session.close()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return result, rfid_tag_value
