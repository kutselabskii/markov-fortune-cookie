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
    
    # model = make_markov_model(1, data)
    model = make_simple_markov_model(data)
    for i in range(40):
        sentence = generate_random_sentence(random.randint(8, 24), model)
        print(sentence)

if __name__ == "__main__":
    main()
