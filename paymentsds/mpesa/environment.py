class Environment:
	PARAMS = [
		'scheme',
		'domain'
	]

	SANDBOX = 'https://api.sandbox.vm.co.mz'
	PRODUCTION = 'https://api.mpesa.vm.co.mz'

	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			if key in self.PARAMS:
				self.__dict__[key] = value

	@staticmethod
	def from_url(url):
		parts = url.split('://')
		return Environment(scheme=parts[0], domain=parts[1])
