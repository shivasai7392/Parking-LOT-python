class BaseModel:
    def __init__(self):
        self._id = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
