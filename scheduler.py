from classes_definitions import define_classes

def schedule_classes(classes, teachers):
    classes_dict = define_classes()
    Class = classes_dict['Class']
    Teacher = classes_dict['Teacher']
    
    # Sortowanie klas według sumarycznej liczby godzin przedmiotów
    classes.sort(key=lambda x: sum(sub.hours for sub in x.subjects), reverse=True)
    
    # Inicjalizacja słownika harmonogramu, używając ID nauczycieli jako kluczy
    schedule = {teacher.id: [] for teacher in teachers}
    
    # Przejście przez klasy w porządku malejącym
    for class_ in classes:
        # Przejście przez wszystkich nauczycieli
        for teacher in teachers:
            # Sprawdzanie, czy nauczyciel nie prowadzi już lekcji
            if teacher.id not in [teacher_id for teacher_id, _ in schedule.items()]:
                # Dodanie klasy do harmonogramu nauczyciela
                schedule[teacher.id].append(class_)
                break
    
    return schedule
