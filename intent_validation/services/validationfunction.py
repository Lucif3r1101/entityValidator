from intent_validation.services.slotvalidator import SlotValidator

from typing import List, Dict, Tuple

from intent_validation.values.values import Values as val


class ValidationFunction(SlotValidator):

    
    
    SlotValidationResult = Tuple[bool, bool, str, Dict]

    """
    Validate an entity on the basis of its value extracted.
    The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param supported_values: List of supported values for the slot
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :return: a tuple of (filled, partially_filled, trigger, params)
    """

    
    

    def validate_finite_values_entity(self, values: List[Dict], supported_values: List[str] = None,
                                      invalid_trigger: str = None, key: str = None, support_multiple: bool = True,
                                      pick_first: bool = False, **kwargs) -> SlotValidationResult:
       
        filled, partially_filled, trigger, params = False, False, invalid_trigger, {}
        count, n, arr = 0, len(values), []
        for each in values:
            if each[val.staticValue] in supported_values:
                count += 1
                arr.append(each[val.staticValue].upper())
        if 0 < n == count:
            filled = True
            trigger = ''
            params = {key: arr[0]} if pick_first else {key: arr}
        else:
            if n:
                partially_filled = True
        return filled, partially_filled, trigger, params


    

    def validate_numeric_constraints_entity(self, values: List[Dict], invalid_trigger: str = None, key: str = None,
                                            support_multiple: bool = True, pick_first: bool = False, constraint=None,
                                            var_name=None, **kwargs) -> SlotValidationResult:
                                            
        """
            Validate an entity on the basis of its value extracted.
            The method will check if that value satisfies the numeric constraints put on it.
            If there are no numeric constraints, it will simply assume the value is valid.

            If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
            In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
            will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.

            If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be
            partially filled.

            :param pick_first: Set to true if the first value is to be picked up
            :param support_multiple: Set to true if multiple utterances of an entity are supported
            :param values: Values extracted by NLU
            :param invalid_trigger: Trigger to use if the extracted value is not supported
            :param key: Dict key to use in the params returned
            :param constraint: Conditional expression for constraints on the numeric values extracted
            :param var_name: Name of the var used to express the numeric constraint
            :return: a tuple of (filled, partially_filled, trigger, params)
        """
        
        
        
        filled, partially_filled, trigger, params = False, False, '', {}
        count, n, arr = 0, len(values), []
        for each in values:
            if constraint is None:
                count += 1
                arr.append(each[val.staticValue])
                continue
            exp = constraint.replace(var_name, str(each[val.staticValue]))
            if eval(exp):
                count += 1
                arr.append(each[val.staticValue])
        if 0 < n == count:
            filled = True
            params = {key: arr[0]} if pick_first else {key: arr}
        else:
            trigger = invalid_trigger
            if n:
                partially_filled = True
            if count > 0 and support_multiple:
                params = {key: arr[0]} if pick_first else {key: arr}
        return filled, partially_filled, trigger, params
