from flask import Flask, request, jsonify
import psycopg2

app = Flask (__name__)


def conectardb():
 pytops=psycopg2.connect(
 host="localhost",
 database="psql",
 user="u0_a322",
 password=""
 )
 return pytops


    



@app.route("/")
def hola():
 return "hola"

@app.route("/juegos",methods=["POST"])
def postear():
 new_game = request.get_json()
 game_name = new_game["nome"]
 price = float(new_game["preço"])
 impuesto = price * 0.16
 total = price + impuesto
 try:
  con = conectardb()
  cursor = con.cursor()

  sql ="INSERT INTO juegos (nombre,preço) VALUES (%s,%s)"
  cursor.execute(sql, (game_name,total))
  con.commit()
  cursor.close()
  con.close()
 except Exception as e:
  print(f"Erro ao salvar no banco de dados: {e}")


 
 return jsonify({
    "mensagem": f"Jogo {game_name} adicionado com sucesso",
    "preço": price,
    "iva": impuesto,
    "total a pagar": total
 })








if __name__ == "__main__":
 app.run(debug=True, port=8000)
