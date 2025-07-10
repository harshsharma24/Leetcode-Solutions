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
    if not task.strip():
        return False

    if task:
        id=st.session_state.tasks[-1]['id'] if st.session_state.tasks else 0
        st.session_state.tasks.append({"id": id+1, "task":task.strip(), "done": False})

    return True

def mark_task(id):
    for i , work in enumerate(st.session_state.tasks):
        if (work['id']) == id:
            st.session_state.tasks.pop((i))
            return True
    return False

def show_tasks_ui():
    st.subheader="Tasks"

    if not st.session_state.tasks:
        return
    
    total_tasks=len(st.session_state.tasks)
    completed_tasks= sum(1 for task in st.session_state.tasks if task["done"])
    pending_tasks= total_tasks - completed_tasks

    # Display Summary
    st.markdown(f"**Total**: {total_tasks} | **Completed**: {completed_tasks} | **Total**: {pending_tasks} ")

    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.85, 0.5])
        with col1:
            st.markdown(f"**{task['id']}** {task['task']}")
        with col2:
            checked = st.checkbox("Done", key=f"done_{task['id']}", value=task['done'])
            st.session_state.tasks[i]['done'] = checked


if "tasks" not in st.session_state:
    st.session_state.tasks=[]

def add_task_ui():
    with st.form("add_task_form"):
        task= st.text_input("Add task Details")
        submitted= st.form_submit_button("Add Task")
        if submitted:
            success=add_task(task)
            if success:
                st.success(f"Added task to list {task}")
            else:
                st.error("Task cannot be empty")

def delete_task_ui():
    with st.form("delete_task_form"):
        delete_choice= (st.text_input(" Enter Id which one to delete: "))
        submitted= st.form_submit_button("Delete Task")
        if submitted:
            if delete_choice.isdigit(): 
                delete_choice= int(delete_choice)
                success=mark_task(delete_choice)
                if success:
                    st.success("Task Deleted")
                else:
                    st.error("Task ID not found")
            else:
                st.error("Please enter a valid numeric ID")

def main():
    st.title("TO DO List")
    choice = st.radio("Choose an Option:", ["Add Task", "Show all Tasks", "Delete Task"])

    if choice == "Add Task":
        add_task_ui()
    elif choice == "Show all Tasks":
        show_tasks_ui()
    elif choice == "Delete Task":
        delete_task_ui()

if __name__ == "__main__":
    main()






