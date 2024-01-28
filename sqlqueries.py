

# Sale_price_zscore for each sale/row
# sqrt((sum((x - mean)^2)) / (n - 1))

query_a = """
SELECT 
	"SALE_PRICE",
	("SALE_PRICE" - AVG("SALE_PRICE") OVER ()) / STDDEV("SALE_PRICE") OVER () AS sale_price_zscore
FROM nycsales;
"""

# SQL query to compute sale_price_zscore_neighborhood for each sale/row
query_b = """
SELECT 
    "SALE_PRICE",
    "NEIGHBORHOOD",
    "BUILDING_CLASS",
    CASE 
        WHEN STDDEV("SALE_PRICE") OVER (PARTITION BY "NEIGHBORHOOD", "BUILDING_CLASS") <> 0 THEN
            ("SALE_PRICE" - AVG("SALE_PRICE") OVER (PARTITION BY "NEIGHBORHOOD", "BUILDING_CLASS")) / 
            STDDEV("SALE_PRICE") OVER (PARTITION BY "NEIGHBORHOOD", "BUILDING_CLASS")
        ELSE
            NULL
    END AS sale_price_zscore_neighborhood
FROM nycsales;
"""

# SQL query to compute square_ft_per_unit and price_per_unit
query_c = """
SELECT 
    "SQUARE_FT",
    "UNITS_IN_BUILDING",
    "SALE_PRICE",
    CASE 
        WHEN "UNITS_IN_BUILDING" <> 0 THEN
            "SQUARE_FT" / "UNITS_IN_BUILDING"
        ELSE
            NULL
    END AS square_ft_per_unit,
    CASE 
        WHEN "UNITS_IN_BUILDING" <> 0 THEN
            "SALE_PRICE" / "UNITS_IN_BUILDING"
        ELSE
            NULL
    END AS price_per_unit
FROM nycsales;
"""