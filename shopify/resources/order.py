from ..base import ShopifyResource
from shopify import mixins
from .transaction import Transaction
from .fulfillment_order import FulfillmentOrder

class Order(ShopifyResource, mixins.Metafields, mixins.Events):

    def close(self):
        self._load_attributes_from_response(self.post("close"))

    def open(self):
        self._load_attributes_from_response(self.post("open"))

    def cancel(self, **kwargs):
        self._load_attributes_from_response(self.post("cancel", **kwargs))

    def transactions(self):
        return Transaction.find(order_id=self.id)

    def capture(self, amount=""):
        return Transaction.create({"amount": amount, "kind": "capture", "order_id": self.id})

    def fulfillment_orders(self, **kwargs):
        return FulfillmentOrder.find(from_="%s/orders/%s/fulfillment_orders.json" % (
            ShopifyResource.site, self.id), **kwargs)

