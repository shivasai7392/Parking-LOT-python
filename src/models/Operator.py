from src.models.BaseModel import BaseModel


class Operator(BaseModel):
    def __init__(self):
        self._name = None
        self._employee_Id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def employee_Id(self):
        return self._employee_Id

    @employee_Id.setter
    def employee_Id(self, value):
        self._employee_Id = value
