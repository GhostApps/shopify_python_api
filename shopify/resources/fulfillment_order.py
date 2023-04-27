from ..base import ShopifyResource
from .location import Location
import json

class FulfillmentOrder(ShopifyResource):

    @classmethod
    def find(cls, key=None, **kwargs):
        order_id = kwargs.get("order_id")
        if order_id:
            return super(FulfillmentOrder, cls).find(from_="%s/orders/%s/fulfillment_orders.json" % ( cls.site, order_id), **kwargs) 
        else:
            return super(FulfillmentOrder, cls).find(key)
    
    @classmethod
    def locations_for_move(cls, key=None, **kwargs):
        return Location.find(from_="%s/fulfillment_orders/%s/locations_for_move.json" % (
            ShopifyResource.site, key), **kwargs)

    def cancel(self):
        self._load_attributes_from_response(self.post("cancel"))

    def close(self):
        self._load_attributes_from_response(self.post("close"))

    def move(self, new_location_id, fulfillment_order_line_items = []):
        body = { 'fulfillment_order' : { 'new_location_id' : new_location_id } }
        if fulfillment_order_line_items:
            body['fulfillment_order']['fulfillment_order_line_items'] = fulfillment_order_line_items
        self.post("move", body=json.dumps(body).encode())
