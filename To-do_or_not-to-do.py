import sys
"""
print("This is the name of the script: ", sys.argv[0])
print("This is the name of the script: ", len(sys.argv))
print("This is the name of the script: ", str(sys.argv))
"""
rtfm = ("Command Line Todo application" "\n"
    "=============================" "\n"
    "\n"
    "Command line arguments:" "\n"
    " -l   Lists all the tasks" "\n"
    " -a   Adds a new task" "\n"
    " -r   Removes a task" "\n"
    " -c   Completes a task")

def lister():
    todolist = open("tasklist.txt", "r")
    list_of_tasks = todolist.readlines()
    if len(list_of_tasks) == 0:
        print("No todos for today! :)")
    else:
        for i in range(len(list_of_tasks)):
            print(str(i+1) + " - " + list_of_tasks[i].strip())
    todolist.close()

def task_adder(new_text):
    todolist = open("tasklist.txt", "a")
    todolist.write("\n" + "[ ] " + new_text)
    todolist.close()

def task_remover(remover):
    todolist = open("tasklist.txt", "r")
    list_of_task = todolist.readlines()
    list_of_task = list_of_task[:int(remover)-1] + list_of_task[int(remover):]
    todolist.close()
    todolist = open("tasklist.txt", "w")
    for i in range(len(list_of_task)):
        todolist.write(list_of_task[i].strip() + "\n")
    todolist.close()

def task_checker(checker):
    todolist = open("tasklist.txt", "r")
    list_of_task = todolist.readlines()
    word = list_of_task[int(checker)-1]
    word = word[:1] + "X]" + word[3:]
    word_list = [word]
    list_of_task = list_of_task[:int(checker)-1] + word_list + list_of_task[int(checker):]
    todolist.close()
    todolist = open("tasklist.txt", "w")
    for i in range(len(list_of_task)):
        todolist.write(list_of_task[i].strip() + "\n")
    todolist.close()


if len(sys.argv) == 1:
    print(rtfm)
elif len(sys.argv) == 2:
    if sys.argv[1] == "-l":
        lister()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-a":
        task_adder(sys.argv[2])
    elif sys.argv[1] == "-r":
        task_remover(sys.argv[2])
    elif sys.argv[1] == "-c":
        task_checker(sys.argv[2])
    else:
        print("Unsupported argument." + "\n" + "\n" + rtfm)