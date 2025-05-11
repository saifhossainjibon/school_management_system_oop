class ClassRoom:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.subjects=[]

    def add_students(self,student):
        roll_no=f"{self.name}-{len(self.students)+1}"