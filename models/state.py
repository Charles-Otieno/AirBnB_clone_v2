#!/usr/bin/python3

"""A module that has the state class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import models
import shlex
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """A class for State"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        variable = models.storage.all()
        lista = []
        res = []
        for key in variable:
            city = key.replace('.', ' ')
            city = shlex.split(city)

            if (city[0] == 'City'):
                lista.append(variable[key])

        for elements in lista:
            if (elements.state_id == self.id):
                res.append(elements)

        return (res)
