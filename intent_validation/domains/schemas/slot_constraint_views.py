from marshmallow import Schema, fields, post_load, INCLUDE
from intent_validation.domains.domain.slot_constraints import SlotConstraints

"""
        Deserialize JSON data into python object.
        :param data: object
        :param kwargs: extra parameters
        :return: SlotConstraints object
"""


class SlotConstraintViews(Schema):
   
    values = fields.List(fields.Dict(), required=True)
    invalid_trigger = fields.Str(required=True)
    key = fields.Str(required=True)
    support_multiple = fields.Bool(missing=True)
    pick_first = fields.Bool(missing=False)
    constraint = fields.Str(missing=None)
    var_name = fields.Str(required=True)

    @post_load()
    def make_entity_obj(self, data, **kwargs):
        
        return SlotConstraints(**data)

    class Meta:
        unknown = INCLUDE
