## say goodbye
* goodbye
  - utter_goodbye


## Ask for medical advice
* inform{"personal_name": "Mark Markus", "medical_issue": "runny_nose", "personal_id": "35411272720"}
    - utter_slot_values_medical
    - action_search_medical_advice
    - action_suggest_medical_advice
* affirm
  - utter_happy


## Ask for medical advice
* inform{"personal_name": "Toomas Laanelaia", "medical_issue": "37.8C fever", "personal_id": "38906070254"}
    - utter_slot_values_medical
    - action_search_medical_advice
    - action_suggest_medical_advice
* deny
  - utter_goodbye


## Ask about insurance
* inform{"country": "Estonia", "role": "origin", "country": "Lithuania", "role": "destination"}
  - insurance_form
  - form{"name": "insurance_form"}
  - form{"name": null}
  - utter_slot_values_insurance
* affirm
  - utter_goodbye
