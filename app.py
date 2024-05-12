from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filter')
def filter_questions():
    difficulty = request.args.get('difficulty', '')
    tags = request.args.get('tags', '').split(',')
    with open('questions.json', 'r') as file:
        questions = json.load(file)
        filtered_questions = [
            q for q in questions if
            (difficulty.lower() == q['difficulty_level'].lower() if difficulty else True) and
            (any(tag.lower() in [t.lower() for t in q['tags']] for tag in tags) if tags[0] else True)
        ]
    return jsonify(filtered_questions)

if __name__ == "__main__":
    app.run(debug=True)
