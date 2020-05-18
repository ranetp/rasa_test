# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import List, Text, Dict, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class RegistrationForm(FormAction):
    '''Example of a custom form action'''

    def name(self):
        '''Unique identifier of the form'''
        return 'registration_form'


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        '''A list of required slots that the form has to fill'''

        return [
            'company_name',
            'company_country',
            'company_address',
            'company_num_food_locations',
            'food_place_name',
            'food_place_country',
            'food_place_team_size',
            'food_place_main_activity',
            'food_place_type_of_location',
            'food_place_additional_activities',
        ]


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        '''Define what the form has to do after all required slots are filled'''

        dispatcher.utter_template('utter_submit', tracker)
        return []
