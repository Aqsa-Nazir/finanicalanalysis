import os, config
from llama_index import GPTVectorStoreIndex, StorageContext, load_index_from_storage
from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import yfinance as yf
# import plotly 
import pandas as pd
import seaborn as sns; sns.set()
os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY

from llama_index import ServiceContext, LLMPredictor
from langchain.llms import OpenAI

app = Flask(__name__,static_folder='./templates/startbootstrap/css')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/startbootstrap/index.html', result='')
llm = OpenAI(model_name='gpt-4', max_tokens=6000)

llm_predictor = LLMPredictor(llm=llm)

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    
@app.route('/process', methods=['POST'])
def process():
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    symbol = request.form.get('dropdown')
    if symbol == 'Google':
        ysymbol = 'GOOG'
    elif symbol == 'Microsoft':
        ysymbol = 'MSFT'
    elif symbol == 'Nvidia':
        ysymbol = 'NVDA'
    elif symbol == 'Amazon':
        ysymbol = 'AMZN'
    elif symbol == 'Meta':
        ysymbol = 'META'
    elif symbol == 'Apple':
        ysymbol = 'AAPL'
    elif symbol == 'Taiwan Semiconductor':
        ysymbol = 'TSM'
    elif symbol == 'Pepsi':
        ysymbol = 'PEP'
    elif symbol == 'Intel':
        ysymbol = 'INTC'
    elif symbol == 'Adobe':
        ysymbol = 'ADBE'
    elif symbol == 'Netflix':
        ysymbol = 'NFLX'
    elif symbol == 'Tesla':
        ysymbol = 'TSLA'
    
    
    df = yf.download(ysymbol, period='1d', start='2019-01-01', end='2023-07-1')
    df.head()
    img = io.BytesIO()

    plt.figure(figsize=(14,5))
    sns.set_style("ticks")
    sns.lineplot(data=df,x="Date",y='High',color='firebrick')
    plt.ylabel('Price ($)')
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    if request.form['action'] == 'Generate Analysis': 
        response = query_engine.query(f"Is the {symbol} stock trend going up or down? Be sure to include why and when.")
        result = response       
        # print(plot_url)
        return render_template('/startbootstrap/index.html', result=result , plot_url=plot_url)
    elif request.form['action'] == 'Generate Report':
        response2 = query_engine.query(f"write a report on {symbol} stock untill 2027 Be sure to include potential risks and headwinds.")
        result2 = response2
        return render_template('/startbootstrap/index.html', result2=result2, plot_url=plot_url)


if __name__ == '__main__':
    app.run()

