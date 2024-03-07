
import duckdb
from palmerpenguins import penguins

conn = duckdb.connect('my-db.duckdb')
df = penguins.load_penguins()
conn.execute('CREATE TABLE penguins AS SELECT * FROM df')
conn.close()

conn = duckdb.connect('my-db.duckdb')
df = conn.execute('SELECT * FROM penguins').fetchdf().dropna()
df.head()
conn.close()
