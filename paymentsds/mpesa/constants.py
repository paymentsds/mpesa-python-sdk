
PATTERNS = {
  'PHONE_NUMBER': re.compile('^((00|\+)?258)?8[45][0-9]{7}$'),
  'SERVICE_PROVIDER_CODE': re.compile('^[0-9]{5,6}$'),
  'WORD': re.compile('\\w+'),
  'MONEY_AMOUNT': re.compile( '^[1-9][0-9]*(\.[0-9])*$')
}

DEFAULT_OPERATIONS = {
  'B2C_PAYMENT': {
      'name':'b2cPayment',
      'method': 'POST',
      'port':'18345',
      'path':'/ipg/v1x/b2cPayment',
      'mapping': {
        'from': 'input_ServiceProviderCode',
        'to': 'input_CustomerMSISDN',
        'amount': 'input_Amount',
        'transaction': 'input_TransactionReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
        'from': PATTERNS['SERVICE_PROVIDER_CODE'],
        'to': re.compile('^((00|\+)?258)?8[45][0-9]{7}$'),
        'amount': re.compile( '^[1-9][0-9]*(\.[0-9])*$'),
        'transaction': re.compile( '\\w+'),
        'reference': re.compile( '\\w+')
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference'
      ],
      'optional': [
        'from'
      ]
  },
  'B2B_PAYMENT': {
      'name':'b2cPayment',
      'method': 'POST',
      'port':'18345',
      'path':'/ipg/v1x/b2cPayment',
      'mapping': {
        'from': 'input_ServiceProviderCode',
        'to': 'input_CustomerMSISDN',
        'amount': 'input_Amount',
        'transaction': 'input_TransactionReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
        'from': PATTERNS['SERVICE_PROVIDER_CODE'],
        'to': re.compile('^((00|\+)?258)?8[45][0-9]{7}$'),
        'amount': re.compile( '^[1-9][0-9]*(\.[0-9])*$'),
        'transaction': re.compile( '\\w+'),
        'reference': re.compile( '\\w+')
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference'
      ],
      'optional': [
       'from'
      ]
  },
  'C2B_PAYMENT': {
      'name':'b2cPayment',
      'method': 'POST',
      'port':'18345',
      'path':'/ipg/v1x/b2cPayment',
      'mapping': {
        'from': 'input_ServiceProviderCode',
        'to': 'input_CustomerMSISDN',
        'amount': 'input_Amount',
        'transaction': 'input_TransactionReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
        'from': PATTERNS['SERVICE_PROVIDER_CODE'],
        'to': re.compile('^((00|\+)?258)?8[45][0-9]{7}$'),
        'amount': re.compile( '^[1-9][0-9]*(\.[0-9])*$'),
        'transaction': re.compile( '\\w+'),
        'reference': re.compile( '\\w+')
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference'
      ],
      'optional': [
        'from'
      ]
  },
  'C2B_PAYMENT': {
      'name':'b2cPayment',
      'method': 'POST',
      'port':'18345',
      'path':'/ipg/v1x/b2cPayment',
      'mapping': {
        'from': 'input_ServiceProviderCode',
        'to': 'input_CustomerMSISDN',
        'amount': 'input_Amount',
        'transaction': 'input_TransactionReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
        'from': PATTERNS['SERVICE_PROVIDER_CODE'],
        'to': re.compile('^((00|\+)?258)?8[45][0-9]{7}$'),
        'amount': re.compile( '^[1-9][0-9]*(\.[0-9])*$'),
        'transaction': re.compile( '\\w+'),
        'reference': re.compile( '\\w+')
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference'
      ],
      'optional': [
        'from'
      ]
  },
  'C2B_PAYMENT': {
      'name':'b2cPayment',
      'method': 'POST',
      'port':'18345',
      'path':'/ipg/v1x/b2cPayment',
      'mapping': {
        'from': 'input_ServiceProviderCode',
        'to': 'input_CustomerMSISDN',
        'amount': 'input_Amount',
        'transaction': 'input_TransactionReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
        'from': re.compile('^[0-9]{5,6}$'),
        'to': re.compile('^((00|\+)?258)?8[45][0-9]{7}$'),
        'amount': re.compile( '^[1-9][0-9]*(\.[0-9])*$'),
        'transaction': re.compile( '\\w+'),
        'reference': re.compile( '\\w+')
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference'
      ],
      'optional': [
        'from' 
      ]
  }
}
