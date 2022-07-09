from flask import Flask
import image_processing as imagem

app = Flask(__name__)

@app.route('/')
def hello_world():

    return app.response_class(
        response="Up",
        status=200,
        mimetype="application/json"     
    )

@app.route('/hiperDCR', methods=["POST", "GET"])
def validar_campo():

    print("teste")
    response = imagem.Image_processing.pdf2png_crop()

    return str(response["resultadoDaComparacao"])

if __name__ == '__main__':
    app.run(debug=True)