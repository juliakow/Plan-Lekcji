def evaluate_schedule(schedule):
    scores = {}
    for teacher, classes in schedule.items():
        scores[teacher.name] = len(classes)
    return scores
