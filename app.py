from flask import Flask, render_template, request, redirect, url_for
import api

app = Flask(__name__)

@app.route("/")
def index():
    items = api.get_projects()
    return render_template("index.html", items=items)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        api.add_project(name, description)
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/update/<int:project_id>", methods=["GET", "POST"])
def update(project_id):
    item = api.get_project(project_id)
    if not item:
        return "Item not found", 404
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        api.update_project(project_id, name, description)
        return redirect(url_for("index"))
    return render_template("update.html", item=item)

@app.route("/delete/<int:project_id>", methods=["POST"])
def delete(project_id):
    api.delete_project(project_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
