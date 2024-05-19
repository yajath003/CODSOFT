from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    res = ''
    if request.method == 'POST':
        res = request.form.get('res', '')
        hel = request.form.get('val')

        if hel == 'C':
            res = ''
        elif hel == '=':
            try:
                res = str(eval(res))
            except:
                res = 'Error'
        else:
            res += hel
    return render_template('index.html', res=res)

if __name__ == "__main__":
    app.run(debug=True)
