def evaluate_schedule(schedule):
    scores = {}
    for teacher, classes in schedule.items():
        scores[teacher] = len(classes)
    return scores
