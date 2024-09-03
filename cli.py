import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = functions.getTodos()
        todos.append(todo)
        functions.writeTodos(todos)

    elif user_action.startswith("show"):
        todos = functions.getTodos()
        new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index+1}-{item}")

    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:])
            todos = functions.getTodos()
            if 1 <= index < len(todos)+1:
                new_todo = input("Enter the new todo: ")
                todos[index-1] = new_todo + "\n"
                functions.writeTodos(todos)
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid Command")
            continue

    elif user_action.startswith("complete"):
        try:
            index = int(user_action[9:])
            todos = functions.getTodos()
            if 1 <= index < len(todos)+1:
                removedTodo = todos[index-1]
                todos.pop(index-1)
                functions.writeTodos(todos)
                print(f"{removedTodo.strip('\n')} has been completed!")
            else:
                print("Invalid index!") 
        except ValueError:
            print("Invalid Command")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command!")

print("Bye!")
