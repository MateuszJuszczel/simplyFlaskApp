from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    dane = '''<form action="" method="POST">
                      Podaj kod pocztowy: <input type="text" name="code"><br>
                      <input type="submit" value="Submit"><br>
                  </form>'''
    if request.method == 'GET':
        return dane
    else:
        code = request.form.get("code")
        if "-" in code:
            s = code.split("-")
            if len(s[0]) == 2 and len(s[1]) == 3 and s[0].isdigit() and s[1].isdigit():
                return "Kod poprawny"
            else:
                return "Kod niepoprawny"
        else:
            return "Kod niepoprawny"

if __name__ == "__main__":
    app.run(debug=True)