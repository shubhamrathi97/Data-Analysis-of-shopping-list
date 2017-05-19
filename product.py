import csv
import sys
#Reading Data file
file_obj = open(sys.argv[1])
#Converting file into list
data = csv.reader(file_obj, delimiter=",")
#Removing space in values
data = [[x.strip(' ') for x in row] for row in data]

"""
@method product_check
@param product, data_list
@param_type str, list
@method_description To check if product is in store or not.
"""
def product_check(product, data_list):
	#Initialize list
	shops_have_product = []
	for shop_data in data_list:
		shop_item_list = []
		for i in range(2, len(shop_data)):
			shop_item_list.append(shop_data[i])
		for shop_item in shop_item_list:
			if product == shop_item:
				for all_shop in data_list:
					if all_shop[0] == shop_data[0]:
						shops_have_product.append(all_shop)			
	#Return list of all the shops which have requested product
	return shops_have_product

"""
@method calculator
@param final_list
@param_type list
@method_description Calculates minimum amount of products.
"""
def calculator(final_list):
	sum_list = []
	for i in range(len(final_list)):
		for item in sum_list:
			if final_list[i][0] == sum_list[0]:
				break 
		else:
			for j in range(i+1, len(final_list)):
				if final_list[i][0] == final_list[j][0]:
					sum_list.append([final_list[i][0], float(final_list[i][1]) + float(final_list[j][1])])
	sum_list = sorted(sum_list, key=lambda sum: sum[1])
	return sum_list[0]

"""
@method filter
@param product
@method_description Filter the shops having product, then calculate the minimum amount and prints the result.
"""
def filter(product):
	product_list = product.split(" ")
	if len(product_list) > 0:
		filter_list = product_check(product_list[0], data)
		if len(product_list) > 1:
			for i in range(1, len(product_list)):
				filter_list = product_check(product_list[i], filter_list)
		if len(filter_list) == 0:
			print("None")
			return
		print(calculator(filter_list))
		return
	else:
		print("Empty List ! Add something")
		return False				

if __name__ == '__main__':
	#filter("teddy_bear baby_powder")
	#filter("scissor bath_towel")
	#filter("pampers_diapers baby_soap")
	#filter("scissor powder_puff cotton_balls")
	filter(" ".join([sys.argv[i] for i in range(2,len(sys.argv))]))