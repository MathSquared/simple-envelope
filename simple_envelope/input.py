import re
import sys

from . import constants
from .constants import ENVELOPE_SIZES, TO_PT


ENVELOPE_REGEX = '(?P<height>[0-9.]*) x (?P<width>[0-9.]*) (?P<unit>in|mm|cm|pt)'


def get_input():
    # The principle is that we want the same input format with a TTY or otherwise,
    # but we only prompt if it is a TTY.
    # We also take the input registered so far if EOF is reached.
    show_prompt = sys.stdout.isatty()
    retry_on_error = sys.stdout.isatty()
    show_warning = True
    ret = {}

    if show_prompt:
        print('Welcome to Simple Envelope.')
        print()

    # Everything's wrapped in a big try-except so if we hit EOF, we just return what we have.
    try:
        # Delivery address
        if show_prompt:
            print('Enter the delivery address, ending with a blank line.')
        ret['delivery'] = []
        latest = input()
        while latest != '':
            ret['delivery'].append(latest)
            latest = input()

        # Return address
        if show_prompt:
            print('Now the return address, ending with a blank line.')
        ret['return'] = []
        latest = input()
        while latest != '':
            ret['return'].append(latest)
            latest = input()

        # Envelope size
        if show_prompt:
            print('What size envelope are you using?')
            print('Enter either a standard size or an expression of the form hh x ww unit.')
            print('No fractions. Units: in, mm, cm, pt.')
        latest = input()
        while _parse_envelope_size(latest) is None:
            if not retry_on_error:
                raise ValueError('Bad envelope size {}'.format(latest))
            if show_prompt:
                print('I couldn\'t make sense out of that. Try again, please.')
            latest = input()
        ret['envelope'] = _parse_envelope_size(latest)
        print()

        # Warn if envelope is bad size
        if show_warning:
            for warning in _create_envelope_warnings(ret['envelope']):
                print(warning)
            print()

        return ret
    except EOFError:
        return ret


def _parse_envelope_size(query):
    if query in ENVELOPE_SIZES:
        return ENVELOPE_SIZES[query]
    m = re.match(ENVELOPE_REGEX, query)
    if m:
        return (m.group('unit'), float(m.group('height')), float(m.group('width')))
    return None


def _create_envelope_warnings(size):
    ret = []

    aspect = size[2] / size[1]
    if aspect < constants.ENVELOPE_MACHINEABLE_MIN - 1e-9:
        ret.append('Warning: envelope is non-machineable (too square or portrait)')
    if aspect > constants.ENVELOPE_MACHINEABLE_MAX + 1e-9:
        ret.append('Warning: envelope is non-machineable (too wide)')

    height_pt = size[1] * TO_PT[size[0]]
    width_pt = size[2] * TO_PT[size[0]]

    if height_pt < constants.ENVELOPE_HEIGHT_MIN:
        ret.append('Warning: envelope is non-mailable (not tall enough)')
    if height_pt > constants.ENVELOPE_HEIGHT_BIG:
        ret.append('Warning: envelope is a flat (too tall for a letter)')
    if height_pt < constants.ENVELOPE_HEIGHT_MAX:
        ret.append('Warning: envelope is non-mailable (too tall)')

    if width_pt < constants.ENVELOPE_WIDTH_MIN:
        ret.append('Warning: envelope is non-mailable (not wide enough)')
    if width_pt > constants.ENVELOPE_WIDTH_BIG:
        ret.append('Warning: envelope is a flat (too wide for a letter)')
    if width_pt < constants.ENVELOPE_WIDTH_MAX:
        ret.append('Warning: envelope is non-mailable (too wide)')

    return ret
