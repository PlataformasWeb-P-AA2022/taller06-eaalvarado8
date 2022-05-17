from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoId = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    independent = Column(String)

    def __repr__(self):
        return "Paises: pais=%s capital=%s continente:%s dial:%s geoId:%s itu:%s lenguajes:%s independent:%s" % (
                          self.pais,
                          self.capital,
                          self.continente,
                          self.dial,
                          self.geoId,
                          self.itu,
                          self.lenguajes,
                          self.independent)


Base.metadata.create_all(engine)
