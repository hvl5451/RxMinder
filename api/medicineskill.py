# class for handling and directing the right request and building the skill from echo
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

from .models import PillDetails


sb = SkillBuilder()


class ListAllintent(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("ListAll")(handler_input)

    def handle(self, handler_input):
        speech_text = "The following is the list of medicines you take, "
        for items in PillDetails.objects.all():
            speech_text = items + ', '
        handler_input.response_builder.speak(speech_text).set_should_end_session(True)
        return handler_input.response_builder.response

class DailyDosage(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("DailyDosage")(handler_input)

    def handle(self, handler_input):
        pass
