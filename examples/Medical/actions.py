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

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import random


class MedicalAPI:
    '''
    Can be used for external API calls, or even for querying elasticsearch.
    '''
    def search(self, medical_issue):
        employee_id = random.randrange(1, 10)
        try:
            data = requests.get(f'https://reqres.in/api/users/{employee_id}').json()['data']
            doctor = f"{data['first_name']} {data['last_name']}"
        except:
            doctor = 'Mr. Anonymous Doctor'

        advice = f'Doctor {doctor} suggests that the best way to treat {medical_issue} is to take antibiotics.'
        return doctor, advice


class ActionSearchMedicalData(Action):

    def name(self):
        return 'action_search_medical_advice'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text='Analyzing your medical data.')
        medical_api = MedicalAPI()
        doctor, advice = medical_api.search(tracker.get_slot('medical_issue'))

        # Set slot values programmatically
        return [SlotSet('advice', advice), SlotSet('doctor', doctor)]


class ActionGiveAdvice(Action):

    def name(self):
        return 'action_suggest_medical_advice'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text='Here is some medical advice:')
        dispatcher.utter_message(text=tracker.get_slot('advice'))

        # Create buttons dynamically through the action
        buttons = [
            {"title": f"Yes. I, {tracker.get_slot('personal_name')}, have my absolute trust in {tracker.get_slot('doctor')}",
             "payload": "/happy"
            },
            {"title": f"No. I, {tracker.get_slot('personal_name')}, don't trust no {tracker.get_slot('doctor')}",
             "payload": "/goodbye"
            }
        ]

        dispatcher.utter_button_message(
            f"Does this help? Or do you ({tracker.get_slot('personal_name')}, {tracker.get_slot('personal_id')}) doubt the advice of {tracker.get_slot('doctor')}?",
            buttons
        )

        return []
