import logging
import random
import analytics

analytics.write_key = ''

analytics.identify('python-customer', {

    'email': 'Marg@gmail.com',

    'name': 'Marg Not',

    'friends': 30

})


