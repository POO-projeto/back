from models.task import Task


def nest_tasks(obj):
    return [Task.query.get(task_obj.task_id) for task_obj in obj.tasks]
