Simple Envelope
===============

You give it your address and their address, and it makes you an envelope. This is designed principally for Americans sending letters and flats through the United States Postal Service (USPS), but others can use it too.

This is currently very basic, but it will make you an envelope. If I get around to it, here are some features I might add:

- allow the user to configure where addresses are printed on the page
- support custom, user-specified fonts, as well as changing the font and font size
- properly support printing flats, including more sensible defaults for the address position, correct warnings based on USPS physical standards, and proper warnings for printing flats in portrait
- add data for metric envelopes (and test more fully with metric)
- check the delivery address against basic USPS standards (all caps, suffix and secondary unit indicators, proper city-state-ZIP line, common addressing errors, international addresses have the country alone on the last line) and help the user validate it
- warn the user if the addresses overlap, the delivery address extends outside the OCR read area or inside the barcode clear area, or the address is outside the page
- support additional markings like PAR AVION/AIRMAIL, as specified by the International Mail Manual (IMM) for First-Class Mail International
- support printing postcards, including a message area on the left, top, bottom, or none at all, and warnings if the card exceeds the dimensions for postcard prices
- allow the user to configure a default return address
- allow the user to select warnings for a postal carrier apart from USPS
