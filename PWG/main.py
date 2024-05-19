from flask import Flask, render_template,request, redirect, url_for
import random, string
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        ascii_char = list(string.printable)
        result = ''
        for i in range(1,number+1):
            a = random.choice(ascii_char)
            result+=a
        print(result)
        return render_template('index.html', result = result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
