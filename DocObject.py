
class DocOject:
    grantor = ''
    grantee = ''
    def __init__(self, Grantor, Grantee):
        self.grantor = Grantor
        self.grantee = Grantee

    def print_object(self):
        print(self.grantor + ": " + self.grantee)