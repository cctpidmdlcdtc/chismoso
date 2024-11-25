import sqlite3

DB_PATH = "projects.db"  # Database file path

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enables dictionary-like access to rows
    return conn

def initialize_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Create tables if they do not exist
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS Projects (
                project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS Workers (
                worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                max_daily_hours INTEGER DEFAULT 8,
                max_weekly_hours INTEGER DEFAULT 40
            );
            CREATE TABLE IF NOT EXISTS Roles (
                role_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
            CREATE TABLE IF NOT EXISTS Worker_Hours (
                hours_id INTEGER PRIMARY KEY AUTOINCREMENT,
                worker_id INTEGER,
                project_id INTEGER,
                role_id INTEGER,
                date DATE NOT NULL,
                availability_percentage DECIMAL(3, 2) DEFAULT 1.0,
                FOREIGN KEY (worker_id) REFERENCES Workers(worker_id),
                FOREIGN KEY (project_id) REFERENCES Projects(project_id),
                FOREIGN KEY (role_id) REFERENCES Roles(role_id),
                UNIQUE (worker_id, project_id, role_id, date)
            );
        """)
        conn.commit()

def populate_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Insert initial content
        cursor.executescript("""

            -- Insert a few projects
            INSERT INTO Projects (name) VALUES ('Nieve');
            INSERT INTO Projects (name) VALUES ('Playa');
            INSERT INTO Projects (name) VALUES ('Coche');
            INSERT INTO Projects (name) VALUES ('Casa');

            -- Insert workers
            INSERT INTO Workers (name) VALUES ('Anselmo');
            INSERT INTO Workers (name) VALUES ('Baldomero');
            INSERT INTO Workers (name) VALUES ('Clodomiro');
            INSERT INTO Workers (name) VALUES ('Doroteo');

            -- Insert managers
            INSERT INTO Workers (name) VALUES ('Plácido');
            INSERT INTO Workers (name) VALUES ('Olegario');

            -- Insert initial roles
            INSERT INTO Roles (name) VALUES 
            ('Technician'), 
            ('Project Manager'),
            ('Consultant'),
            ('Developer'),
            ('Account Manager');

            -- Record hours worked
            -- 2024-11-20
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 1, 3, '2024-11-20', 0.5);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 2, 3, '2024-11-20', 0.5);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (1, 3, 3, '2024-11-20', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (3, 4, 3, '2024-11-20', 0.5);

            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 1, 2, '2024-11-20', 0.25);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 2, 2, '2024-11-20', 0.25);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 3, 2, '2024-11-20', 0.25);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 4, 2, '2024-11-20', 0.25);

            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (5, 1, 5, '2024-11-20', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (5, 2, 5, '2024-11-20', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (5, 3, 5, '2024-11-20', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (5, 4, 5, '2024-11-20', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (6, 4, 5, '2024-11-20', 1);

            -- 2024-11-21
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 1, 3, '2024-11-21', 0.5);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 2, 3, '2024-11-21', 0.5);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (1, 3, 3, '2024-11-21', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (3, 4, 3, '2024-11-21', 0.5);

            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 1, 2, '2024-11-21', 0.25);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 2, 2, '2024-11-21', 0.25);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 3, 2, '2024-11-21', 0.25);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (4, 4, 2, '2024-11-21', 0.25);

            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (5, 1, 5, '2024-11-21', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (5, 2, 5, '2024-11-21', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (5, 3, 5, '2024-11-21', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (5, 4, 5, '2024-11-21', 1);
            INSERT INTO Worker_Hours (worker_id, project_id, role_id, date, availability_percentage) VALUES (6, 4, 5, '2024-11-21', 1);

        """)
        conn.commit()
