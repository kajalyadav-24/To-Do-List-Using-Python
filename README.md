# To-Do-List-Using-Python

A simple To-Do List web application built using Python and Streamlit.

The application allows users to manage tasks by adding new tasks, viewing the current task list, and clearing all tasks. Tasks are stored in a CSV file for persistence.

## Features

- Add new tasks
- View current tasks
- Clear all tasks
- Store tasks using a CSV file
- Simple web interface using Streamlit

## Technologies Used

- Python
- Streamlit
- CSV

## Installation

1. Clone the repository:

```bash
git clone https://github.com/kajalyadav-24/To-Do-List-Using-Python.git
```

2. Navigate to the project directory:

```bash
cd To-Do-List-Using-Python
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your web browser.

## How to Use

1. Enter a task in the **Add a new task** input field.
2. Click **Add** to add the task.
3. The current tasks will be displayed on the page.
4. Click **Clear all tasks** to remove all tasks.

## Repository Structure

```text
To-Do-List-Using-Python/
│
├── app.py
├── requirements.txt
├── README.md
└── tasks.csv
```

### app.py

Contains the main Streamlit application code and task management logic.

### requirements.txt

Contains the Python dependencies required to run the application.

### tasks.csv

Stores the To-Do List tasks.