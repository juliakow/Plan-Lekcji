from classes_definitions import define_classes

def schedule_classes(classes, teachers):
    classes_dict = define_classes()
    Class = classes_dict['Class']
    Teacher = classes_dict['Teacher']
    
    classes.sort(key=lambda x: sum(sub.hours for sub in x.subjects), reverse=True)
    schedule = {teacher.id: [] for teacher in teachers}
    
    for class_ in classes:
        for teacher in teachers:
            if teacher.id not in [teacher_id for teacher_id, _ in schedule.items()]:
                schedule[teacher.id].append(class_)
                break
    
    return schedule
