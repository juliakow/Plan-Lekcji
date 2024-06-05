from data_loader import load_data
from scheduler import schedule_classes
from evaluator import evaluate_schedule

def main():
    file_path = 'plan_lekcji.json'
    teachers, classes = load_data(file_path)
    schedule = schedule_classes(classes, teachers)
    evaluation = evaluate_schedule(schedule)
    
    print("Harmonogram lekcji:")
    for teacher, classes in schedule.items():
        print(f"{teacher.name}:")
        for class_ in classes:
            print(f"  {class_.name}")
    
    print("\nOcena harmonogramu:")
    for teacher, score in evaluation.items():
        print(f"{teacher}: {score} lekcji")

if __name__ == "__main__":
    main()
