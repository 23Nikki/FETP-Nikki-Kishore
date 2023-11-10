from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_dance.contrib.google import make_google_blueprint, google
import requests

app = Flask(__name__, template_folder="templates")
app.secret_key = "Bittu@2017"

google_bp = make_google_blueprint(client_id="229741477131-jnup9b513evj2a1584tidbs5jnoiqcrr.apps.googleusercontent.com", client_secret="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", redirect_to='google_login')
app.register_blueprint(google_bp, url_prefix='/google_login')

def requires_auth(f):
    def decorated(*args, **kwargs):
        if not google.authorized:
            return redirect(url_for('google.login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requires_auth
def home():
    user_name = "Nikki Kishore"
    user_email = "kishorenikki2014@gmail.com"

    # Get current Indian time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = requests.get('https://www.googleapis.com/plus/v1/people/me?key='+ AIzaSyCBPsy5c7rxf-Pc8uAvQqjUjH-E2xqzuRs)
    if response.status.code==200:
     user_info = response.json()
     user_name = user_info.get("displayName", user_name)
     user_email = user_info.get("email" , user_email)

    return render_template('home.html', user_name=user_name, user_email=user_email, current_time=current_time)

@app.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)