from abc import ABCMeta, abstractmethod

class Order(object):
    def __init__(self, shipper):
        self._shipper = shipper

    @property
    def shipper(self):
        return self._shipper


class Shipper(object):
    fedex = 1
    ups = 2
    postal = 3


class ShippingCost(object):

    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)

        elif order.shipper == Shipper.ups:
            return self._ups_cost(order)

        elif order.shipper == Shipper.postal:
            return self._postal_cost(order)

        else:
            raise ValueError('Invalid shipper %s' % order.shipper)

    def _fedex_cost(self, order):
        return 3.00

    def _ups_cost(self, order):
        return 4.00

    def _postal_cost(self, order):
        return 5.00


class ShippingCost1(object):
    def __init__(self, strategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)


class AbsStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""


class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.00

class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 4.00

class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00



if __name__ == '__main__':
    #Test Federal Express shipping

    order = Order("Federal")
    strategy = FedExStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 3.0


    #Test UPS shipping

    order = Order("UPS")
    strategy = UPSStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 4.0

    #Test Postal Service shipping

    order = Order("Postal")
    strategy = PostalStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 5.0

    print("All tests done")
