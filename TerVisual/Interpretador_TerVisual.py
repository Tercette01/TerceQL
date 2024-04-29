from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Botão Flask</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            $(document).ready(function(){
                $("button").click(function(){
                    $.post("/button_press", function(){
                        alert("Botão pressionado!");
                    });
                });
            });
        </script>
    </head>
    <body>
        <button type="button">Clique aqui</button>
    </body>
    </html>
    '''

@app.route('/button_press', methods=['POST'])
def button_press():
    print("Botão pressionado!")
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
