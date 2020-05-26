#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## End-to-End tests where a custom action appends events
* inform: Hello. My name is [Janek Sepp](personal_name) (ID code: [38906090245](personal_id)). I am currently suffering from [a 38.5C fever](medical_issue).
    - utter_slot_values_medical
    - action_search_medical_advice
    - action_suggest_medical_advice
* affirm: thanks
    - utter_happy


## Test insurance form
* inform: I'm from [Estonia](country) and I'd like to travel to [Finland](country). Could I have health insurance?
    - insurance_form
    - form{"name": "insurance_form"}
    - form{"name": null}
    - utter_slot_values_insurance
* affirm: thanks
    - utter_goodbye


## Test insurance form with extra questions
* inform: I'm going to [France](country) and I'd like some health insurance
    - insurance_form
    - form{"name": "insurance_form"}
    - form{"name": null}
    - utter_slot_values_insurance
* affirm: thanks
    - utter_goodbye
