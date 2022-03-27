## https://segment.com/docs/connections/sources/catalog/libraries/server/python/quickstart/
## https://segment.com/docs/connections/sources/catalog/libraries/server/python/

import analytics
import datetime

analytics.write_key = ''

## https://segment.com/docs/connections/sources/catalog/libraries/server/python/#identify
## make this call when login, signup or page load
## Properties below are user_id, traits
print('Start Identify a User...')
analytics.identify('f4ca124298', {
    'name': 'Michael Bolton',
    'email': 'mbolton@example.com',
    'created_at': datetime.datetime.now()
})
print('End Identify a User.')

## https://segment.com/docs/connections/sources/catalog/libraries/server/python/#track
##  Properties below are user_id, event_name, properties
print('Start Track User 1...')
analytics.track('f4ca124298', 'Signed Up', {
  'plan': 'Enterprise'
})
print('End Track User 1.')

## https://segment.com/docs/connections/sources/catalog/libraries/server/python/#track
##  Properties below are user_id, event_name, properties
print('Start Track User 2...')
analytics.track('f4ca124298', 'Article Bookmarked', {
    'title': 'Snow Fall',
    'subtitle': 'The Avalance at Tunnel Creek',
    'author': 'John Branch'
})
print('End Track User 2.')

## https://segment.com/docs/connections/sources/catalog/libraries/server/python/#track
##  Properties below are user_id, event_name, properties
print('Start Track Garbage...')
analytics.track('xxxxx', 'Garbage', {
  'garbage': 'xx16238467841789'
})
print('End Track Garbage.')

## https://segment.com/docs/connections/sources/catalog/libraries/server/python/#page
## Properties below are user_id, category, page_name
print('Start Page...')
analytics.page('grifftest', 'Docs', 'Python', {
  'url': 'http://segment.com'
})
print('End Page.')

## https://segment.com/docs/connections/sources/catalog/libraries/server/python/#screen
## the following is for mobile
## Properties below are user_id, category, page_name
print('Start Screen...')
analytics.screen('grifftest', 'Settings', 'Brightness', {
  'from': 'Home Screen'
})
print('End Screen.')

## https://segment.com/docs/connections/sources/catalog/libraries/server/python/#group
print('Start Group...')
analytics.group('grifftest', 'group_id', {
  'name': 'Initech',
  'domain': 'Accounting Software'
})
print('End Group.')


#https://segment.com/docs/connections/sources/catalog/libraries/server/python/#alias

customer_cookie = '92734232-2342423423-973945'
user_id = '1234'

##so we could pass in customer cookie guid whenever not logged in for every event
# the anonymous user does actions under an anonymous ID
analytics.track(customer_cookie, 'Anonymous Event')

##
# the anonymous user signs up and is aliased to their new user ID
analytics.alias(customer_cookie, user_id)

# the user is identified
analytics.identify('1234', { 'plan': 'Free' })

# the identified user does actions
analytics.track(user_id, 'Identified Action')



