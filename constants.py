numeric_columns = ["RESIDENTIAL UNITS","COMMERCIAL UNITS","TOTAL UNITS", "LAND SQUARE FEET" ,
           "GROSS SQUARE FEET","SALE PRICE"
           ]

categorical_columns = ["BOROUGH","NEIGHBORHOOD",'BUILDING CLASS CATEGORY', 'TAX CLASS AT PRESENT',
               'BUILDING CLASS AT PRESENT','ZIP CODE', 'BUILDING CLASS AT TIME OF SALE', 
               'TAX CLASS AT TIME OF SALE'
               ]

date_column = 'SALE DATE'

borough_encoding = {1:'Manhattan', 2:'Bronx', 3: 'Brooklyn', 4:'Queens',5:'Staten Island'}
#borough_encoding = {'Manhattan':1, 'Bronx':2, 'Brooklyn': 3, 'Queens':4 ,'Staten Island':5}