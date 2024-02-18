class Item:
    
    def __init__(self, itemID, itemName, price, quantity):
        self.itemID = itemID
        self.itemName = itemName
        self.price = price
        self.quantity = quantity
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        
        
    def calculate_total_cost(self, quantity):
        return self.quantity * self.price
    
    def printItem(self):
        return 'ID = '+ str(self.itemID)+' Name = '+ self.itemName+ ' price = '+str(self.price)+ ' quantity = '+str(self.quantity)
        
        
class PerishableItem (Item):
    
    def __init__(self, itemID, itemName, price, quantity, expiryDate):
        Item.__init__(self, itemID, itemName, price, quantity)
        self.expiryDate = expiryDate
        
    def setExpiryDate(self, expiryDate):
        self.expiryDate = expiryDate
    
    def checkExpiry(self, currentDate):
        if currentDate > expirydate:
            return "expired"
        else:
            return "not expired"

    def printItem(self):
        return super().printItem()+' expiryDate = '+str(self.expiryDate)
    
        
class NonPerishableItem(Item):
    
    def __init__(self, itemID, itemName, price, quantity, weight):
        Item.__init__(self, itemID, itemName, price, quantity)
        self.weight = weight
        
    def calculate_shipping_cost (self, shippingRate):
        return self.weight*shippingRate

    def printItem(self):
        return super().printItem()+' weight = '+str(self.weight)
    
class Inventory:
    
    def __init__(self):
        self.itemList=[]
        
    def add_item(self, item):
        self.itemList.append(item)
        
    def update_item_quantity(self, itemID, newQuantity):
        for xItem in self.itemList:
            if xItem.itemID == itemID:
                xItem.quantity = newQuantity
                break
    
    def removeItem(self, itemID):
        for i in range(len(self.itemList)):
            if self.itemList[i].itemID == itemID:
                self.itemList.pop(i)
                break
    
    def displayInventory(self):
        print('======Printing Inventory======')
        for xItem in self.itemList:
            print(xItem.printItem())
        print('======Printing Done=======')
        


myInventory = Inventory()

pItem = PerishableItem(1,"fruit",1,10,123)

npItem = NonPerishableItem(2, "car",1000,2,5000)

print('Lets add a perishable item to the Inventory')
myInventory.add_item(pItem)

print('Lets add a non-perishable item to the Inventory')
myInventory.add_item(npItem)

print("Here's what the inventory looks like")
myInventory.displayInventory()

print("Updating the quantity of the perishable item")
myInventory.update_item_quantity(1,0)

print("Here's what the inventory looks like")
myInventory.displayInventory()

print("Let's remove the perisbale item")
myInventory.removeItem(1)

print("Here's what the inventory looks like")
myInventory.displayInventory()
