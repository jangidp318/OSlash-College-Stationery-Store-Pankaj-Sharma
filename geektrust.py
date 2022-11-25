from sys import argv

Cart = []
Products = {
    "TSHIRT":{
        "category":"Clothing",
        "orgPrice":1000,
        "discount":10,
    },
    "JACKET":{
        "category":"Clothing",
        "orgPrice":2000,
        "discount":5,
    },
    "CAP":{
        "category":"Clothing",
        "orgPrice":500,
        "discount":20,
    },
    "NOTEBOOK":{
        "category":"Stationery",
        "orgPrice":200,
        "discount":20,
    },
    "PENS":{
        "category":"Stationery",
        "orgPrice":300,
        "discount":10,
    },
    "MARKERS":{
        "category":"Stationery",
        "orgPrice":500,
        "discount":5,
    },
}


def addItem(ItemName, Quantity):
    if (Products[ItemName]["category"] == "Stationery" and int(Quantity)<=3) or (Products[ItemName]["category"] == "Clothing" and int(Quantity)<=2):
        Cart.append({"itemName":ItemName, "quantity":Quantity})
        print("ITEM_ADDED")
    else:
        print("ERROR_QUANTITY_EXCEEDED")

def additionDiscount(subTotal):
    subTotalAfterAdditionalDiscount = subTotal - ((5/100)*subTotal)
    additionDiscount = ((5/100)*subTotal)
    return subTotalAfterAdditionalDiscount, additionDiscount

def calculateTax(subTotal):
    subTotalAfterTax = subTotal + ((10/100)*subTotal)
    tax = ((10/100)*subTotal)
    return subTotalAfterTax, tax

def CalculateBill():
    subTotal,discount,CartValue,discount,totalDiscount=0.0,0.0,0.0,0.0,0.0
    for item in Cart:
        amountPerItem = (Products[item["itemName"]]["orgPrice"])*float(item["quantity"])
        discountPerItem =(Products[item["itemName"]]["discount"]/100)*(Products[item["itemName"]]["orgPrice"])*float(item["quantity"])
        discount += discountPerItem
        # print("amountPerItem",amountPerItem)
        CartValue +=amountPerItem
    
    if(CartValue >= 1000):
        subTotal = CartValue - discount
        totalDiscount = discount
    else:
        subTotal = CartValue
    # Additional Discount
    if(subTotal>=3000):
        subTotal, AddDis = additionDiscount(subTotal)
        totalDiscount = discount + AddDis

    print("TOTAL_DISCOUNT",totalDiscount)
    # print("subTotal",subTotal)

    #Subtotal After Sales Tax
    totalAmtToPay, Tax = calculateTax(subTotal)

    print("Total_AMOUNT_TO_PAY",totalAmtToPay)
    

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        # Add your code here to process input commands.
        lineCommands= line.split(" ")
        if lineCommands[0] == "ADD_ITEM": #Adding Item in Cart
            addItem(lineCommands[1], lineCommands[2]) 
        else:
            CalculateBill()
    output = "" #process the input command and get the output
    # Once it is processed print the output using the command System.out.println()
    print(output)
    # print("Cart",Cart)
    
if __name__ == "__main__":
    main()