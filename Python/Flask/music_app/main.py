from flask import Flask

outPutPath = './'
app = Flask(__name__, static_folder=outPutPath)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

if __name__ == '__main__':
    app.run()