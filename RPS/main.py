from flask import Flask, render_template, request, flash, session
import random
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    session.clear()
    session['my_score'] = 0
    session['comp_score'] = 0
    return render_template('index.html')

@app.route('/start', methods = ['GET', 'POST'])
def start():
    if request.method == 'POST':
        rock_selected = 'rock' in request.form
        paper_selected = 'paper' in request.form
        scissor_selected = 'scissor' in request.form
        if rock_selected:
            session['selected'] = 'rock'
        if paper_selected:
            session['selected'] = 'paper'
        if scissor_selected:
            session['selected'] = 'scissor'
        my_choice = session['selected']
        ran_num = random.randint(1, 4)
        if ran_num == 1:
            pic = "paper"
        elif ran_num == 2:
            pic = "rock"
        else:
            pic = "scissor"
        if my_choice == 'rock':
            if pic == 'scissor':
                session['my_score'] += 1
                flash("you won...!")
            elif pic == 'paper':
                session['comp_score'] += 1
                flash("computer won...!")
        elif my_choice == 'paper':
            if pic == 'scissor':
                session['comp_score'] += 1
                flash("computer won...!")
            elif pic == 'rock':
                session['my_score'] += 1
                flash("you won...!")
        elif my_choice == 'scissor':
            if pic == 'rock':
                session['comp_score'] += 1
                flash("computer won...!")
            elif pic == 'paper':
                session['my_score'] += 1
                flash("you won...!")
        my_score = session['my_score']
        comp_score = session['comp_score']
        return render_template('start1.html', my_choice=my_choice, pic=pic, my_score=my_score, comp_score=comp_score)
    return render_template('start.html')


@app.route('/start1', methods = ['GET', 'POST'])
def start1():
    return render_template('start1.html')


if __name__ == "__main__":
    app.run(debug=True)
