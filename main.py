from fastapi import FastAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = FastAPI()

model = SentimentIntensityAnalyzer()


@app.get('/')
async def authenticated(key: str=''):
    '''
    returns state=1 if the user is authenticated else state=0
    '''
    state = 0
    if key == 'bonjour':
        state = 1
    return {'state': state}


@app.get('/sentiment')
async def return_sentiment(key:str='',
                           sentence: str = 'hello world'):
    '''
    returns state=1, sentence and sentiment of the sentence if the user is authenticated
    else return state=0, sentence=sentence, sentiment=0

    sentiment=1 means positive while sentiment=-1 means negative
    '''
    state = 0
    sentiment = 0
    if key == 'bonjour':
        state = 1
        polarity_score = model.polarity_scores(text=sentence)
        print(polarity_score)
        sentiment = polarity_score['compound']

    return {'state': state, 'sentence': sentence, 'sentiment': sentiment}
