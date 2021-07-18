from intent_validation.domains.domain.domain_base import DomainBase
from intent_validation.domains.domain.domain_base import DomainBase

"""
    SlotValuesDomain extending common values from DomainBase.
    Used to create value similar to json object
"""

class SlotValuesDomain(DomainBase):
    
    def __init__(self, values, supported_values, invalid_trigger, key, support_multiple, pick_first, **kwargs):
        super().__init__(values, invalid_trigger, key, support_multiple, pick_first)
        self.supported_values = supported_values
