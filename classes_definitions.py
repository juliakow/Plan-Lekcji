def define_classes():
    class Subject:
        def __init__(self, name, hours):
            self.name = name
            self.hours = hours

    class Class:
        def __init__(self, id=None, name=None, subjects=None):
            self.id = id
            self.name = name
            self.subjects = subjects if subjects else []

    class Teacher:
        def __init__(self, id=None, name=None, subjects=None):
            self.id = id
            self.name = name
            self.subjects = subjects if subjects else []

    return {'Subject': Subject, 'Class': Class, 'Teacher': Teacher}
