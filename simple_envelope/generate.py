from fpdf import FPDF

from .constants import TO_PT


def make_envelope(specs):
    # First, compute delivery_from_right if we need to
    delivery_from_right = specs['delivery_from_right'] or _compute_delivery_from_right(specs['envelope'])

    unit = specs['envelope'][0]
    to_pt = TO_PT[unit]

    size_tuple = specs['envelope'][1], specs['envelope'][2]
    orientation = 'L' if size_tuple[0] <= size_tuple[1] else 'P'
    size_tuple = min(size_tuple), max(size_tuple)
    pdf = FPDF(orientation, unit, size_tuple)

    pdf.set_auto_page_break(False)
    # Margins don't really matter because we jump around manually, but eh why not
    pdf.set_margins(specs['return_from_left'], specs['return_from_top'])
    pdf.add_page()

    delivery_leading = specs['delivery_size'] / to_pt * specs['line_spacing']
    _print_multiline(
        pdf,
        -delivery_from_right / to_pt,
        -specs['delivery_from_bottom'] / to_pt,
        specs['delivery'],
        specs['delivery_font'],
        specs['delivery_size'],
        delivery_leading,
    )

    return_leading = specs['return_size'] / to_pt * specs['line_spacing']
    _print_multiline(
        pdf,
        specs['return_from_left'] / to_pt,
        specs['return_from_top'] / to_pt,
        specs['return'],
        specs['return_font'],
        specs['return_size'],
        return_leading,
    )

    # encode call prescribed by docs for Python 3
    return pdf.output(dest='S').encode('latin-1')


def _compute_delivery_from_right(envelope):
    # Wider of 4 in or 65% of the envelope
    width_pt = envelope[2] * TO_PT[envelope[0]]
    return max(width_pt * 0.65, 4 * 72)


def _print_multiline(pdf, x, y, lines, font, size, leading):
    pdf.set_xy(x, y)
    pdf.set_font(font, '', size)
    for line in lines:
        pdf.cell(0, leading, line, ln=2)
