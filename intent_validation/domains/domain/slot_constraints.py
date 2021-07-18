from intent_validation.domains.domain.domain_base import DomainBase

"""
    Slot Constraints domain takes common values from Base Domain.
"""

class SlotConstraints(DomainBase):
   
    def __init__(self, values, invalid_trigger, key, support_multiple, pick_first, constraint, var_name, **kwargs):
        super().__init__(values, invalid_trigger, key, support_multiple, pick_first)
        self.constraint = constraint
        self.var_name = var_name
