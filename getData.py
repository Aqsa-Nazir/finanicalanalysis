# this is for downloading the current data and storing on the computer for use
from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

news_providers = ib.reqNewsProviders()

codes = '+'.join(news_provider.code for news_provider in news_providers)

symbols = ['AMZN','MSFT', 'NVDA', 'GOOG', 'META', 'AAPL', 'TSM', 'PEP', 'INTC', 'TSLA', 'ADBE', 'NFLX']

for symbol in symbols:
    stock = Stock(symbol, 'SMART', 'USD')
    ib.qualifyContracts(stock)
    headlines = ib.reqHistoricalNews(stock.conId, codes, '', '', 100)

    for headline in headlines:
        article_date = headline.time.date()
        article = ib.reqNewsArticle(headline.providerCode, headline.articleId)

        article_filename = f"data/{article_date}-{symbol}-{headline.articleId}.html"

        with open(article_filename, 'w') as f:
            f.write(article.articleText)
