from flask import Flask, render_template, request, redirect, url_for
import api

app = Flask(__name__)

@app.route("/")
@app.route("/projects")
def index():
    items = api.get_projects()
    return render_template("list_projects.html", items=items)

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
    item = api.get_project(project_id)
    if not item:
        return "Item not found", 404
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        api.update_project(project_id, name, description)
        return redirect(url_for("index"))
    return render_template("update_project.html", item=item)

@app.route("/delete_project/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    api.delete_project(project_id)
    return redirect(url_for("index"))


@app.route("/workers")
def index_workers():
    items = api.get_workers()
    return render_template("list_workers.html", items=items)

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
    item = api.get_worker(worker_id)
    if not item:
        return "Item not found", 404
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        api.update_worker(worker_id, name, description)
        return redirect(url_for("index_workers"))
    return render_template("update_worker.html", item=item)

@app.route("/delete_worker/<int:worker_id>", methods=["POST"])
def delete_worker(worker_id):
    api.delete_worker(worker_id)
    return redirect(url_for("index_workers"))


if __name__ == "__main__":
    app.run(debug=True)
