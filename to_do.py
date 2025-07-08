import streamlit as st

# to_do=[]

# def add_task(task):
#     to_do.append(task)
#     print(task)
#     return task

# def mark_task(id):
#     for i , work in enumerate(to_do):
#         if (work['id']) == id:
#             to_do.pop((i))
#             print("Deleted")
#             return
#     print("Not Found")

# def show_list():
#     print(to_do)

# def menu():
#     while True:
#         print("\n Menu: 1 for Adding task 2 for print list 3 to delete task")
        
#         choice=input("Enter Choice : ")
        

#         if choice == "1":
#             print("You need to add task")
#             id= len(to_do)+1
#             work=input("Enter Work : ")
#             add_task({"id": id, "work" : work})

#         elif choice=="2":
#             show_list()

#         elif choice=="3":
#             print("Mark task as completed")
#             id= int(input("Enter id to delete "))
#             mark_task(id)
            
#         else:
#             print("Invalid Choice")
#             return False

# menu()


def add_task(task):
    if task:
        id=len(st.session_state.tasks)+1
        st.session_state.tasks.append({"id": id, "task":task})
        st.write(f"Added task to list {task}")
    return task

def mark_task(id):
    for i , work in enumerate(st.session_state.tasks):
        if (work['id']) == id:
            st.session_state.tasks.pop((i))
            st.write("Deleted")
            return
    st.write("Not Found")

if "tasks" not in st.session_state:
    st.session_state.tasks=[]

st.title("TO DO List")
choice=st.text_input("\n Press: 1 for adding task 2 for all tasks list 3 to delete task" )

st.write(f"Your Choice {choice}")

if choice == "1":
    task=st.text_input("Add task details", key="task_input")
    if st.button("add task"):
        (add_task(task))

elif choice == "2":
    st.write(st.session_state.tasks)

elif choice == "3":
    delete_choice= (st.text_input(" Enter Id which one to delete: "))
    delete_choice= int(delete_choice)
    mark_task(delete_choice)





