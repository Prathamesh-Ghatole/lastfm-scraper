from flask import Flask, render_template, request, send_file, redirect
from numpy import False_
import lib.auth as auth
import lib.lastfm as lastfm
from time import sleep

app = Flask(__name__)
_ = auth.init()

@app.route("/#home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    lastfm.initCache()
    # config = auth.init()

    if request.method == "POST":
        
        username = request.form["Username"]
        type = request.form["file_type"].lower()
        file_name = username + "." + type
        
        return render_template("base.html", file_name = file_name, dl_flag = True, complete_flag = False)
        # return redirect(f"/download/{file_name}")

    return render_template("base.html", dl_flag = False, complete_flag = False)

def generate_download(file_name):
    # Initialize default config
    config = auth.init()

    # Set config object's username based on file_name
    config.username = file_name.split(".")[0]
    config.type = file_name.split(".")[1]

    print(f"Fetching Scrobbles for {config.username}: ")
    scrobbles = lastfm.grab(config)

    lastfm.export(
        cleaned_df = scrobbles, 
        username = config.username, 
        type = config.type
        )

    print("Done!\n")

    return f'exports/{file_name}'

@app.route("/download/<file_name>")
def download(file_name):
    dl_path = generate_download(file_name)
    return render_template("base.html", file_name = file_name, dl_flag = False, complete_flag = True)

@app.route("/send/<file_name>/")
def send(file_name):
    sleep(0.2)
    return send_file(f'exports/{file_name}', as_attachment = True)


#################
if(__name__ == "__main__"):
    app.run(debug = True, host='127.0.0.1', port=6969)
