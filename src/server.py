from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import src.tweet as tweeter
import src.word_filter as filter

@app.route('/', methods = ['GET'])
def homepage():
    return render_template('homepage.html')
@app.route('/submit', methods = ['POST'])
def submit():
    #print("post")
    tweet = request.form.get('tweet',None)
    #print(tweet)
    if(filter.isBadWord(tweet)):
        tweeter.submit('The word filter has blocked this message from being sent.')
    else:
        tweeter.submit(tweet)
    return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)