from flask import Flask, request, send_from_directory, abort
import os

app = Flask(__name__)
base_html_folder = 'html'

@app.route('/html/redirection-new.php', methods=['GET'])
def get_html_file():
    url = request.args.get('URL')
    name = request.args.get('NAME')
    if not url or not name:
        abort(400, "URL and NAME parameters are required")

    filename = f"redirection-new.php?URL={url}&NAME={name}"
    file_path = os.path.join(base_html_folder, filename)

    if os.path.exists(file_path):
        return send_from_directory(base_html_folder, filename)
    else:
        abort(404, f"File not found: {filename}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)