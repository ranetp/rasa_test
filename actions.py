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

from typing import List, Text, Dict, Any, Union

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

        always_required = [
            'company_address',
            'company_num_food_locations',
            'food_place_team_size',
            'food_place_main_activity',
            'food_place_type_of_location',
            'food_place_additional_activities',
        ]

        required_slots = always_required
        # In order to avoid both slots with same entities getting filled from a single question
        # See https://forum.rasa.com/t/using-a-single-entity-for-different-form-slots/29000/4
        if tracker.get_slot('company_name') is None:
            # Set it as the first question question, as the list order matters
            required_slots = ['company_name'] + required_slots
        else:
            ind = required_slots.index('company_num_food_locations') + 1
            required_slots.insert(ind, 'food_place_name')

        if tracker.get_slot('company_country') is None:
            # Set it before the question
            ind = required_slots.index('company_address')
            required_slots.insert(ind, 'company_country')
        else:
            ind = required_slots.index('food_place_name') + 1
            required_slots.insert(ind, 'food_place_country')


        return required_slots


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        '''Define what the form has to do after all required slots are filled'''

        dispatcher.utter_template('utter_submit', tracker)
        return []


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        '''A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message or a list of them, where a first match will be picked'''

        return {
            'company_name': self.from_entity(entity='organisation_name'),
            'food_place_name': self.from_entity(entity='organisation_name'),
            'company_country': self.from_entity(
                entity='country',
                intent=['inform']
            ),
            'food_place_country': self.from_entity(
                entity='country',
                intent=['inform']
            )
        }
