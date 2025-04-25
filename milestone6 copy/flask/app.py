from flask import Flask, send_from_directory, render_template, request, send_file
from pixelate import pixelate_image
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')

@app.route('/ai-info')
def ai_info():
    return render_template('ai-info.html')

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.abspath(os.path.dirname(__file__) + '/../'), filename)

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            pixelated_img = pixelate_image(file.stream)
            return send_file(
                pixelated_img,
                mimetype='image/png',
                download_name='pixelated.png',
                as_attachment=True
            )
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)
