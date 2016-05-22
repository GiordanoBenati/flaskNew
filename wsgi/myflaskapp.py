from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import send_from_directory
import sqlite3
        
        
        
app = Flask(__name__)


def initDB():
    # crea le tabelle del DB se non esistono
    conn = sqlite3.connect('/data/Alunni.db')

    stringSQLTableAlunni = \
        "create table registroAlunni  if not exists(\
            numeroReg integer primary key,\
            nome      text not null,\
            cognome   text not null,\
            annoNascita text not null,\
        );"
    conn.execute(stringSQLTableAlunni)
    conn.close()

initDB()


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('indexTest.html')


@app.route("/insertAlunno/")  # metodo GET per chiamare dalla barra del browser
def inserisciAlunno ():
    # spedizione in formato html
    numeroReg   =   request.args.get('numeroReg')
    nome        =   request.args.get('nome')
    cognome     =   request.args.get('cognome')
    annoNascita =   request.args.get('annoNascita') 
    
    
    '''  inserire nel db '''
    
    
    return "OK"   #restituisce status = 200  OK , ma nessuna stringa
    
    
@app.route("/alunnoByNumeroReg/", methods=["POST"]) # metodo POST
def alunnoByNumeroReg():
    # spedizione in formato html
    
    numeroReg = request.json['numeroReg']
    
        #apre connessione al DB per inserire un Alunno
    
    conn = sqlite3.connect('/data/Alunni.db')
    print "Opened database successfully";
    cursor = conn.execute("SELECT * FROM registroAlunni  WHERE NUMEROREG == ? ",numeroReg);
    conn.close()
    
    # in questo caso e' atteso un solo elemento o nessuno: cursor e' una lista
    # di liste, ogni elemento e' una lista di valori corrispondenti alle chiavi
    # di un dizionario numeroReg | nome | cognome | annoNascita
    dizAlunno = {}
    for alunno in cursor:
        numeroReg   =   alunno[0]
        nome        =   alunno[1]
        cognome     =   alunno[2]
        annoNascita =   alunno[3]
        
        dizAlunno = {"numeroReg": numeroReg, "nome": nome,
        "cognome": cognome, "annoNascita":annoNascita}
        break  #  al max un solo elemento viene letto
    
    # dizAluuno o e' diz vuoto oppure e' un solo elemento
    
    # in casi piu' complessi usare render_templates e quindi jsonify
    stringJson = jsonify(** dizAlunno)
    return stringJson   #aggiunge content-type => json

@app.route("/insertAlunnoPOST/", methods=["POST"])
def inserisciAlunnoPOST():
    
    numeroReg   =   request.json['numeroReg']
    nome        =   request.json['nome']
    cognome     =   request.json['cognome']
    annoNascita =   request.json['annoNascita']
    
    
    #apre connessione al DB per inserire un Alunno
    
    conn = sqlite3.connect('/data/Alunni.db')
    print "Opened database successfully";
    conn.execute("INSERT INTO registroAlunni \
        (NUMEROREG,NOME,COGNOME,ANNONASCITA) \
        VALUES (numeroReg,nome,cognome,annoNascita)");
    conn.close()
    
    

return jsonify("")
    
if __name__ == "__main__":
    #app.debug=True
    app.run(debug=True)
