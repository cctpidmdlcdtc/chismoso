import hug
from database import get_db_connection, initialize_db, populate_db

# Initialize the database
initialize_db()

# Initial data load; ideally, replace with a backup restore reading a SQL file with inserts
@hug.get('/initial_load')
def initial_load():
    populate_db()

# CRUD for Projects
@hug.get('/projects')
def get_projects():
    """Retrieves all projects"""
    with get_db_connection() as conn:
        projects = conn.execute("SELECT * FROM Projects").fetchall()
        return [dict(project) for project in projects]

@hug.get('/project/{project_id}')
def get_project(project_id: int):
    """Retrieves a project by its ID"""
    with get_db_connection() as conn:
        project = conn.execute("SELECT * FROM Projects WHERE project_id = ?", (project_id,)).fetchone()
        return dict(project)

@hug.post('/projects')
def add_project(name: str):
    """Adds a new project"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Projects (name) VALUES (?)", (name,))
        conn.commit()
        return {"project_id": cursor.lastrowid, "name": name}

@hug.put('/projects/{project_id}')
def update_project(project_id: int, name: str):
    """Updates an existing project"""
    with get_db_connection() as conn:
        conn.execute("UPDATE Projects SET name = ? WHERE project_id = ?", (name, project_id))
        conn.commit()
        return {"status": "project updated", "project_id": project_id, "name": name}

@hug.delete('/projects/{project_id}')
def delete_project(project_id: int):
    """Deletes a project"""
    with get_db_connection() as conn:
        conn.execute("DELETE FROM Projects WHERE project_id = ?", (project_id,))
        conn.commit()
        return {"status": "project deleted", "project_id": project_id}

# CRUD for workers
@hug.get('/workers')
def get_workers():
    """Retrieves all workers"""
    with get_db_connection() as conn:
        workers = conn.execute("SELECT * FROM workers").fetchall()
        return [dict(worker) for worker in workers]

@hug.get('/workers/{worker_id}')
def get_worker(worker_id: int):
    """Retrieves a worker by their ID"""
    with get_db_connection() as conn:
        worker = conn.execute("SELECT * FROM workers WHERE worker_id = ?", (worker_id,)).fetchone()
        return dict(worker)

@hug.post('/workers')
def add_worker(name: str, max_daily_hours: int = 8, max_weekly_hours: int = 40):
    """Adds a new worker"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO workers (name, max_daily_hours, max_weekly_hours) VALUES (?, ?, ?)",
            (name, max_daily_hours, max_weekly_hours),
        )
        conn.commit()
        return {"worker_id": cursor.lastrowid, "name": name}

@hug.put('/workers/{worker_id}')
def update_worker(worker_id: int, name: str = None, max_daily_hours: int = None, max_weekly_hours: int = None):
    """Updates a worker by their ID"""
    with get_db_connection() as conn:
        # Retrieve existing worker record
        worker = conn.execute("SELECT * FROM workers WHERE worker_id = ?", (worker_id,)).fetchone()
        
        # Update only provided fields
        fields = []
        values = []
        
        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if max_daily_hours is not None:
            fields.append("max_daily_hours = ?")
            values.append(max_daily_hours)
        if max_weekly_hours is not None:
            fields.append("max_weekly_hours = ?")
            values.append(max_weekly_hours)
        
        if fields:
            values.append(worker_id)
            conn.execute(f"UPDATE workers SET {', '.join(fields)} WHERE worker_id = ?", values)
            conn.commit()
        
        return {"success": True, "updated_fields": fields}

# worker Hours Registration
@hug.post('/worker_hours')
def register_hours(worker_id: int, project_id: int, role_id: int, date: str, availability_percentage: float = 1.0):
    """Registers hours worked"""
    with get_db_connection() as conn:
        try:
            conn.execute(
                "INSERT INTO worker_Hours (worker_id, project_id, id_role, date, availability_percentage) VALUES (?, ?, ?, ?, ?)",
                (worker_id, project_id, role_id, date, availability_percentage),
            )
            conn.commit()
            return {"status": "hours registered"}
        except sqlite3.IntegrityError as e:
            return {"error": str(e)}

@hug.get('/worker_hours')
def get_worker_hours():
    """Retrieves all registered hours"""
    with get_db_connection() as conn:
        hours = conn.execute("SELECT * FROM worker_Hours").fetchall()
        return [dict(hour) for hour in hours]