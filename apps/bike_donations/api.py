import requests
import json
import string
import random
import time
from .api_errors import errorsDictionary
from .models import InventoryItem

class LightspeedApi(object):
	acnt = ''
	auth = ('', '')

	def get_inventory(self):
		url = 'https://api.merchantos.com/API/Account/'+self.acnt+'/Item.json'

		response = requests.get(url, auth=self.auth)
		return response.content

	def get_item(self, customSku):
		url = 'https://api.merchantos.com/API/Account/'+self.acnt+'/Item/'+customSku+'.json'


		### used with lightspeed api ###
		# response = requests.get(url, auth=self.auth)
		# if response.status_code != 200:
		# 	if response.status_code == 404:
		# 		finalResult = {'status': 'Item could not be found'}
		# 	else:
		# 		finalResult = {'status': errorsDictionary[response.status_code]}
		# else:
		# 	finalResult = {'status': response.status_code, 'content':response.content}

		### ###

		fake_api_request_delay = time.sleep(random.random() * 2.5 + 0.5)

		response = InventoryItem.objects.get(customSku=customSku)

		if response is not None:
			finalResult = {'status': 200, 'content': {'itemID': response.id, 'description':response.description, 'price': response.price, 'customSku': response.customSku, 'archived': response.archived}}
		else:
			finalResult = {'status': 'Item could not be found'}

		return finalResult

	def delete_item(self, id):
		url = 'https://api.merchantos.com/API/Account/'+self.acnt+'/Item/'+id+'.json'
		

		

		### used with lightspeed api ###
		# response = requests.delete(url, auth=self.auth)
		# if response.status_code != 200:
		# 	print type(response.status_code)
		# 	if response.status_code == 404:
		# 		finalResult = {'status': 'Item could not be found'}
		# 	else:
		# 		finalResult = {'status': response.status_code, 'error': errorsDictionary[response.status_code]}
		# else:
		# 	finalResult = {'status': response.status_code, 'content':response.content}

		###  ###

		fake_api_request_delay = time.sleep(random.random() * 2.5 + 0.5)
		response = InventoryItem.objects.get(id=id)
		response.archived = True
		response.save()
		finalResult = {'status': 200}

		return finalResult

	def create_sku(self):
		sku_chars = string.digits
		sku = "4"

		for _ in range(11):
			sku += random.choice(sku_chars)

		check_digit = 0
		for idx in range(len(sku)):
			if idx % 2 == 0:
				check_digit += int(sku[idx])
			else:
				check_digit += 3 * int(sku[idx])
		check_digit = 10 - (check_digit % 10)
		if check_digit == 10:
			check_digit = 0
		sku += str(check_digit)

		return sku

	def create_item(self, description, price, username,quantity):
		sku = self.create_sku()

		url = 'https://api.merchantos.com/API/Account/'+self.acnt+'/Item.json'
		pythonDictionary = {}
		pythonDictionary["description"] = description
		pythonDictionary["customSku"] = sku
		pythonDictionary['ItemShops'] = {}
		pythonDictionary['ItemShops']['ItemShop'] = {}
		pythonDictionary['ItemShops']['ItemShop']['qoh'] = quantity
		pythonDictionary['ItemShops']['ItemShop']['shopID'] = 1
		pythonDictionary['Prices'] = {}
		pythonDictionary['Prices']['ItemPrice']={}
		pythonDictionary['Prices']['ItemPrice']['amount'] = price
		pythonDictionary['Prices']['ItemPrice']['useType'] = "Default"
		pythonDictionary['Prices']['ItemPrice']['useTypeID'] = 1
		#bad stuff, trying to break it
		# pythonDictionary['Tags'] = []
		# pythonDictionary['Tags'].append("squiddy")
		# done trying to break it
		#trying to add tags -- the good stuff
		pythonDictionary['Tags'] = {}
		pythonDictionary['Tags']['@attributes'] = {"count":1}
		pythonDictionary['Tags']['tag'] = username

		#done adding tags == the good stuff

		### used with lightspeed api ###
		# json_data = json.dumps(pythonDictionary)
		# response = requests.post(url, auth=self.auth, data=json_data)
		
		# if response.status_code != 200:
		# 	finalResult = {'status': errorsDictionary[response.status_code]}
		# 	return finalResult

		# finalResult = {'status': response.status_code, 'bikeAdded': pythonDictionary}
		### ###

		response = InventoryItem()
		response.description = description
		response.price = price
		response.customSku = sku
		response.save()

		# random delay between ~0.5 and 3 seconds
		fake_api_request_delay = time.sleep(random.random() * 2.5 + 0.5)

		finalResult = {'status': 200, 'bikeAdded': pythonDictionary}
		
		return finalResult
