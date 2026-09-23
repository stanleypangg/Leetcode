class Order:
    def __init__(self, orderType, price):
        self.orderType = orderType
        self.price = price

class OrderManagementSystem:

    def __init__(self):
        self.orders = {}
        self.order_ids_by_type_and_price = defaultdict(lambda: defaultdict(set))

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        # orderId -> (orderType, price)
        order = Order(orderType, price)
        self.orders[orderId] = order
        self.order_ids_by_type_and_price[orderType][price].add(orderId)

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        # order.price = newPrice
        order = self.orders[orderId]
        orderType = order.orderType
        oldPrice, order.price = order.price, newPrice

        orders_at_old_price = self.order_ids_by_type_and_price[orderType][oldPrice]
        orders_at_old_price.remove(orderId)

        orders_at_new_price = self.order_ids_by_type_and_price[orderType][newPrice]
        orders_at_new_price.add(orderId)

    def cancelOrder(self, orderId: int) -> None:
        # del order[orderId]
        order = self.orders[orderId]
        price = order.price
        orderType = order.orderType

        del self.orders[orderId]
        self.order_ids_by_type_and_price[orderType][price].remove(orderId)

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        # order[orderType][price]
        return list(self.order_ids_by_type_and_price[orderType][price])

# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)