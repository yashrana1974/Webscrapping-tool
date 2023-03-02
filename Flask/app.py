from flask import Flask, render_template, request
import requests

from bs4 import BeautifulSoup

app = Flask(__name__)
# Here the code wants to get the link to perfrom beautiful soup https://blank.com to show this website cannot be scrapped
url ="https://m.economictimes.com/news/economy/policy/india-budget-2023-key-highlights/articleshow/97509935.cms"
r = requests.get(url)
html_doc = r.content
soup = BeautifulSoup(html_doc, 'html.parser')
d = {}

@app.route('/')

@app.route('/htmlcode', methods=['GET', 'POST'])
def htmlcode():
    htmlcodeoutput = soup.prettify()
    return render_template('htmlcode.html', htmlcodeoutput=htmlcodeoutput)


@app.route('/webtext', methods=['GET', 'POST'])
def webtext():
    webtext = soup.get_text()
    return render_template('webtext.html', webtext=webtext)

@app.route('/paragraph', methods=['GET', 'POST'])
def paragraph():
    webbody = soup.p
    return render_template('paragraph.html', webbody=webbody)

@app.route('/alllinks', methods=['GET', 'POST'])
def alllinks():
    for x in soup.find_all('a'):
        d[x] = x.get('href')
    link_list = list(d.values())
    link_list = [i for i in d.values()]
    link_list = []
    for i in d.values():
        link_list.append(i)

    return render_template('alllinks.html', link_list=link_list)

if __name__ == "__main__":
    app.run(debug=True, port=8000)