class RefundPolicy:
	def __init__(self, item, customer_name):
		self.item = item
		self.customer_name = customer_name
	
	def get_refund_days(self):
		pass

class HygieneProductRefund(RefundPolicy):
	def get_refund_days(self):
		return 0

class ProductRefund(RefundPolicy):
	def get_refund_days(self):
		return 14

print(HygieneProductRefund("Loop In-ear", "Hannah XXXXXX").get_refund_days())
print(ProductRefund("Max Mara Art. 12345", "Nicole XXXXXX").get_refund_days())
