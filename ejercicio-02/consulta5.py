from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from crear_base import Paises

engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Paises).filter(or_(Paises.pais.like("%uador"), Paises.capital.like("%ito"))).all()
print(paises)