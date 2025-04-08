import sqlite3
import pandas as pd
conn = sqlite3.connect('chinook.db')


query = """
SELECT c.CustomerId, c.FirstName, c.LastName, COUNT(i.InvoiceId) AS TotalInvoices
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
"""
df = pd.read_sql(query, conn)


print("Inner Join Result:")
print(df.head())


conn.close()
