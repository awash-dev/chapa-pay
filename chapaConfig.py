from chapa import Chapa
from datetime import datetime

key_api = 'CHASECK_TEST-0zD8Cma3TVM8EOa0Vt8QDOpgnoKe579O'
chapa = Chapa(key_api)

class Payment:
    @staticmethod
    def pay(amount, fname, lname, email):
        try:
            # Generate a unique transaction reference
            tx_ref = datetime.now().strftime('%Y%m%d%H%M%S')
            tx_key = f'tx{fname}{tx_ref}'
           
            # Prepare the payment data
            data = {
                "amount": amount,  # Amount in the smallest currency unit (e.g., cents)
                "currency": "ETB",
                "first_name": fname,
                "last_name": lname,
                "email": email,
                'tx_ref': tx_key,  # Unique transaction reference
                'redirect_url': 'https://www.yourcallbackurl.com',  # Replace with your actual redirect URL
                'customizations': {
                    'title': 'Awash Shop',
                    'description': 'Payment for services',
                    'logo': 'https://assets.piedpiper.com/logo.png'
                }
            }
            
            response = chapa.initialize(**data)
            return {'response': response, 'tx_key': tx_key}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def verify(tx_num):
        try:
            # Verify the payment with the transaction reference
            response = chapa.verify(tx_num)
            return response
        except Exception as e:
            return {'error': str(e)}
