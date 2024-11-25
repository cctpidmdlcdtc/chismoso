from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    item_id = request.form['id']
    data[item_id] = {'id': item_id, 'name': request.form['name']}
    return jsonify(data[item_id])

@app.route('/update', methods=['POST'])
def update():
    item_id = request.form['id']
    if item_id in data:
        data[item_id]['name'] = request.form['name']
        return jsonify(data[item_id])
    return jsonify({'error': 'Item not found'}), 404

@app.route('/read', methods=['GET'])
def read():
    item_id = request.args.get('id')
    return jsonify(data.get(item_id, {}))

@app.route('/delete', methods=['POST'])
def delete():
    item_id = request.form['id']
    if item_id in data:
        del data[item_id]
        return jsonify({}), 204
    return jsonify({'error': 'Item not found'}), 404

@app.route('/all', methods=['GET'])
def show_all():
    return jsonify(data)

if __name__ == '__main__':
    app.run()
