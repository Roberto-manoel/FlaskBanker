from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    # Return a response with a Portuguese greeting
    return 'Olá, mundo do back-end com Flask!'

# Run the development server if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)