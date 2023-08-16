from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run-bot', methods=['GET'])
def run_bot():
    # This is where our robot would do its trading. For now, it just says it did.
    return jsonify({'message': 'Toy robot did a pretend trade!'})

# This line will make our robot's playground run and ready to play!
app.run(port=5000)
