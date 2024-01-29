numeric_columns = ["RESIDENTIAL UNITS","COMMERCIAL UNITS","TOTAL UNITS", "LAND SQUARE FEET" ,
           "GROSS SQUARE FEET","SALE PRICE"
           ]

categorical_columns = ["BOROUGH","NEIGHBORHOOD",'BUILDING CLASS CATEGORY', 'TAX CLASS AT PRESENT',
               'BUILDING CLASS AT PRESENT','ZIP CODE', 'BUILDING CLASS AT TIME OF SALE', 
               'TAX CLASS AT TIME OF SALE'
               ]

date_column = 'SALE DATE'

borough_encoding = {
    1:'Manhattan', 2:'Bronx', 3: 'Brooklyn', 4:'Queens',5:'Staten Island'
    }

column_name_map = {
    "SALE PRICE": "SALE_PRICE",
    "LAND SQUARE FEET": "SQUARE_FT",
    "TOTAL UNITS":"UNITS_IN_BUILDING",
    "BUILDING CLASS AT PRESENT":"BUILDING_CLASS"
}

target_variable = 'SALE PRICE'
file_path = 'data/nyc-rolling-sales.csv'

"""
BOROUGH: 
A digit code for the borough the property is located in.

- Manhattan = 1

- Bronx = 2

- Brooklyn = 3

- Queens = 4

- Staten Island = 5

BLOCK; LOT: 

- The combination of borough, block, and lot forms a unique key for property in New York City.


BUILDING CLASS AT PRESENT and BUILDING CLASS AT TIME OF SALE: 

- The type of building at various points in time.


** Note : 0 dollar sales are actually transfers of ownership between parties.
"""