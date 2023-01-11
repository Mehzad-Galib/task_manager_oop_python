import uuid
from datetime import datetime

task_list = []


class Task:

    def __init__(self, task_name, idx,  created_time, updated_time, completed_time, task_done) -> None:
        self.task_name = task_name
        self.created_time = created_time
        self.updated_time = updated_time
        self.completed_time = completed_time
        self.task_done = task_done
        self.idx = idx

    def update_task(self, new_name):
        task_list[task_no-1].task_name = new_name
        now = datetime.now()
        created_time = now.strftime("%d/%m/%Y %H:%M:%S")
        task_list[task_no-1].updated_time = created_time

    def complete_task(self):
        task_list[task_no-1].task_done = True
        now = datetime.now()
        created_time = now.strftime("%d/%m/%Y %H:%M:%S")
        task_list[task_no-1].completed_time = created_time


while True:
    print("1. Add New Task\n2. Show All Task\n3. Show Incomplete Task\n4. Show Completed Task\n5. Update Task\n6. Mark a Task Completed\n")
    option = int(input("ENTER OPTION: "))

    # Add new task
    if option == 1:
        task_name = input("Enter New Task: ")
        task_id = uuid.uuid1()
        now = datetime.now()
        created_time = now.strftime("%d/%m/%Y %H:%M:%S")

        task_manager = Task(task_name, task_id,
                            created_time, 'NA', 'NA', False)
        task_list.append(task_manager)
        print("\nTask Created Successfully\n")

    # show all tasks
    if option == 2:
        for i in range(len(task_list)):
            print(f"\nID - {task_list[i].idx}\nTask - {task_list[i].task_name}\nCreated Time - {task_list[i].created_time}\nUpdated Time - {task_list[i].updated_time}\nCompleted - {task_list[i].task_done}\nCompleted Time - {task_list[i].completed_time}")

    # show incomplete task
    if option == 3:
        print("\nShowing Incomplete Task:\n")
        for i in range(len(task_list)):
            if not task_list[i].task_done:
                print(f"\nID - {task_list[i].idx}\nTask - {task_list[i].task_name}\nCreated Time - {task_list[i].created_time}\nUpdated Time - {task_list[i].updated_time}\nCompleted - {task_list[i].task_done}\nCompleted Time - {task_list[i].completed_time}")

    # show completed task
    if option == 4:
        if len(task_list) == 0:
            print("No Completed Task")

        for i in range(len(task_list)):
            if task_list[i].task_done:
                print(f"\nID - {task_list[i].idx}\nTask - {task_list[i].task_name}\nCreated Time - {task_list[i].created_time}\nUpdated Time - {task_list[i].updated_time}\nCompleted - {task_list[i].task_done}\nCompleted Time - {task_list[i].completed_time}")

    # updating task
    if option == 5:
        for i in range(len(task_list)):
            print(f"\nTask No - {i+1}\nID - {task_list[i].idx}\nTask - {task_list[i].task_name}\nCreated Time - {task_list[i].created_time}\nUpdated Time - {task_list[i].updated_time}\nCompleted - {task_list[i].task_done}\nCompleted Time - {task_list[i].completed_time}")

        task_no = int(input("Enter Task No: "))
        new_name = input("Enter New Task: ")
        task_list[task_no-1].update_task(new_name)
        print("\nTask Updated Successfully\n")

    # marking a task complete
    if option == 6:
        for i in range(len(task_list)):
            print(f"\nTask No - {i+1}\nID - {task_list[i].idx}\nTask - {task_list[i].task_name}\nCreated Time - {task_list[i].created_time}\nUpdated Time - {task_list[i].updated_time}\nCompleted - {task_list[i].task_done}\nCompleted Time - {task_list[i].completed_time}")
        task_no = int(input("Enter Task No: "))

        task_list[task_no-1].task_done = True
        task_list[task_no-1].complete_task()
        print("\nTask Marked Completed Successfully\n")

    if option == 0:
        break
