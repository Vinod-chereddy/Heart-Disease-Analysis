from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve index.html
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Serve images folder
@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=True)
