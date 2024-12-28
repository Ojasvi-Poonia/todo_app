# FastAPI Todo List App

A lightweight and efficient Todo List backend application built using **FastAPI**. This app provides basic CRUD functionality to manage tasks with an in-memory database.

---

## Features

- **Add Tasks**: Use the `POST` endpoint to create new tasks.
- **View Tasks**: Use the `GET` endpoint to retrieve all tasks or a specific task by its ID.
- **Update Tasks**: Use the `PUT` endpoint to update existing tasks.
- **Delete Tasks**: Use the `DELETE` endpoint to remove tasks by ID.
- **In-Memory Database**: Data is stored in memory, making it lightweight and ideal for development and testing.

---

## Getting Started

### Prerequisites
- Python 3.7+
- `pip` (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ojasvi-Poonia/todo_app.git
   cd todo_app
2. Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate    # On macOS/Linux
  venv\Scripts\activate       # On Windows
```
3. Install the dependencies:

  ```bash
  Copy code
  pip install -r requirements.txt
```
  Usage
  Run the FastAPI server:
  ```bash
  Copy code
  uvicorn main:app --reload
