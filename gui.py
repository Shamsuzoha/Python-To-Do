import functions
import PySimpleGUI as sg # type: ignore
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple4")

clock = sg.Text("", key = "clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip ="Enter To Do", key = "todo")
add_button = sg.Button("Add")
listBox = sg.Listbox(values =functions.getTodos(), key = "todos", enable_events=True, size=[45, 10]) #
editButton = sg.Button("Edit")
completeButton = sg.Button("Complete")
exitButton = sg.Button("Exit")

window = sg.Window("To-Do App",
                layout=[[clock],[label], [input_box,  add_button],[listBox, editButton, completeButton],[exitButton]],
                font = ("Helvetica",20))

while True:
    event, values = window.read(timeout = 200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.getTodos()
            new_todo = values["todo"]
            todos.append(new_todo + "\n")
            functions.writeTodos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.getTodos()
                index = todos.index(todo_edit)
                todos[index] = new_todo + "\n"
                functions.writeTodos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        case "Complete":
            try:    
                todo_complete = values["todos"][0]
                todos = functions.getTodos()
                todos.remove(todo_complete)
                functions.writeTodos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break
window.close()