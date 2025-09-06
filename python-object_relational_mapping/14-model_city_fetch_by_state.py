#!/usr/bin/python3
"""Start link class to table in database
this will create the tables
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    Citys = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for c, s in Citys:
        print(f"{s.name}: ({c.id}) {c.name}")
