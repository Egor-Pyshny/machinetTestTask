import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from machinettesttask import generate_random_file_name

app = Flask(__name__)
socketio = SocketIO(app, max_http_buffer_size=1024 * 1024 * 5)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


@socketio.on("file_upload")
def handle_file_upload(data):
    file_name = generate_random_file_name()
    while os.path.exists(file_name):
        file_name = generate_random_file_name()
    with open(f"files\\{file_name}", "w") as file:
        try:
            for d in data:
                filename: str = d["name"]
                file_req = d["request"]
                if not filename.endswith(".md") and not filename.endswith(".txt"):
                    emit(
                        "file_upload_status",
                        {
                            "message": f"File {filename} "
                            f"have incorrect extension REQUEST NUM {file_req}"
                        },
                    )
                    continue
                file_content = d["fileData"]
                file.write(file_content)
                file.write("\n<file-separator>\n")
                emit(
                    "file_upload_status",
                    {"message": f"File {filename} uploaded REQUEST NUM {file_req}"},
                )
        except Exception as e:
            emit(
                "file_upload_status",
                {"message": f"Error during handling {filename}, {e.args[0]}"},
            )


if __name__ == "__main__":
    directory_path = f"{os.path.abspath('.')}\\files"
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        os.makedirs(directory_path)
    if not os.path.exists(directory_path+".gitignore"):
        with open('files\\.gitignore', 'w') as gitignore_file:
            gitignore_file.write("*\n!.gitignore")
    socketio.run(app, allow_unsafe_werkzeug=True)
