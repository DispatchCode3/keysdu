import psycopg2
connection = psycopg2.connect(user = "u_keysdu",
                                password = "#R0b3rtB3u533",
                                host = "localhost",
                                port = "5432",
                                database = "keysdu")

cursor = connection.cursor()

cursor.execute("""
    INSERT INTO public.keyholders_address (area, number, directional, street_name, street_type, suffix, zipcode, city_id)
    SELECT area, number, directional, street_name, street_type, suffix, zipcode, (SELECT c.id FROM public.keyholders_city c WHERE c.name = t.city) AS city_id
    FROM public.tmp t
""")

connection.commit()
