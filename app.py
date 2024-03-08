from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    try:
        # Save the uploaded image
        img = Image.open(file)
        img.save('uploaded_image.png')
    
        # Use Tesseract to extract text
        extracted_text = pytesseract.image_to_string(img)

        return render_template('index.html', extracted_text=extracted_text, image_path='uploaded_image.png')

    except Exception as e:
        return render_template('index.html', error=f'Error processing the image: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)