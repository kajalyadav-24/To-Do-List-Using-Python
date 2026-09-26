import streamlit as st
import csv

CSV_FILE = "tasks.csv"


def main():
    st.set_page_config(page_title="To-Do List", page_icon="✅", layout="centered")
    st.title("To-Do List")
    st.caption("Add tasks, mark them done, or remove them one by one.")

    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?cs=srgb&dl=pexels-adrien-olichon-2387793.jpg&fm=jpg");
            background-attachment: fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    tasks = load_tasks()

    with st.form("add_task_form", clear_on_submit=True):
        task_input = st.text_input("Add a new task:")
        submitted = st.form_submit_button("Add task")
        if submitted and task_input.strip():
            tasks.append({"text": task_input.strip(), "done": False})
            save_tasks(tasks)
            st.success("Task added.")
            st.rerun()

    pending = sum(1 for t in tasks if not t["done"])
    completed = sum(1 for t in tasks if t["done"])
    st.write(f"**{len(tasks)}** total · **{pending}** pending · **{completed}** done")

    display(tasks)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear completed", use_container_width=True, disabled=completed == 0):
            tasks = [t for t in tasks if not t["done"]]
            save_tasks(tasks)
            st.rerun()
    with col2:
        if st.button("Clear all tasks", use_container_width=True, disabled=len(tasks) == 0):
            save_tasks([])
            st.rerun()


def load_tasks():
    """Load tasks from CSV. Supports plain text rows and text,done rows."""
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            tasks = []
            for row in reader:
                if not row or not row[0].strip():
                    continue
                text = row[0].strip()
                done = len(row) > 1 and row[1].strip().lower() in ("1", "true", "yes", "done")
                tasks.append({"text": text, "done": done})
            return tasks
    except FileNotFoundError:
        return []


def display(tasks):
    if not tasks:
        st.info("No tasks yet. Add one above to get started.")
        return

    st.subheader("Your tasks")
    for i, task in enumerate(tasks):
        left, mid, right = st.columns([0.1, 0.7, 0.2])
        with left:
            done = st.checkbox(
                "Done",
                value=task["done"],
                key=f"done_{i}",
                label_visibility="collapsed",
            )
            if done != task["done"]:
                tasks[i]["done"] = done
                save_tasks(tasks)
                st.rerun()
        with mid:
            label = f"~~{task['text']}~~" if task["done"] else task["text"]
            st.markdown(f"{i + 1}. {label}")
        with right:
            if st.button("Delete", key=f"del_{i}", use_container_width=True):
                tasks.pop(i)
                save_tasks(tasks)
                st.rerun()


def save_tasks(tasks):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([[t["text"], "1" if t["done"] else "0"] for t in tasks])


if __name__ == "__main__":
    main()
