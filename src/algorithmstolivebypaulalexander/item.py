
class Item:
    def __init__(self, name="", value=0, unique_id=None):
        if unique_id is not None:
            self.unique_id = unique_id
        else:
            self.unique_id = id(self)
        self.name = name
        self.value = value
