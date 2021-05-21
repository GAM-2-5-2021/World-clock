from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #dodaje glavnu rutu koja ce se loadoat pri otvaranju stranice
def main():
    return render_template('index.html') #funkcija vraca galvni html file

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80) #stavlja ip za host-a i odreduje port te pokrece stranicu(aplikaciju)