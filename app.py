from flask import Flask, render_template, request, send_from_directory
import os
import subprocess

app = Flask(__name__)

OUTPUT_FOLDER = "output_images"
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_url = request.form['image_url']
        process_image(image_url)
    return render_template('index.html')

def process_image(url):
    output_path = os.path.join(OUTPUT_FOLDER, "output.png")
    cmd = f"curl -s {url} | rembg i > {output_path}"
    subprocess.run(cmd, shell=True)

@app.route('/output')
def output():
    return send_from_directory(OUTPUT_FOLDER, "output.png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
