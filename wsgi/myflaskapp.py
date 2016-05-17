from flask import Flask

from flask import Flask,request, send_from_directory
from flask import render_template
from flask import jsonify
#from flask.ext.cors import CORS

global registroAlunni
registroAlunni = { 0: {"numeroReg" : '0', "nome" : 'nome',
                "cognome" : 'cognome', "annoNascita"  : 'annoNascita'},
                  1: {"numeroReg" : '1', "nome" : 'nome',
                "cognome" : 'cognome', "annoNascita"  : 'annoNascita'},
                  2: {"numeroReg" : '2', "nome" : 'nome',
                "cognome" : 'cognome', "annoNascita"  : 'annoNascita'}}
    
        
        
        
    
app = Flask(__name__)
#CORS(app)

#global registroAlunni 
#registroAlunni = {}

@app.route("/")
def hello():
    return render_template( 'index.html')

@app.route("/test")
def test():
    return render_template( 'indexTest.html')

@app.route("/js/<nomeFileJs>")
def jsLoad(nomeFileJs):
    return send_from_directory('js', nomeFileJs)

@app.route("/css/<nomeFileCss>")
def cssLoad(nomeFileCss):
    return send_from_directory('css', nomeFileCss)
   
@app.route("/insertAlunno/")  # metodo GET per chiamare dalla barra del browser
def inserisciAlunno ():
    # spedizione in formato html
    numeroReg =  request.args.get('numeroReg')
    nome =       request.args.get('nome')
    cognome =    request.args.get('cognome')
    annoNascita =request.args.get('annoNascita') 
    dizAlunno = { "numeroReg": numeroReg, "nome": nome,
                  "cognome" : cognome , "annoNascita":annoNascita}
    
    
    global registroAlunni              
    registroAlunni[int(numeroReg)]= dizAlunno
    
    return "OK"   #restituisce status = 200  OK , ma nessuna stringa
    
    
@app.route("/alunnoByNumeroReg/", methods=["POST"]) # metodo POST
def alunnoByNumeroReg():
    # spedizione in formato html
    
    numeroReg =  request.json['numeroReg']
    
    global registroAlunni
    #calcola il max numeroReg presente nel dizionario
    # se la richeista eccede il numero manda lo zero
    max = 0
    for key in registroAlunni:
        if key > max:
            max = key
            
    if int(numeroReg) < max:        
        dizAlunno = registroAlunni[int(numeroReg)]
    else:
        dizAlunno = registroAlunni[0]
    # in casi piu' complessi usare render_templates e quindi jsonify
    stringJson = jsonify( ** dizAlunno)
    return stringJson   #aggiunge content-type => json

@app.route("/insertAlunnoPOST/", methods = ["POST"])
def inserisciAlunnoPOST():
    
    numeroReg =     request.json['numeroReg']
    nome =          request.json['nome']
    cognome =       request.json['cognome']
    annoNascita =   request.json['annoNascita']
    
    dizAlunno = {"numeroReg" : numeroReg, "nome" : nome, 
                "cognome" : cognome, "annoNascita"  : annoNascita}
    
    global registroAlunni
    registroAlunni[int(numeroReg)]= dizAlunno
    print dizAlunno
    print registroAlunni[int(numeroReg)]
    return jsonify("")
    
if __name__ == "__main__":
    #app.debug=True
    app.run(debug=True, port=6501)
