# LinkedIn to Resume Converter

This web application converts a LinkedIn profile PDF into an HTML resume using OpenAI's GPT-3.5 model.

## Approach

1. **Backend**: We use Flask, a lightweight Python web framework, to handle file uploads and API requests.
2. **PDF Processing**: PyPDF2 is used to extract text from the uploaded LinkedIn PDF.
3. **Resume Generation**: We use OpenAI's GPT-3.5 model to convert the extracted LinkedIn profile information into an HTML resume.
4. **Frontend**: A simple HTML form is used for file upload and API key input.

## Requirements

- Python 3.7+
- Flask
- PyPDF2
- openai
- python-dotenv

## Setup and Running

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/linkedin-to-resume.git
   cd linkedin-to-resume
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Open a web browser and go to `http://localhost:5000`

5. Enter your OpenAI API key and upload a LinkedIn PDF to generate the resume.

## Deployment on GitHub Pages

To deploy this application on GitHub Pages:

1. Create a new repository on GitHub.

2. Push your code to the repository:
   ```
   git remote add origin https://github.com/yourusername/linkedin-to-resume.git
   git branch -M main
   git push -u origin main
   ```

3. Go to your repository settings on GitHub.

4. Scroll down to the "GitHub Pages" section.

5. Select the branch you want to deploy (usually `main`).

6. Choose the `/docs` folder as the source.

7. Click "Save".

Your application will now be available at `https://yourusername.github.io/linkedin-to-resume`.

Note: Since GitHub Pages only serves static content, you'll need to modify the application to run entirely in the browser using JavaScript for PDF processing and API calls. This may require significant changes to the current Python-based implementation.

## Future Improvements

- Add error handling and input validation
- Implement user authentication for API key management
- Add options for different resume styles
- Integrate with LinkedIn API for direct profile fetching (requires LinkedIn Developer approval)

## License

This project is licensed under the MIT License.