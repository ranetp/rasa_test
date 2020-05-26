## Registration path 1 (Just for entities - I don't understand how to test forms with multile/follow up questions and don't want to waste more time on this. The docs only have an example with one question https://rasa.com/docs/rasa/user-guide/testing-your-assistant/) (C:\Users\Ranet\AppData\Local\Temp\tmp0lxcdfhr\088d4f258f0f434aa0e7b9572a22c2f5_conversation_tests.md)
* greet: Hello!
    - utter_greet
* request_registration: I'm fine thanks. I'd like to register an account.
    - slot{"company_name": "Rimi"}
    - slot{"company_country": "Estonia"}
    - slot{"company_address": "Pärnu mnt 130-40"}
    - slot{"food_place_name": "Tatari Rimi"}
    - slot{"food_place_country": "Finland"}
    - slot{"food_place_country": "Finland"}
    - slot{"food_place_main_activity": "food_retail"}
    - slot{"food_place_type_of_location": "restaurant"}
    - slot{"food_place_additional_activities": "takeaway"}
    - slot{"food_place_team_size": "over5"}
    - slot{"company_num_food_locations": "over5"}
    - registration_form
    - form{"name": "registration_form"}
    - form: utter_slots_values   <!-- predicted: action_listen -->
    - form: utter_did_that_help   <!-- predicted: registration_form -->
    - form: action_listen   <!-- predicted: registration_form -->
* form: affirm: Yes, thanks
    - form: utter_happy -->   <!-- predicted: registration_form -->
    - form: action_listen   <!-- predicted: registration_form -->


