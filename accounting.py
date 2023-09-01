melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00


def customer_payments(filename):
    """Calculates cost of melons per customer and produces report of payment."""

    #Opens the file of customer data
    file = open(filename)   

    #Iterate through each line in file
    for line in file:

        data = line.split("|")   #Splits line at "|" into list of strings
        customer = data[1]      #Assign customer to index 1
        num_melons = float(data[2])    #Assign float number of melons
        customer_paid = float(data[3])  #Assign float customer payment
        
        customer_expected = num_melons * melon_cost   #Calculate price customer expected to pay

        if customer_expected != customer_paid:         #Check to see if price paid doen't match expected
            print(f"{customer} paid ${customer_paid:.2f},", #Prints out what customer paid vs expected
            f"expected ${customer_expected:.2f}")

            if customer_paid > customer_expected:       #If customer overpaid
                print(f"{customer} overpaid for their melons!")

            elif customer_paid < customer_expected:     #If customer underpaid
                print(f"{customer} underpaid for their melons!")

        else:
            print(f"{customer} paid the exact amount for their melons!")    #If customer paid exactly expected amount

    #Close the file
    file.close()


customer_payments("customer-orders.txt")   #Call function

