import streamlit as st
import functions

td = functions.getTodos()

def addTodo():
    tf = st.session_state["todoText"]
    td.append(tf+"\n")
    functions.writeTodos(td)

st.title("To-Do App")

for index, item in enumerate(td):
    checkbox = st.checkbox(item, key = item)
    if checkbox:
        td.pop(index)
        functions.writeTodos(td)
        del st.session_state[item]
        st.rerun()

st.text_input(label = "Add To-Do",placeholder = "Add new To-Do...", on_change = addTodo, key = "todoText")