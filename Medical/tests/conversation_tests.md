#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## End-to-End tests where a custom action appends events
* inform: Hello. My name is Janek Sepp (ID code: 38906090245). I am currently suffering from a 38.5C fever.
    - utter_slots_values_medical
    - action_search_medical_advice
    - action_suggest_medical_advice
* affirm: thanks
    - utter_happy
