from flask import Flask, render_template, request, send_file
import os
import subprocess

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)  # Create folder if it doesn't exist

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")  # Get YouTube URL from form
        if not url:
            return "No URL provided", 400

        # Command to download video
        command = f"yt-dlp -o '{DOWNLOAD_FOLDER}/%(title)s.%(ext)s' {url}"
        subprocess.run(command, shell=True)

        # Get the latest downloaded file
        files = sorted(os.listdir(DOWNLOAD_FOLDER), key=lambda x: os.path.getctime(os.path.join(DOWNLOAD_FOLDER, x)), reverse=True)
        if files:
            return send_file(os.path.join(DOWNLOAD_FOLDER, files[0]), as_attachment=True)

    return render_template("index.html")  # Show download form

if __name__ == "__main__":
    app.run(debug=True)
