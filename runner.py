from flask import render_template, redirect, Flask, url_for, request
from bs4 import BeautifulSoup
import wget
import os
app = Flask(__name__)


@app.route("/")
def start():

    return render_template("Home.html")


@app.route("/serp", methods=['GET'])
def serp():
    search = request.args.get('q', None)
    u = search.replace(" ", "+")
    wget.download(f"https://www.info.com/serp?q={u}", "tmp.html")
    with open("tmp.html") as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    os.remove("tmp.html")
    ree = soup.find('div', attrs={'class': 'web-bing'})
    return render_template(ree[0].prettify())


if __name__ == '__main__':
    app.run(debug=True)
