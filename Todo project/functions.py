FILEPATH = "Todo project\\todos.txt"

def getTodos(filepath = FILEPATH):
    #Read a text file and return a list of to-do items
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def writeTodos(todos_params, filepath = FILEPATH):
    #Write a list of to-do items to a text file
    with open(filepath, "w") as file:
        file.writelines(todos_params)
