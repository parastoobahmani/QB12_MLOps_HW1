
import sys
from hashlib import sha256, pbkdf2_hmac

listings = read_csv_checked('data/raw/listings_sample.csv')

sha256 = hashlib.sha256()
# def pseudonymize_value(value, salt=b'qbc12'):
#     sha256.update(bytes(value)+ salt)
#     return sha256.hexdigest()
    
def pseudonymize_value(value, salt=b'qbc12'):
    dk = pbkdf2_hmac('sha256', bytes(value), salt, 1000)
    return dk.hex()

host_key = []
def handle_pii(df):
    for x in df['host_id']:
        host_key.append(pseudonymize_value(x))
    return host_key
    

listings['host_key'] = handle_pii(listings)
listings = listings.drop(columns=['host_name', 'host_id'])
listings
