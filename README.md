# **Overview**
Your task is to create a web application using Flask that incorporates WebSocket technology
to accept file uploads from a client. The client will be a simple HTML+JavaScript one-pager
that can send files to the server. This project aims to test your skills in Python (Flask),
JavaScript, WebSocket communication, and file handling.

# **Objectives:**
- **Server Setup**: Create a Flask server that opens a WebSocket connection for
  communication with the client.
- **Client Creation**: Develop a simple HTML+JavaScript page capable of selecting up to 10
  files and sending them to the server through the WebSocket connection.
- **File Handling**: The server should only accept a maximum of 10 files in one WebSocket request.
Upon receiving files, the server must concatenate the content of these files and store the
result in a single .txt file. Each file's content should be separated by a clear delimiter (e.g., a
line of dashes ---------- or a specific tag <file-separator>).
- **Data Acceptance Confirmation**: Implement a mechanism where the client continuously
  sends data to the server and shows notification that all files were successfully uploaded and
  processed by the server.

# **Enhanced Requirements:**
- File Type Restriction: Ensure the server only accepts files of specific types (e.g., .txt, .md).
- Error Handling: Implement robust error handling on both the server and client to manage
  scenarios such as connection issues, file size limitations, and unsupported file types.
- Upload your code to github
