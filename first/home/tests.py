from nsetools import Nse
 
# creating a Nse object
nse = Nse()
 
# getting quote of the sbin
quote = nse.get_quote('sbin')
 
# printing company name
print(quote['companyName'])
 
# printing buy price
print("Buy Price : " + str(quote['buyPrice1']))