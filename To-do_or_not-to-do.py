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
    " -r   Removes an task" "\n"
    " -c   Completes an task")

def lister():
    todolist = open("tasklist.txt", "r")
    list_of_tasks = todolist.readlines()
    for i in range(len(list_of_tasks)):
        print(str(i+1) + " - " + list_of_tasks[i].strip())
    todolist.close()

if len(sys.argv) == 1:
    print(rtfm)
if len(sys.argv) == 2:
    if sys.argv[1] == "-l":
        lister()
    elif sys.argv[1] == "-a":
        print("You wanted to add a new task.")
    elif sys.argv[1] == "-r":
        print("You wanted to remove a task.")
    elif sys.argv[1] == "-c":
        print("You wanted to complete a task.")
    else:
        print("Unsupported argument." + "\n" + "\n" + rtfm)
