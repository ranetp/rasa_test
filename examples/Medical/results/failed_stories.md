## End-to-End tests where a custom action appends events (C:\Users\Ranet\AppData\Local\Temp\tmpc5hoy3eo\b46a7efe10274d648f958ff479134110_conversation_tests.md)
* inform: Hello. My name is Janek Sepp (ID code: 38906090245). I am currently suffering from a 38.5C fever.   <!-- predicted: inform: Hello. My name is [Janek Sepp](personal_name) (ID code: [38906090245](personal_id)). I am currently suffering from [a 38.5C fever](medical_issue). -->
    - slot{"medical_issue": "a 38.5C fever"}
    - slot{"personal_id": "38906090245"}
    - slot{"personal_name": "Janek Sepp"}
    - utter_slots_values_medical   <!-- predicted: utter_goodbye -->
    - action_search_medical_advice
    - action_suggest_medical_advice
* affirm: thanks
    - utter_happy


