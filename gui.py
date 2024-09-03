import functions
import PySimpleGUI as sg # type: ignore

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip ="Enter To Do", key = "todo")
add_button = sg.Button("Add")
listBox = sg.Listbox(values =functions.getTodos(), key = "todos", enable_events=True, size=[45, 10]) #
editButton = sg.Button("Edit")

window = sg.Window("To-Do App",
                layout=[[label], [input_box,  add_button],[listBox, editButton]],
                font = ("Helvetica",20))

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.getTodos()
            new_todo = values["todo"]
            todos.append(new_todo + "\n")
            functions.writeTodos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = functions.getTodos()
            index = todos.index(todo_edit)
            todos[index] = new_todo + "\n"
            functions.writeTodos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break
window.close()