

# Sale_price_zscore for each sale/row
# sqrt((sum((x - mean)^2)) / (n - 1))

query_a = """
SELECT 
	*,
	("SALE_PRICE" - AVG("SALE_PRICE") OVER ()) / STDDEV("SALE_PRICE") OVER () AS sale_price_zscore
FROM nycsales
"""

# SQL query to compute sale_price_zscore_neighborhood for each sale/row
query_b = """
SELECT *,
       ("SALE_PRICE" - AVG("SALE_PRICE") OVER (PARTITION BY "NEIGHBORHOOD", "BUILDING_CLASS")) / 
       STDDEV("SALE_PRICE") OVER (PARTITION BY "NEIGHBORHOOD", "BUILDING_CLASS") AS sale_price_zscore_neighborhood
FROM nycsales;
"""

# SQL query to compute square_ft_per_unit and price_per_unit
query_c = """
SELECT *,
       SQUARE_FT / UNITS_IN_BUILDING AS square_ft_per_unit,
       SALE_PRICE / UNITS_IN_BUILDING AS price_per_unit
FROM nycsales;
"""