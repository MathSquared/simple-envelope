ENVELOPE_SIZES = {
    '#6 1/4': ('pt', 252, 432),
    '#6 3/4': ('pt', 261, 468),
    '#7':     ('pt', 270, 486),
    '#7 3/4': ('pt', 279, 540),
    '#8 5/8': ('pt', 261, 621),
    '#9':     ('pt', 279, 639),
    '#10':    ('pt', 297, 684),
    '#11':    ('pt', 324, 747),
    '#12':    ('pt', 342, 792),
    '#14':    ('pt', 360, 828),
    '#16':    ('pt', 432, 864),
}

USPS_SUFFIXES = {
    # USPS Publication 28, C1, 2020-09-07.
    'ALLEY': 'ALY',
    'ANEX': 'ANX',
    'ARCADE': 'ARC',
    'AVENUE': 'AVE',
    'BAYOU': 'BYU',
    'BEACH': 'BCH',
    'BEND': 'BND',
    'BLUFF': 'BLF',
    'BLUFFS': 'BLFS',
    'BOTTOM': 'BTM',
    'BOULEVARD': 'BLVD',
    'BRANCH': 'BR',
    'BRIDGE': 'BRG',
    'BROOK': 'BRK',
    'BROOKS': 'BRKS',
    'BURG': 'BG',
    'BURGS': 'BGS',
    'BYPASS': 'BYP',
    'CAMP': 'CP',
    'CANYON': 'CYN',
    'CAPE': 'CPE',
    'CAUSEWAY': 'CSWY',
    'CENTER': 'CTR',
    'CENTERS': 'CTRS',
    'CIRCLE': 'CIR',
    'CIRCLES': 'CIRS',
    'CLIFF': 'CLF',
    'CLIFFS': 'CLFS',
    'CLUB': 'CLB',
    'COMMON': 'CMN',
    'COMMONS': 'CMNS',
    'CORNER': 'COR',
    'CORNERS': 'CORS',
    'COURSE': 'CRSE',
    'COURT': 'CT',
    'COURTS': 'CTS',
    'COVE': 'CV',
    'COVES': 'CVS',
    'CREEK': 'CRK',
    'CRESCENT': 'CRES',
    'CREST': 'CRST',
    'CROSSING': 'XING',
    'CROSSROAD': 'XRD',
    'CROSSROADS': 'XRDS',
    'CURVE': 'CURV',
    'DALE': 'DL',
    'DAM': 'DM',
    'DIVIDE': 'DV',
    'DRIVE': 'DR',
    'DRIVES': 'DRS',
    'ESTATE': 'EST',
    'ESTATES': 'ESTS',
    'EXPRESSWAY': 'EXPY',
    'EXTENSION': 'EXT',
    'EXTENSIONS': 'EXTS',
    'FALL': 'FALL',
    'FALLS': 'FLS',
    'FERRY': 'FRY',
    'FIELD': 'FLD',
    'FIELDS': 'FLDS',
    'FLAT': 'FLT',
    'FLATS': 'FLTS',
    'FORD': 'FRD',
    'FORDS': 'FRDS',
    'FOREST': 'FRST',
    'FORGE': 'FRG',
    'FORGES': 'FRGS',
    'FORK': 'FRK',
    'FORKS': 'FRKS',
    'FORT': 'FT',
    'FREEWAY': 'FWY',
    'GARDEN': 'GDN',
    'GARDENS': 'GDNS',
    'GATEWAY': 'GTWY',
    'GLEN': 'GLN',
    'GLENS': 'GLNS',
    'GREEN': 'GRN',
    'GREENS': 'GRNS',
    'GROVE': 'GRV',
    'GROVES': 'GRVS',
    'HARBOR': 'HBR',
    'HARBORS': 'HBRS',
    'HAVEN': 'HVN',
    'HEIGHTS': 'HTS',
    'HIGHWAY': 'HWY',
    'HILL': 'HL',
    'HILLS': 'HLS',
    'HOLLOW': 'HOLW',
    'INLET': 'INLT',
    'ISLAND': 'IS',
    'ISLANDS': 'ISS',
    'ISLE': 'ISLE',
    'JUNCTION': 'JCT',
    'JUNCTIONS': 'JCTS',
    'KEY': 'KY',
    'KEYS': 'KYS',
    'KNOLL': 'KNL',
    'KNOLLS': 'KNLS',
    'LAKE': 'LK',
    'LAKES': 'LKS',
    'LAND': 'LAND',
    'LANDING': 'LNDG',
    'LANE': 'LN',
    'LIGHT': 'LGT',
    'LIGHTS': 'LGTS',
    'LOAF': 'LF',
    'LOCK': 'LCK',
    'LOCKS': 'LCKS',
    'LODGE': 'LDG',
    'LOOP': 'LOOP',
    'MALL': 'MALL',
    'MANOR': 'MNR',
    'MANORS': 'MNRS',
    'MEADOW': 'MDW',
    'MEADOWS': 'MDWS',
    'MEWS': 'MEWS',
    'MILL': 'ML',
    'MILLS': 'MLS',
    'MISSION': 'MSN',
    'MOTORWAY': 'MTWY',
    'MOUNT': 'MT',
    'MOUNTAIN': 'MTN',
    'MOUNTAINS': 'MTNS',
    'NECK': 'NCK',
    'ORCHARD': 'ORCH',
    'OVAL': 'OVAL',
    'OVERPASS': 'OPAS',
    'PARK': 'PARK',
    'PARKS': 'PARK',
    'PARKWAY': 'PKWY',
    'PARKWAYS': 'PKWY',
    'PASS': 'PASS',
    'PASSAGE': 'PSGE',
    'PATH': 'PATH',
    'PIKE': 'PIKE',
    'PINE': 'PNE',
    'PINES': 'PNES',
    'PLACE': 'PL',
    'PLAIN': 'PLN',
    'PLAINS': 'PLNS',
    'PLAZA': 'PLZ',
    'POINT': 'PT',
    'POINTS': 'PTS',
    'PORT': 'PRT',
    'PORTS': 'PRTS',
    'PRAIRIE': 'PR',
    'RADIAL': 'RADL',
    'RAMP': 'RAMP',
    'RANCH': 'RNCH',
    'RAPID': 'RPD',
    'RAPIDS': 'RPDS',
    'REST': 'RST',
    'RIDGE': 'RDG',
    'RIDGES': 'RDGS',
    'RIVER': 'RIV',
    'ROAD': 'RD',
    'ROADS': 'RDS',
    'ROUTE': 'RTE',
    'ROW': 'ROW',
    'RUE': 'RUE',
    'RUN': 'RUN',
    'SHOAL': 'SHL',
    'SHOALS': 'SHLS',
    'SHORE': 'SHR',
    'SHORES': 'SHRS',
    'SKYWAY': 'SKWY',
    'SPRING': 'SPG',
    'SPRINGS': 'SPGS',
    'SPUR': 'SPUR',
    'SPURS': 'SPUR',
    'SQUARE': 'SQ',
    'SQUARES': 'SQS',
    'STATION': 'STA',
    'STRAVENUE': 'STRA',
    'STREAM': 'STRM',
    'STREET': 'ST',
    'STREETS': 'STS',
    'SUMMIT': 'SMT',
    'TERRACE': 'TER',
    'THROUGHWAY': 'TRWY',
    'TRACE': 'TRCE',
    'TRACK': 'TRAK',
    'TRAFFICWAY': 'TRFY',
    'TRAIL': 'TRL',
    'TRAILER': 'TRLR',
    'TUNNEL': 'TUNL',
    'TURNPIKE': 'TPKE',
    'UNDERPASS': 'UPAS',
    'UNION': 'UN',
    'UNIONS': 'UNS',
    'VALLEY': 'VLY',
    'VALLEYS': 'VLYS',
    'VIADUCT': 'VIA',
    'VIEW': 'VW',
    'VIEWS': 'VWS',
    'VILLAGE': 'VLG',
    'VILLAGES': 'VLGS',
    'VILLE': 'VL',
    'VISTA': 'VIS',
    'WALK': 'WALK',
    'WALKS': 'WALK',
    'WALL': 'WALL',
    'WAY': 'WAY',
    'WAYS': 'WAYS',
    'WELL': 'WL',
    'WELLS': 'WLS',
}

USPS_SECONDARIES = {
    # USPS Publication 28, C2, 2020-09-07.
    # Boolean is if it requires/allows a unit number.
    'APARTMENT': ('APT', True),
    'BASEMENT': ('BSMT', False),
    'BUILDING': ('BLDG', True),
    'DEPARTMENT': ('DEPT', True),
    'FLOOR': ('FL', True),
    'FRONT': ('FRNT', False),
    'HANGER': ('HNGR', True),
    'KEY': ('KEY', True),
    'LOBBY': ('LBBY', False),
    'LOT': ('LOT', True),
    'LOWER': ('LOWR', False),
    'OFFICE': ('OFC', False),
    'PENTHOUSE': ('PH', False),
    'PIER': ('PIER', True),
    'REAR': ('REAR', False),
    'ROOM': ('RM', True),
    'SIDE': ('SIDE', False),
    'SLIP': ('SLIP', True),
    'SPACE': ('SPC', True),
    'STOP': ('STOP', True),
    'SUITE': ('STE', True),
    'TRAILER': ('TRLR', True),
    'UNIT': ('UNIT', True),
    'UPPER': ('UPPR', False),
}
