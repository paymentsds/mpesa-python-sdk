# PYTHON M-Pesa SDK


<p align="center"><a href="https://pypi.org/project/paymentsds-mpesa/"><img src="https://img.shields.io/pypi/dm/paymentsds-mpesa" alt="Total Downloads"></a> <a href="https://github.com/paymentsds/mpesa-python-sdk/"><img src="https://img.shields.io/pypi/v/paymentsds-mpesa" alt="Latest Stable Version"></a> <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a></p>

This is a library willing to help you to integrate the [Vodacom M-Pesa](https://developer.mpesa.vm.co.mz) operations to your application.

<br>

### Features

Using this library, you can implement the following operations:

- Receive money from a mobile account to a business account (C2B)
- Send money from a business account to a mobile account (B2C)
- Send money from a business account to another business account (B2B)
- Revert any of the transactions above mentioned

<br><br>

## Requirements

- Valid credentials obtained from the [Mpesa Developer](https://developer.mpesa.vm.co.mz) portal
- Port 18352 open on your server (usually open on local env)
- [Python 3.5+](https://www.python.org)
- [PIP](https://pip.pypa.io)


<br><br>


## Installation

<br>

### Using PIP

```bash
$ pip install paymentsds-mpesa

$ cd paymentsds-mpesa

$ pip install -r requirements.txt
```

<br><br>


## Usage

Using this SDK is very simple and fast, let us see some examples:

<br>

#### C2B Transaction (Receive money from mobile account)

```python
from paymentsds.mpesa import Client

client = Client(
   api_key='<REPLACE>',              # API Key
   public_key='<REPLACE>',           # Public Key
   service_provider_code='<REPLACE>' # input_ServiceProviderCode
)

try:
   payment_data = {
      'from': '841234567',       # input_CustomerMSISDN
      'reference': '11114',      # input_ThirdPartyReference
      'transaction': 'T12344CC', # input_TransactionReference
      'amount': '10'             # input_Amount
   }

   result = client.receive(payment_data)
except:
   print('Operation failed')

```

<br>

#### B2C Transaction (Sending money to mobile account)

```python
from paymentsds.mpesa import Client

client = Client(
   api_key='<REPLACE>',              # API Key
   public_key='<REPLACE>',           # Public Key
   service_provider_code='<REPLACE>' # input_ServiceProviderCode
)

try:
   payment_data = {
      'to': '841234567',         # input_CustomerMSISDN
      'reference': '11114',      # input_ThirdPartyReference
      'transaction': 'T12344CC', # input_TransactionReference
      'amount': '10'             # input_Amount
   }

   result = client.send(payment_data)
except:
   print('Operation failed')

```

<br>

#### B2B Transaction (Sending money to business account)

```python
from paymentsds.mpesa import Client

client = Client(
   api_key='<REPLACE>',              # API Key
   public_key='<REPLACE>',           # Public Key
   service_provider_code='<REPLACE>' # input_ServiceProviderCode
)

try:
   payment_data = {
      'to': '979797',            # input_ReceiverPartyCode
      'reference': '11114',      # input_ThirdPartyReference
      'transaction': 'T12344CC', # input_TransactionReference
      'amount': '10'             # input_Amount
   }

   result = client.send(payment_data)
except:
   print('Operation failed')

```

<br>


#### Transaction Reversal

```python
from paymentsds.mpesa import Client

client = Client(
   api_key='<REPLACE>',                # API Key
   public_key='<REPLACE>',             # Public Key
   service_provider_code='<REPLACE>',  # input_ServiceProviderCode
   initiatorIdentifier='<REPLACE>',    # input_InitiatorIdentifier,
   securityIdentifier='<REPLACE>'      # input_SecurityCredential
)

try:
   reversion_data = {
      'reference': '11114',      # input_ThirdPartyReference
      'transaction': 'T12344CC', # input_TransactionReference
      'amount': '10'             # input_ReversalAmount
   }

   result = client.revert(reversion_data)
except:
   # Handle success scenario

```

<br>

## Friends

- [M-Pesa SDK for Javascript](https://github.com/paymentsds/mpesa-js-sdk)
- [M-Pesa SDK for Java](https://github.com/paymentsds/mpesa-java-sdk)
- [M-Pesa SDK for PHP](https://github.com/paymentsds/mpesa-php-sdk)
- [M-Pesa SDK for Ruby](https://github.com/paymentsds/mpesa-ruby-sdk)


<br><br>

## Authors <a name="authors"></a>

- [Edson Michaque](https://github.com/edsonmichaque)
- [Nélio Macombo](https://github.com/neliomacombo)


<br><br>

## Contributing

Thank you for considering contributing to this package. If you wish to do it, email us at [developers@paymentsds.org](mailto:developers@paymentsds.org) and we will get back to you as soon as possible.


<br><br>

## Security Vulnerabilities

If you discover a security vulnerability, please email us at [developers@paymentsds.org](mailto:developers@paymentsds.org) and we will address the issue with the needed urgency.

<br><br>

## License

Copyright 2022 &copy; The PaymentsDS Team

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
