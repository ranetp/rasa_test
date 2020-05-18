## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot


## asks for help path 1
* greet
    - utter_greet
* asks_help
    - utter_offer_help


## asks about main activity positive
* greet
    - utter_greet
* asks_about_main_activity
    - utter_explain_main_activity
    - utter_did_that_help
* affirm
  - utter_happy


## asks about main activity negative
* greet
    - utter_greet
* asks_about_location_type
    - utter_explain_location_type
    - utter_did_that_help
* deny
  - utter_apologize
  - utter_offer_to_connect_with_human

## asks about location type positive
* greet
    - utter_greet
* asks_about_location_type
    - utter_explain_location_type
    - utter_did_that_help
* affirm
  - utter_happy


## asks about location type negative
* greet
    - utter_greet
* asks_about_location_type
    - utter_explain_location_type
    - utter_did_that_help
* deny
  - utter_apologize
  - utter_offer_to_connect_with_human


## Ask about account registering success
* greet
    - utter_greet
* request_registration
    - registration_form
    - form{"name": "registration_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_did_that_help
* affirm
  - utter_happy

## Ask about account registering negative
* greet
    - utter_greet
* request_registration
    - registration_form
    - form{"name": "registration_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_did_that_help
* deny
  - utter_apologize
  - utter_offer_to_connect_with_human
