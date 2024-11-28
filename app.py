from flask import Flask, render_template, request, redirect, url_for, jsonify
import api

app = Flask(__name__)

@app.route("/")
@app.route("/projects")
def index():
    projects = api.get_projects()
    return render_template("list_projects.html", projects=projects)

@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        api.add_project(name, description)
        return redirect(url_for("index"))
    return render_template("add_project.html")

@app.route("/update_project/<int:project_id>", methods=["GET", "POST"])
def update_project(project_id):
    project = api.get_project(project_id)
    if not project:
        return "Project not found", 404
    workers = api.get_workers()  # Obtener la lista de trabajadores para el selector.
    if not workers:
        return "No workers found", 404
    roles = api.get_roles()  # Obtener la lista de roles para el selector.
    if not roles:
        return "No roles found", 404
    if request.method == "POST":
        if 'update_project' in request.form:
            name = request.form["name"]
            description = request.form["description"]
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]
            api.update_project(project_id, name, description, start_date, end_date)
            return redirect(url_for("index"))
        else:
            worker = request.form["worker"]
            role = request.form["role"]
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]
            #api.register_hours(worker, project, role, start_date, 0.5) # availability_percentageeeeeeeeeeee
            #api.register_hours(worker, project, role, end_date, 0.5) # availability_percentageeeeeeeeeeee
            #return redirect(url_for("index"))
            return f"{worker}, {role}, {start_date}, {end_date}"
    return render_template("update_project.html", project=project, workers=workers, roles=roles)

@app.route("/delete_project/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    api.delete_project(project_id)
    return redirect(url_for("index"))


@app.route("/workers")
def index_workers():
    workers = api.get_workers()
    return render_template("list_workers.html", workers=workers)

@app.route("/add_worker", methods=["GET", "POST"])
def add_worker():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        api.add_worker(name, description)
        return redirect(url_for("index_workers"))
    return render_template("add_worker.html")

@app.route("/update_worker/<int:worker_id>", methods=["GET", "POST"])
def update_worker(worker_id):
    worker = api.get_worker(worker_id)
    if not worker:
        return "Worker not found", 404
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        api.update_worker(worker_id, name, description)
        return redirect(url_for("index_workers"))
    return render_template("update_worker.html", worker=worker)

@app.route("/delete_worker/<int:worker_id>", methods=["POST"])
def delete_worker(worker_id):
    api.delete_worker(worker_id)
    return redirect(url_for("index_workers"))

@app.route('/calendar_events')
def calendar_events():
    workers_working = api.calendar_events()

    # Convertimos los datos a formato de eventos para FullCalendar
    events = [
        {
            "title": f"{row['project']} - {row['role']} - {row['worker']} {row['worked_hours']}h",
            "start": row['date'],  # Fecha de inicio
            "allDay": False   # Para asegurar que no es un evento de todo el día
        }
        for row in workers_working
    ]
    return jsonify(events)

@app.route('/calendar_view')
def calendar_view():
    return render_template("calendar.html")


if __name__ == "__main__":
    app.run(debug=True)
