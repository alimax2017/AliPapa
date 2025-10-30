from flask import Flask, render_template

app = Flask(__name__)

# Données fictives de meubles
meubles = [
    {
        "id": 1,
        "nom": "Canapé en cuir",
        "prix": 799,
        "image": "images/meuble1.jpg",
        "description": "Un canapé en cuir véritable, design et confortable."
    },
    {
        "id": 2,
        "nom": "Table en chêne massif",
        "prix": 499,
        "image": "images/meuble2.jpg",
        "description": "Table artisanale en bois de chêne naturel."
    },
    {
        "id": 3,
        "nom": "Chaise scandinave",
        "prix": 129,
        "image": "images/meuble3.jpg",
        "description": "Chaise élégante et moderne au style nordique."
    }
]

@app.route('/')
def accueil():
    return render_template('index.html', meubles=meubles)

if __name__ == '__main__':
    app.run(debug=True)
