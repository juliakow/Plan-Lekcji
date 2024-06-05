import json
from classes_definitions import define_classes

def load_data(file_path):
    classes_dict = define_classes()
    Subject = classes_dict['Subject']
    Class = classes_dict['Class']
    Teacher = classes_dict['Teacher']
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    teachers = [Teacher(id=teacher['id'], name=teacher['name'], subjects=teacher['subjects']) for teacher in data['teachers']]
    classes = [Class(id=class_, name=class_['name'], subjects=[Subject(name=sub['name'], hours=sub['hours']) for sub in class_['subjects']]) for class_ in data['classes']]
    
    return teachers, classes
