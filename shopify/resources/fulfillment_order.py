from ..base import ShopifyResource
import json

class FulfillmentOrder(ShopifyResource):

    @classmethod
    def find(cls, key=None, **kwargs):
        order_id = kwargs.get("order_id")
        if order_id:
            return super(FulfillmentOrder, cls).find(from_="%s/orders/%s/fulfillment_orders.json" % ( cls.site, order_id), **kwargs) 
        else:
            return super(FulfillmentOrder, cls).find(key)
    

    def cancel(self):
        self._load_attributes_from_response(self.post("cancel"))

    def close(self):
        self._load_attributes_from_response(self.post("close"))

    def move(self, new_location_id):
        body = { 'fulfillment_order' : { 'new_location_id' : new_location_id } }
        self.post("move", body=json.dumps(body).encode())
