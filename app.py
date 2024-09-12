from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

categories = [
    {"catid": 1, "desc": "meat"},
    {"catid": 2, "desc": "dairyyyyyyyyy"},
    {"catid": 3, "desc": "bakery"},
    {"catid": 4, "desc": "something"}
]

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/categories')
def get_categories():
    return jsonify(categories)

# New route to handle the selected category
@app.route('/selected/<int:catid>')
def selected_category(catid):
    category = next((cat for cat in categories if cat['catid'] == catid), None)
    if category:
        print(f"Selected Category ID: {catid}")
        return jsonify({"message": f"Category {catid} selected", "category": category})
    else:
        return jsonify({"message": "Category not found"}), 404

@app.route('/test')
def test():
    return 'Hello, test!'

if __name__ == '__main__':
    app.run(debug=True)
