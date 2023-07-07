# financial-news-llama-index

Financial News Analysis and Prediciton with Llama Index, GPT-4, and Flask
Trader workstation

1# To run this application locally first make a python environment in conda or venv using python 3.9.16 and following libraries:
--openai
--ib_insync
--pandas
--llama-index
--jinja2
--flask
--matplotlib
--yfinance
--pandas
--seaborn

2# Clone this git repository and do following steps:
-- add your OpenAI API key in config.py
-- (optional) Data is already provided and preprocessed in the git repository in "data" and "storage" directory respectively. But if you want to fetch new data you first need to install 'Trader Workstation' application of International Brokers website which provides financial news and provides api to fetch the news. Their services are not free but you can use the free trial version. To get the data run 'python getData.py' in the project's home directory. After downloading the data, emtpy the 'storage' folder and run 'python PreprocessData.py' in the project's home directory. 

3# To run the project with already provided preprocessed data run 'app.py' in the project's home directory using following command:
--python app.py 
