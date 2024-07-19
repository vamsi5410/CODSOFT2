from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, reminder_time=None):
        task = {
            'id': len(self.tasks) + 1,
            'name': name,
            'status': 'pending',
            'reminder_time': reminder_time
        }
        self.tasks.append(task)
        return task

    def update_task(self, task_id, new_name, reminder_time=None):
        for task in self.tasks:
            if task['id'] == task_id:
                task['name'] = new_name
                task['reminder_time'] = reminder_time
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                return task
        return None

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'completed'
                return task
        return None

    def list_tasks(self):
        return self.tasks
