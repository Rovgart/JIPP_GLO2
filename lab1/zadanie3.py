tasks = [
    {
        'title': 'Zadanie 1',
        'description': 'Stworzenie nowego repozytorium na GitHub',
        'priority': 1,
        'time': 500,
        'status': 'To Do'
    },
    {
        'title': 'Zadanie 2',
        'description': 'Napisanie pierwszego programu',
        'priority': 212,
        'time': 300,  # Dodano brakujący czas
        'status': 'In Progress'
    },
    {
        'title': 'Zadanie 3',
        'description': 'Uzupełnienie programu',
        'priority': 3,
        'time': 100,  # Dodano brakujący czas
        'status': 'Done'
    }
]

def getOptimalTasks(task_list):
    sorted_tasks = sorted(task_list, key=lambda x: (-x['priority'], -x['time']))
    return sorted_tasks

optimal_tasks = getOptimalTasks(tasks)

print("Zoptymalizowana lista zadań:")
for task in optimal_tasks:
    print(f"Tytuł: {task['title']}")
    print(f"Priorytet: {task['priority']}")
    print(f"Czas: {task['time']}")
    print(f"Status: {task['status']}")
    print("---")