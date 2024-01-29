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