from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Create a connection to force database creation
conn = engine.connect()
conn.close()

print("Database created successfully!")