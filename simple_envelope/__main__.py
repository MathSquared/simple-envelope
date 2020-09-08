from .constants import DEFAULT_SPECS
from .generate import make_envelope
from .input import get_input

def main():
    specs = dict(DEFAULT_SPECS)
    specs.update(get_input())
    pdf_bytes = make_envelope(specs)
    with open('output.pdf', 'wb') as fout:
        fout.write(pdf_bytes)


if __name__ == '__main__':
    main()
