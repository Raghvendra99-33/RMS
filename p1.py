product_list=[]
product_sold_list=[]
class product:
   	def __init__(self,name,price,Imported_quantity,Total_sold_quantity=0):
		self.name=name
		self.price=price
		self.Imported_quantity=Imported_quantity
		self.Total_sold_quantity=Total_sold_quantity
	def add_to_product(self):
		product_list.append(self.name)
	def sell(self,sell_qty):
		print("Product=",self.name)
		print("Pay= $",self.price)
		print("quantity_sold=",sell_qty)
		product_sold_list.append(self.name)
		self.Total_sold_quantity+=sell_qty
	def product_info(self):
		print("Product_name=",self.name)
		print("Price=",self.price)
		print("Imported_quantity=",self.Imported_quantity)
		print("Total_sold_quantity=",self.Total_sold_quantity)
		print("Total_left_quantity=",(self.Imported_quantity-self.Total_sold_quantity))
