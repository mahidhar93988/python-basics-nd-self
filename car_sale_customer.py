# car_sale_customer
# Your class should be named `CarSell`.
# Your method should be named `getPromisingCustomers`
# Your method should return the indices of customers who are willing to pay greater than or equal to 90% of the car value
class Carsell:
    def __init__(self, all_proposals):
        self.proposals = all_proposals

    def getPromisingCustomers(self):
        res = []
        for i in range(len(self.proposals)):
            if(self.proposals[i] >= 900000):
                res.append(i)
            if(len(res) == 0):
                return([-1])
        return(res)


if __name__ == "__main__":
    num_customers = int(input())
    customer_proposals = []
    for i in range(num_customers):
        customer_proposals.append(int(input()))

    car_sell = Carsell(customer_proposals)
    for j in car_sell.getPromisingCustomers():
        print(j)
