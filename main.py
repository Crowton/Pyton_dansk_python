from tokenize import tokenize, untokenize


def run_code(file: str):
    keys = {
        'hvis': 'if',
        'i': 'in',
        'Rigtigt': 'True',
        'Forkert': 'False',
        'imens': 'while',
        'hvert': 'for',
        'eller': 'or',
        'og': 'and',
        'fortsæt': 'continue',
        'afbryd': 'break',
        'spænd': 'range',
        'aflever': 'return',
        'importér': 'import',
        'ellers': 'else',
        'elvis': 'elif',
        'udskriv': 'print',
        'prøv': 'try',
        'afvent': 'await',
        'passér': 'pass',
        'medmindre': 'except',
        'rejs': 'raise',
        'klasse': 'class',
        'endeligt': 'finally',
        'er': 'is',
        'som': 'as',
        'definér': 'def',
        'fra': 'from',
        'udefrakommende': 'nonlocal',
        'kontrollér': 'assert',
        'fjern': 'del',
        'verdensomspændende': 'global',
        'ej': 'not',
        'med': 'with',
        'asynkron': 'async',
        'afkast': 'yield',
        'næste': 'next',
        'længde': 'len',
        'størrelse': 'size',
        'heltal': 'int',
        'decimaltal': 'float',
        'tekst': 'str',
        'bogstav': 'char',
        'summér': 'sum',
        'hoved': 'head',
        'hale': 'hale',
        'åben': 'open',
        'påsæt': 'append',
        'indsæt': 'insert',
        'liste': 'list',
        'tag': 'pop',
        'skub': 'push',
        'sortér': 'sort',
        'kopiér': 'copy',
        'modtag': 'input',
        'sig': 'self',
        'få': 'get',
        'lokalisér': 'find',
        'luk': 'close',
        'primær': 'main',
        'navn': 'name',
        'sammensæt': 'join',
        'tæl': 'count',
        'lokation': 'location',
        'sti': 'path',
        'fil': 'file',
        'læs': 'read',
        'skriv': 'write',
        '__fil__': '__file__'
    }

    with open(file, 'rb') as src:
        tokens = []

        for token in tokenize(src.readline):
            if token.string in keys:
                t = (token.type, keys[token.string])
            else:
                t = (token.type, token.string)

            tokens.append(t)

    code = untokenize(tokens).decode('utf-8')
    exec(code)

if __name__ == '__main__':
    run_code('kode.pyt')