from chain import *
import random
import pandas as pd

def create_model(folder):
    data = open("predictions.txt", "r").read()
    news = ' '.join(pd.read_csv("lenta-ru-news.csv", nrows=10000)["text"].tolist())
    data = data + news

    for symbol in ['\n', '\t', '\"', '\'']:
        data = data.replace(symbol, ' ')
    for symbol in ['.', '-', ',', '!', '?', '(', ')']:
        data = data.replace(symbol, f' {symbol} ')
    data = data.split()
    data = list(map(lambda x: x.lower(), data))
    
    size = 2
    model = Chain()
    model.create(data, size)
    model.save(folder)
    return model

def load_model(folder):
    model = Chain()
    model.load(folder)
    return model

def main():
    # model = create_model("big")
    model = load_model("big")

    for i in range(10):
        sentence = model.generate("судьба будет", chain_length=random.randint(8, 60), seed_length=model.size)
        print(sentence)


if __name__ == "__main__":
    main()
