from flask import Flask, render_template
#mostre dentro do import o comando ,render_template - trazer templates ja salvos

#a variavel a baixo é a variavel 
#que roda a aplicação (todos os objetos de programação dependem dela)
app = Flask(__name__)

#rota

@app.route('/')
def ola():
    return "<h1>iniciando flask<h1>"

@app.route("/lista")
def lista():
    return render_template("lista.html")





app.run()

#nome 
#marca 
#preço
