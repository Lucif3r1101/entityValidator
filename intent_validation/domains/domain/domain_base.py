class DomainBase:

    """
    BaseDomain Class to act as a deserializer
    """
    
    def __init__(self, values, invalid_trigger, key, support_multiple, pick_first):
        self.values = values
        self.invalid_trigger = invalid_trigger
        self.key = key
        self.support_multiple = support_multiple
        self.pick_first = pick_first
