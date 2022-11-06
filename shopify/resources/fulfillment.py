from ..base import ShopifyResource
import json


class FulfillmentV2(ShopifyResource):
    _singular = "fulfillment"
    _plural = "fulfillments"

    @classmethod
    def find(cls, key=None, **kwargs):
        order_id = kwargs.get("order_id")
        fulfillment_order = kwargs.get("fulfillment_order_id")
        if order_id:
            if key:
                return super(FulfillmentV2, cls).find_one(from_="%s/orders/%s/fulfillments/%s.json" % ( cls.site, order_id, key), **kwargs)
            else:   
                return super(FulfillmentV2, cls).find(from_="%s/orders/%s/fulfillments.json" % ( cls.site, order_id), **kwargs)
        elif fulfillment_order:
            return super(FulfillmentV2, cls).find(from_="%s/fulfillment_orders/%s/fulfillments.json" % ( cls.site, fulfillment_order), **kwargs) 

    def cancel(self):
        self._load_attributes_from_response(self.post("cancel"))

    def update_tracking(self, tracking_info, notify_customer):
        body = {"fulfillment": {"tracking_info": tracking_info, "notify_customer": notify_customer}}
        return self.post("update_tracking", json.dumps(body).encode())
