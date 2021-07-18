from intent_validation.domains.domain.slot_values_domain import SlotValuesDomain

from marshmallow import Schema, fields, post_load, INCLUDE

"""
        Deserialize JSON data into python object.
        :param data: object data
        :param kwargs: extra parameters
        :return: SlotValuesViews object
"""


class SlotValuesViews(Schema):
    
    values = fields.List(fields.Dict(), required=True)
    invalid_trigger = fields.Str(required=True)
    key = fields.Str(required=True)
    support_multiple = fields.Bool(missing=True)
    pick_first = fields.Bool(missing=False)
    supported_values = fields.List(fields.Str(), required=True)

    @post_load()
    def make_entity_obj(self, data, **kwargs):
        return SlotValuesDomain(**data)

    class Meta:
        unknown = INCLUDE
