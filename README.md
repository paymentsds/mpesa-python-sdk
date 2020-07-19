# MPesa Ruby SDK

Ruby client for the [Vodacom M-Pesa API](https://developers.mpesa.vm.co.mz).

## Contents

1. [Features](#features)
1. [Requirements](#requirements)
1. [Configuration](#configuration)
1. [Usage](#usage)
   1. [Quickstart](#contributing)
   1. [Examples](#contributing)
1. [Installation](#installation)
   1. [Using Rubygems](#installation-rubygems)
   1. [Using Bundler](#installation-bundler)
   1. [Manual Installation](#installation-manual)
1. [Related Projects](#related)
   1. [Dependencies](#contributing)
   1. [Friends](#contributing)
   1. [Alternatives](#contributing)
1. [Contributing](#contributing)
1. [Changelog](#changelog)
1. [Authors](#authors)
1. [Credits](#credits)
1. [License](#license)

## Features <a name="features"></a>
- Make C2B transaction
- Make B2C transaction
- Make B2B transaction
- Revert a transaction
- Query transaction status

## Requirements <a name="requirements"></a>

- [Ruby](https://www.ruby-lang.org)
- [Rubygems](https://rubygems.org)
- [Bundler](https://bundler.io/)

## Usage <a name="usage"></a>
### Quickstart <a name="usage-quickstart"></a>
```python
from paysuite.mpesa import Client

client = Client(
    api_key = '',
    public_key = '',

)

data = {
    'from': '84XXXXXX',
    'amount': '10',
    'transaction': 'TX',
    'reference': 'REF'
}

result = client.receive(data)

if result.is_success:
    puts result.data
```

### Receive money from a mobile wallet

```python
from paysuite.mpesa import Client

client = Client(
    api_key = '',
    public_key = '',

)

data = {
    'from': '84XXXXXX',
    'amount': '10',
    'transaction': 'TX',
    'reference': 'REF'
}

result = client.receive(data)

if result.is_success:
    puts result.data
```

### Send money to a mobile wallet

```python
from paysuite.mpesa import Client

client = Client(
    api_key = '',
    public_key = '',

)

data = {
    'from': '84XXXXXX',
    'amount': '10',
    'transaction': 'TX',
    'reference': 'REF'
}

result = client.receive(data)

if result.is_success:
    puts result.data
```

### Send money to a business wallet

```python
from paysuite.mpesa import Client

client = Client(
    api_key = '',
    public_key = '',

)

data = {
    'from': '84XXXXXX',
    'amount': '10',
    'transaction': 'TX',
    'reference': 'REF'
}

result = client.receive(data)

if result.is_success:
    puts result.data
```

### Revert a transaction

```python
from paysuite.mpesa import Client

client = Client(
    api_key = '',
    public_key = '',

)

data = {
    'from': '84XXXXXX',
    'amount': '10',
    'transaction': 'TX',
    'reference': 'REF'
}

result = client.receive(data)

if result.is_success:
    puts result.data
```

### Query the status of a transaction

```python
from paysuite.mpesa import Client

client = Client(
    api_key = '',
    public_key = '',

)

data = {
    'from': '84XXXXXX',
    'amount': '10',
    'transaction': 'TX',
    'reference': 'REF'
}

result = client.receive(data)

if result.is_success:
    puts result.data
```

### Examples <a name="usage-examples"></a>
- [Make C2B transaction](examples/c2b_payment.rb)
- [Make B2C transaction](examples/b2c_payment.rb)
- [Make B2B transaction](examples/b2b_payment.rb)
- [Revert a transaction](examples/reversal.rb)
- [Query transaction status](examples/query_transaction_status.rb)

## Installation <a name="installation"></a>
### Using Rubygems <a name="installation-rubygems"></a>
```bash
$ gem install paysuite-mpesa
```

### Using Bundler <a name="installation-rubygems"></a>
```ruby
# Gemfile
pip install paysuite-mpesa'
```

```bash
$ pip install paysuite-mpesa
```

### Manual Installation <a name="installation-manual"></a>
```bash
$ git clone https://github.com/paysuite/mpesa-ruby-sdk.git
$ cd mpesa-js-sdk
$ bundle exec rake build
$ bundle exec rake install
```

## Configuration <a name="configuration"></a>
The complete set of configurations looks like this:

```ruby
require 'paysuite/mpesa'

client = Paysuite::MPesa::Client.new do |config|
    config.api_key = '<REPLACE>'
    config.public_key = '<REPLACE>'
    config.service_provider_code = '<REPLACE>'
    config.debugging = true
    config.verify_ssl = false
    config.environment = :sandbox
end
```

The minimal configuration is:
```ruby
require 'paysuite/mpesa'

client = Paysuite::MPesa::Client.new do |config|
    config.api_key = '<REPLACE>'
    config.public_key = '<REPLACE>'
end
```

Or if you have pre-calculated the access token offline:

```ruby
require 'paysuite/mpesa'

client = Paysuite::MPesa::Client.new do |config|
	config.access_token = '<REPLACE>'
end
```

## Related Projects <a name="related"></a>

### Dependencies <a name="related-dependencies"></a>
- [Faraday](https://github.com/lostisland/faraday)

### Friends <a name="related-friends"></a>
TODO: 

### Alternatives <a name="related-alternatives"></a>
TODO: 

### Inspiration
- [rosariopfernandes/mpesa-node-api](https://github.com/abdulmueid/mpesa-php-api)
- [karson/mpesa-php-sdk](https://github.com/karson/mpesa-php-sdk)
- [codeonweekends/mpesa-php-sdk](https://github.com/codeonweekends/mpesa-php-sdk)
- [abdulmueid/mpesa-php-api](https://github.com/abdulmueid/mpesa-php-api)
- [realdm/mpesasdk](https://github.com/realdm/mpesasdk)

## Contributing <a name="contributing"></a>

## Changelog <a name="changelog"></a>

## Authors <a name="authors"></a>

- [Edson Michaque](https://github.com/edsonmichaque)
- [Nélio Macombo](https://github.com/neliomacombo)

## Credits <a name="credits"></a>

## License <a name="license"></a>

Copyright 2020 Edson Michaque and Nélio Macombo

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

