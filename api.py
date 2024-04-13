from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    """Returns a greeting message in Portuguese."""
    return 'Olá, mundo do back-end com Flask!'

# Define a route for personalized greetings with a name parameter
@app.route('/saudacao/<nome>', methods=['GET'])
def saudacao(nome):
    """Returns a personalized greeting message with the provided name.

    Args:
        nome (str): The name to be used in the greeting.

    Returns:
        str: A personalized greeting message.
    """
    return f'Olá, {nome}! Bem-vindo ao nosso serviço de API!'

# Run the development server if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)