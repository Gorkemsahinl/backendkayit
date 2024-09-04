from flask import Flask , request , jsonify ,render_template



app = Flask(__name__)



@app.route('/kayit' , methods=['POST'] )

def kayit():

  try:

         data = request.get_json()
         isim = data.get('İsim')
         soyisim = data.get('Soyisim')
         email = data.get('email')
         telno = data.get('telefon numarası')
        
         with open('kayitlar.txt', 'a') as file:
            file.write(f'{isim}, {soyisim}, {email}, {telno}\n')
         return jsonify({"message": "Kayıt oldun"})
  except Exception as e:
        return jsonify({"error": str(e)})
  
@app.route('/kayitgetir' , methods=['GET'] )

def kayitgetir():
 
  try:

        with open('kayitlar.txt', 'r') as file:
         content = file.read()
        return jsonify({"content": content})
  except Exception as e:
        return jsonify({"error": str(e)})



if __name__ == '__main__':
    app.run(debug=True)