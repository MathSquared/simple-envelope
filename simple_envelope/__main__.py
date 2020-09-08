from .constants import DEFAULT_SPECS
from .input import get_input

def main():
    specs = dict(DEFAULT_SPECS)
    specs.update(get_input())


if __name__ == '__main__':
    main()
