from flask import Flask, render_template, request
import bitly_api
app = Flask(__name__)

bitly_access_token = "d0d5d8b5e8da855f2472345e2920c1957ea83358"

@app.route("/", methods=['POST', 'GET'])
def home():
  if request.method=="POST":
    url_received = request.form["url"]
    bitly = bitly_api.Connection(access_token=bitly_access_token)
    short_url = bitly.shorten(url_received)
    return render_template("form.html", new_url=short_url.get('url'), old_url=url_received)
  else:
    return render_template('form.html')

if __name__ == "__main__":
  app.run() 
