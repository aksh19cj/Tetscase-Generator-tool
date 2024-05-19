from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Implement your login logic here
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup')
def signup():
    # Implement your SSO signup logic here
    return redirect(url_for('dashboard'))

@app.route('/signup_page', methods=['GET', 'POST'])  # Update route definition to support GET and POST methods
def signup_page():
    if request.method == 'POST':
        # Process signup form submission
        # Implement your signup logic here
        return redirect(url_for('dashboard'))  # Redirect to dashboard after successful signup
    else:
        # Render signup form template for GET requests
        return render_template('signup.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    programs = ['CNX', 'CN', 'CX', 'PVOS']
    if request.method == 'POST':
        # Process user input from the chatbox and generate testcases
        user_input = request.form['user_input']
        # Implement logic to generate testcases based on user input
        # For now, let's just print the user input
        print("User input:", user_input)
    return render_template('dashboard.html', programs=programs)

if __name__ == '__main__':
    app.run(debug=True)
