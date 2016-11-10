import logging

logger = logging.getLogger('LOGGER')

# CRITICAL - 50 - somthing failed application must close
# ERROR - 40 - some function failed
# WARNING - 30 - something unexpected
# INFO - 20 - confirmation that things accroding to plan
# DEBUG - 10 - detailed info
format = "%(asctime)s %(clientip)-15s %(user)-8s [%(levelname)s] %(message)s"
extra = {'clientip':'192.168.0.1', 'user':'yoko'}
logging.basicConfig(filename="log.log", format=format ,level=logging.DEBUG)

class Item(object):

	def __init__(self, name, value):
		self.name = name
		self.value = value
		logger.info("Item created: {}({})".format(self.name, self.value), extra=extra)

	def buy(self, quantity=1):
		logger.debug("Bought item {}".format(self.name), extra=extra)

	def sell(self, quantity=1):
		logger.warn("Sold item {}".format(self.name), extra=extra)
		
items = []
for index in xrange(100):
	items.append(Item('sowrd_'+str(index), 100))

for item in items:
	item.buy()

for item in items:
	item.sell()