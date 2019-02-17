from flask import Flask, request, render_template_string

app = Flask(__name__)


def game(min_1=0, max_1=1000):
    guess = int((max_1 - min_1) / 2) + min_1
    return guess, min_1, max_1


@app.route('/', methods=['GET', 'POST'])
def guesses():
    dane = '''<form action="" method="POST">
                          <h3>Pomyśl liczbę od 0 do 1000.
                          Zgadnę ją w max 10 próbach! Spróbujemy?</h3><br>
                          Zgaduję: {{guess_1}}<br><br>
                          <input type="submit" value="więcej" name="wiecej">
                          <input type="submit" value="mniej" name="mniej">
                          <input type="submit" value="trafiłeś" name="trafiles">
                          <input type="hidden" name="min_1" value={{min_1}}>
                          <input type="hidden" name="max_1" value={{max_1}}>
                          <input type="hidden" name="guess_1" value={{guess_1}}>
                      </form>'''
    if request.method == 'GET':
        return render_template_string(dane, guess_1=game()[0], min_1=game()[1],
                                      max_1=game()[2])
    else:
        more = request.form.get("wiecej")
        less = request.form.get("mniej")
        win = request.form.get("trafiles")
        tries = 0
        if tries < 11:
            if more:
                tries += 1
                guess_1 = int(request.form.get("guess_1"))
                max_1 = int(request.form.get("max_1"))
                result = render_template_string(dane, guess_1=game(guess_1, max_1)[0], min_1=game(guess_1, max_1)[1],
                                                max_1=game(guess_1, max_1)[2])
                return result
            elif less:
                tries +=1
                guess_1 = int(request.form.get("guess_1"))
                min_1 = int(request.form.get("min_1"))
                result = render_template_string(dane, guess_1=game(min_1, guess_1)[0], min_1=game(min_1, guess_1)[1],
                                                max_1=game(min_1, guess_1)[2])
                return result
            elif win:
                return "Wygrałem! Twoja liczba to {}".format(request.form.get("guess_1"))


if __name__ == "__main__":
    app.run(debug=True)
