import pandas as pd
from sqlalchemy import create_engine

# Read csv file
data = pd.read_csv('...\\superstore.csv')

# Standardize column names
data.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in data.columns]

# Convert to datetime
data['order_date'] = pd.to_datetime(data['order_date'], format='%d/%m/%Y')
data['ship_date'] = pd.to_datetime(data['ship_date'], format='%d/%m/%Y')

# MySQL connection details
username = '[USERNAME]'
password = '[PASSWORD]'
host = 'localhost'
port = '3306'
database = '[DATABASE_NAME]'

# Create SQLAlchemy engine
engine = create_engine(
    f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'
)

# Load DataFrame into MySQL
data.to_sql(
    name='superstore',
    con=engine,
    if_exists='replace',
    index=False
)

print('Data successfully loaded into MySQL')
print(f'Loaded {len(data)} records')
