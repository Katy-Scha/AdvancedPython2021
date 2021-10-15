import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--country', type=str, required=True)
    parser.add_argument('--petal-colour', type=str, choices=['R', 'V', 'Y', 'W', 'B'], required=True)
    parser.add_argument('--stem-length', type=int, required=True)
    parser.add_argument('--with-thorns', type=bool, nargs='?', const=True, default=False)
    parser.add_argument('--companion-plants', type=str, nargs='+', default=None)
    return parser

if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    with open('journal.txt', "a") as file:
        file.write(str(vars(args)))
        file.write('\n')