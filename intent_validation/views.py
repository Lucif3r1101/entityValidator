from intent_validation.values.values import Values as val
from intent_validation.domains.schemas.slot_constraint_views import SlotConstraintViews
from intent_validation.domains.schemas.slot_values_views import SlotValuesViews
from intent_validation.services.validationfunction import ValidationFunction

from marshmallow import INCLUDE, ValidationError
from rest_framework.response import Response

from rest_framework import status
from rest_framework.views import APIView


class SlotValues(APIView):
    def post(self, request):


        """
        Post API to validate an entity.
        :param request: request.
        :return: Response with either Error message and HTTP status 400 or a dictionary as follows -
                    {
                        "filled": <filled flag>,
                        "partially_filled": <partially filled>,
                        "trigger": <trigger value>,
                        "parameters": <params dict>
                    }
       """
        
        schema = SlotValuesViews()
        try:
            entity_obj = schema.load(request.data, unknown=INCLUDE)
        except ValidationError as e:
            return Response(data=e.messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            validator = ValidationFunction()
            res = validator.validate_finite_values_entity(**vars(entity_obj))
            return Response(
                {val.staticFilled: res[0], val.staticPartial: res[1], val.staticTrigger: res[2], val.staticParams: res[3]})




class SlotConstraints(APIView):
    def post(self, request):

        """
        POST API to validate the numeric constraints.
        :param request: request.
        :return: Response with either Error message and HTTP status 400 or a dictionary as follows -
                    {
                        "filled": <filled flag>,
                        "partially_filled": <partially filled flag>,
                        "trigger": <trigger value>,
                        "parameters": <params dict>
                    }
        """
       
        schema = SlotConstraintViews()
        try:
            entity_obj = schema.load(request.data, unknown=INCLUDE)
        except ValidationError as e:
            return Response(data=e.messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            validator = ValidationFunction()
            res = validator.validate_numeric_constraints_entity(**vars(entity_obj))
            return Response(
                {val.staticFilled: res[0], val.staticPartial: res[1], val.staticTrigger: res[2], val.staticParams: res[3]})


