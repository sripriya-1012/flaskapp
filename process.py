from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'jnguntgjiwuigjrg' # Add a secret key for flashing messages

@app.route('/')
def form():
    return render_template('bot-1.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['Name']
    message = request.form['Message']
    with open('C:/Users/SriPriya/Bots 11/form_data.txt', 'a') as f:
        f.write(f'{name} - {message}\n')
    flash('Form submitted successfully!', 'success') # Flash the success message
    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
