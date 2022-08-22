from flask import Flask, render_template, request
from datetime import datetime
from Utils.security import url_encrypt, url_decrypt
import requests
import socket
from Utils.database import Database

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def shortner():
    if request.method == "POST":
        time_stamp = datetime.now()

        if request.form['submit_button'] == 'submit_url':
            url = request.form.get("url_input")

            hostname = socket.gethostname()
            user_ip = socket.gethostbyname(hostname)

            url_id = url.split("/")[3].replace("watch?v=", '')

            # inserting into database
            data = {"_id": time_stamp,
                    "url": url_id,
                    "user_ip": user_ip
                    }

            result = requests.get(f"https://api.shrtco.de/v2/shorten?url={url}").json()
            shorten_url = result.get('result').get('full_short_link')

            # insertion query
            Database().insertion(data)

            return render_template("result.html", url=str(shorten_url), query_type="Short URL")

        elif request.form['submit_button'] == 'submit_encrypt':
            url = request.form.get("url_input")
            key = request.form.get("key_input")

            str_encoded = url_encrypt(url, key)

            return render_template("result.html", url=str(str_encoded), query_type="Encrypted URL")

        elif request.form['submit_button'] == 'submit_decrypt':
            url = request.form.get("url_input")
            key = request.form.get("key_input")

            str_decoded = url_decrypt(url, key)

            if str_decoded is False:
                str_decoded = "Invalid Credentials"

            return render_template("result.html", url=str(str_decoded), query_type="Decrypted URL")

    return render_template("index.html")


@app.route('/video', methods =["GET", "POST"])
def video():
    latest_url, entire_data = Database().search()
    return render_template("video.html", latest_url=latest_url)


@app.route('/track', methods =["GET", "POST"])
def track():
    latest_url, entire_data = Database().search()
    entire_data.reverse()
    return render_template('track.html', data=entire_data)


if __name__ == '__main__':
    app.run(debug=False)