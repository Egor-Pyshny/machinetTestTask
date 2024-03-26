from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from machinettesttask import error_handler, generate_random_file_name

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


@error_handler
@socketio.on("file_upload")
def handle_file_upload(data):
    with open("files\\" + generate_random_file_name(), "w") as file:
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


if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)
