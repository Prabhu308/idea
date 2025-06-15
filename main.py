from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Simple Static Website</title>
        <style>
            /* Modern, clean styling with colors and spacing */
            body {
                background: linear-gradient(135deg, #7c3aed, #06b6d4);
                color: #f0f9ff;
                font-family: 'Poppins', Arial, sans-serif;
                margin: 0;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: 2rem;
                box-sizing: border-box;
            }
            h1 {
                font-size: 3.5rem;
                margin-bottom: 1rem;
                text-shadow: 0 3px 6px rgba(0,0,0,0.3);
            }
            p {
                font-size: 1.25rem;
                max-width: 600px;
                line-height: 1.6;
                color: #dbeafe;
                text-shadow: 0 2px 4px rgba(0,0,0,0.25);
            }
            /* Button style */
            a.button {
                margin-top: 2rem;
                padding: 0.75rem 1.5rem;
                background: linear-gradient(135deg, #4ade80, #22c55e);
                color: white;
                text-decoration: none;
                font-weight: 600;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(34, 197, 94, 0.4);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                display: inline-block;
            }
            a.button:hover, a.button:focus {
                transform: translateY(-3px);
                box-shadow: 0 12px 30px rgba(34, 197, 94, 0.6);
            }
            @media (max-width: 640px) {
                h1 {
                    font-size: 2.5rem;
                }
                p {
                    font-size: 1rem;
                }
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Simple Static Flask Website!</h1>
        <p>This is a static page served directly from the Flask route without using templates.</p>
        <a href="https://flask.palletsprojects.com/" class="button" target="_blank" rel="noopener noreferrer">Learn More About Flask</a>
    </body>
    </html>
    """
    return Response(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

