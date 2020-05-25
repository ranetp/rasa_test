#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## Registration path 1 (Just for entities - I don't understand how to test forms with multile/follow up questions and don't want to waste more time on this. The docs only have an example with one question https://rasa.com/docs/rasa/user-guide/testing-your-assistant/)
* greet: Hello!
  - utter_greet
* request_registration: I'm fine thanks. I'd like to register an account.
  - registration_form
  - form{"name": "registration_form"}
* inform: The name of my company is [Rimi](organisation_name).
    - registration_form
* inform: Its located in [Estonia](country).
    - registration_form
* inform: The address is [Pärnu mnt 130-40](company_address)
    - registration_form
* inform: The name of my food handling place is [Tatari Rimi](organisation_name)
    - registration_form
* inform: Its in [Finland](country)
    - form{"name": null}
* affirm: Yes, thanks
  - utter_happy

## Ask for help affirm
* greet: Hello!
  - utter_greet
* asks_about_main_activity: I'd like to know more about the main activity of a food handling place
  - utter_explain_main_activity
  - utter_did_that_help
* asks_about_location_type: What about the food handling place location type?
  - utter_explain_location_type
  - utter_did_that_help
* affirm: Yes, thank you!
  - utter_happy

## Ask for help negative
* greet: Hello!
  - utter_greet
* asks_about_location_type: What is the food handling place location type?
  - utter_explain_location_type
  - utter_did_that_help
* deny: No, I still don't understand
  - utter_apologize
  - utter_offer_to_connect_with_human
