
class FamilyFinder:

    def __init__(self, source):
        self.source = source

    def getAncestors(self, name):
        return next((
            person["ancestors"]
            for person in self.source
            if person["name"] == name), [])
