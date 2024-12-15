from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for polling options and votes
poll_data = {
    'options': ["Маргарита", "Пепероні", "Гавайська", "Чотири сири"],
    'votes': [0, 0, 0, 0]  # Votes correspond to the options
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option:
            index = poll_data['options'].index(selected_option)
            poll_data['votes'][index] += 1
        return redirect(url_for('results'))
    return render_template('poll.html', options=poll_data['options'])

@app.route('/results')
def results():
    return render_template('results.html', poll_data=poll_data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=1234)