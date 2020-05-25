## Registration path 1 (Just for entities - I don't understand how to test forms with multile/follow up questions and don't want to waste more time on this. The docs only have an example with one question https://rasa.com/docs/rasa/user-guide/testing-your-assistant/) (C:\Users\Ranet\AppData\Local\Temp\tmptlrrmr5t\238c9332ae954a9aa589550e5cf1ac37_conversation_tests.md)
* greet: Hello!
    - utter_greet
* request_registration: I'm fine thanks. I'd like to register an account.
    - registration_form
    - form{"name": "registration_form"}
* form: inform: The name of my company is [Rimi](organisation_name).
    - form: registration_form
* form: inform: Its located in [Estonia](country).
    - form: registration_form
* form: inform: The address is [Pärnu mnt 130-40](company_address)
    - form: registration_form
* form: inform: The name of my food handling place is [Tatari Rimi](organisation_name)
    - form: registration_form
* form: inform: Its in [Finland](country)
    - form{"name": null}
    - action_listen   <!-- predicted: registration_form -->
* affirm: Yes, thanks
    - utter_happy


## Ask for help negative (C:\Users\Ranet\AppData\Local\Temp\tmptlrrmr5t\238c9332ae954a9aa589550e5cf1ac37_conversation_tests.md)
* greet: Hello!
    - utter_greet
* asks_about_location_type: What is the food handling place location type?
    - utter_explain_location_type
    - utter_did_that_help
* deny: No, I still don't understand   <!-- predicted: asks_about_location_type: No, I still don't understand -->
    - utter_apologize   <!-- predicted: utter_explain_location_type -->
    - utter_offer_to_connect_with_human


