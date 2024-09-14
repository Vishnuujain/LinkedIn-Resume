import os
import tempfile
from flask import Flask, request, render_template, send_file
import PyPDF2
import openai
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the OpenAI API key from the form
        api_key = request.form['api_key']
        openai.api_key = api_key

        # Get the uploaded PDF file
        pdf_file = request.files['pdf_file']
        
        # Read the PDF content
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

        # Use OpenAI to generate HTML resume
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that converts LinkedIn profile information into an HTML resume."},
                {"role": "user", "content": f"Convert the following LinkedIn profile information into an HTML resume. Use modern, responsive design with CSS. Make it visually appealing and professional: {pdf_text}"}
            ]
        )

        html_resume = response.choices[0].message.content

        # Save the HTML resume to a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as temp_file:
            temp_file.write(html_resume)
            temp_file_path = temp_file.name

        return send_file(temp_file_path, as_attachment=True, download_name='resume.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)