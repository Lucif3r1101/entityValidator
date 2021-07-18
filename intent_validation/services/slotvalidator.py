from abc import ABCMeta, abstractmethod

"""
    This module provides the metaclass ABCMeta for defining ABCs and a helper class ABC to alternatively define ABCs through inheritance
    Methods : Finite Values Entity
            : Validate Numeric Constraints Entity
"""

class SlotValidator(metaclass=ABCMeta):
    @abstractmethod
    def validate_finite_values_entity(self, values, supported_values, invalid_trigger, key, support_multiple,
                                      pick_first, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def validate_numeric_constraints_entity(self, values, invalid_trigger, key, support_multiple, pick_first,
                                            constraint, var_name, **kwargs):
        raise NotImplementedError
