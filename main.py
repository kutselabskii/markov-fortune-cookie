from chain import *
import random

def main():
    data = open("predictions.txt", "r").read()
    for symbol in ['\n', '\t', '\"', '\'']:
        data = data.replace(symbol, ' ')
    for symbol in ['.', '-', ',', '!', '?', '(', ')']:
        data = data.replace(symbol, f' {symbol} ')
    data = data.split()
    data = list(map(lambda x: x.lower(), data))
    
    size = 2
    model = Chain(data, size)
    for i in range(40):
        sentence = model.generate("вы сможете", chain_length=random.randint(8, 24), seed_length=size)
        print(sentence)

if __name__ == "__main__":
    main()
