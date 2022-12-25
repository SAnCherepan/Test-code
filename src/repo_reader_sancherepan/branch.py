class Branch(object):
    def __init__(self, data):
        if "name" in data:
            self.name = data["name"]
        else:
            raise ValueError('bad repository branch data: expected attribute "name"')

        if "protected" in data:
            self.protected = data["protected"]
        else:
            raise ValueError('bad repository branch data: expected attribute "protected"')
