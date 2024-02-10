from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Details(Base):
    __tablename__ = 'in_out_details'

    rfid_tag = Column(Integer, primary_key=True)
    vehicle_no = Column(String)
    vehicle_type = Column(String)
    reg_time = Column(String)
    user = Column(String)
    shift = Column(Integer)
    time_in = Column(String)
    date_in = Column(String)
    dono = Column(String)
    doname = Column(String)
    driver = Column(String)
    wb_code = Column(String)
    tare_weight = Column(String)
    tare_time = Column(String)
    tare_date = Column(String)
    gross_weight = Column(String)
    gross_time = Column(String)
    gross_date = Column(String)
    indicator = Column(String)
    palcetovisit = Column(String)
    purpose = Column(String)
    persontovisit = Column(String)
    date_out = Column(String)
    time_out = Column(String)

class VehicleReg(Base):
    __tablename__ = 'vehicle_reg'

    rfid_tag = Column(Integer, primary_key=True)
    vehicle_no = Column(String)
    vehicle_type = Column(String)
    date_reg = Column(Integer, primary_key=True)
    time_reg = Column(String)
    do_no = Column(String)
    do_name = Column(String)
    wb_code = Column(String)
    driver = Column(String)
    user = Column(String)
    shift = Column(String)
    indicator = Column(String)

class VehicleMaster(Base):
    __tablename__ = 'vehicle_mast'

    rfid_tag = Column(String, primary_key=True)
    vehicle_no = Column(String)
    vehicle_type = Column(String)

class User(Base):
    __tablename__ = 'vehicle_master'

    user_name = Column(Integer, primary_key=True)
    user_password = Column(String)


class DoNumber(Base):
    __tablename__ = 'do_no_details'

    do_no = Column(Integer, primary_key=True)
    do_name = Column(String)
    wb_code = Column(String)
    
class Time(Base):
    __tablename__ = 'in-out details'

    start_time = Column(Integer, primary_key=True)
    stop_time = Column(String)
    name = Column(String)

