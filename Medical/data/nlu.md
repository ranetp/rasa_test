## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- thanks
- thank you
- thank you very much

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really


## intent:inform
<!-- Currently 5 medical issues:
- Runny nose/rhinorrhea
- Cough/coughing
- Fever/high temperature
- Sore throat/throat ache/raw throat
- Nausea/dizzyness/dizzy -->
- My name is [Karl Robin](personal_name), my ID is [34806272729](personal_id) and I have a [runny nose](medical_issue)
- My name is [Hugo Rasmus](personal_name), my ID is [37306172235](personal_id) and my nose is [runny](medical_issue)
- My name is [Mattias Oliver](personal_name), my ID is [36004182221](personal_id) and I have a high [fever](medical_issue)
- [Oskar Aron](personal_name), [35411272720](personal_id) and I'm feeling [nauseous](medical_issue)
- [Henri Nikita](personal_name), [36112032755](personal_id) and I'm feeling [dizzy](medical_issue)
- [Artjom Kristofer](personal_name), [36812156010](personal_id) and I'm feeling [dizzyness](medical_issue)
- I'm experiencing a [cough](medical_issue). Name: [Romet Robert](personal_name), id: [39011050304](personal_id).
- I'm cant stop [coughing](medical_issue). Name: [Mark Markus](personal_name), id: [36910280288](personal_id).
- I have a whooping [cough](medical_issue). Name: [Gregor Aleksandr](personal_name), id: [38603026516](personal_id).
- I'm [coughing](medical_issue) my brains out. Name: [Maksim Sebastian](personal_name), id: [36303210352](personal_id).
- I have a [fever of 39 C](medical_issue). My name is [Ralf Timur](personal_name) and my id is [36303050379](personal_id) i think.
- I have a [fever of 39.3C](medical_issue). My name is [Artur Kaspar](personal_name) and my id is [37411092737](personal_id) i think.
- My [fever is 39.2C](medical_issue). My name is [Kirill Marten](personal_name) and my id is [38709184221](personal_id) i think.
- I have a bad [39.4C fever](medical_issue). My name is [Uku Daniil](personal_name) and my id is [38709184221](personal_id) i think.
- I have a [fever of 37.5 C](medical_issue). My name is [Johannes Lukas](personal_name) and my id is [37008044225](personal_id) i think.
- I have a [fever of 37.3 degrees](medical_issue). My name is [Jakob Ivanov](personal_name) and my id is [38708270377](personal_id) i think.
- I have a [37.7 fever](medical_issue). My name is [Georg Tamm](personal_name) and my id is [37408200331](personal_id) i think.
- I have a [fever of 40C](medical_issue). My name is [Kevin Saar](personal_name) and my id is [36101122222](personal_id) i think.
- I have a [37.9 fever](medical_issue). My name is [Daniel Sepp](personal_name) and my id is [34908184247](personal_id) i think.
- My ([David Mägi](personal_name), [36812156010](personal_id)) nose is very [runny](medical_issue)
- My ([Sofia Smirnov](personal_name), [38709184221](personal_id)) nose is [runny](medical_issue)
- My ([Mia Vasiliev](personal_name), [36112032755](personal_id)) nose is in the state of [runnyness](medical_issue)
- My ([Maria Petrov](personal_name), [37411092737](personal_id)) [runny nose](medical_issue) is killing me
- My ([Eliise Kask](personal_name), [35411272720](personal_id)) [nose runny](medical_issue).
- My ([Laura Kukk](personal_name), [34908184247](personal_id)) cant stop [running](medical_issue)
- My ([Nora Kuznetsov](personal_name), [36303210352](personal_id)) nose is very [rhinorrheay](medical_issue)
- My name is [Emily Rebane](personal_name)
- My name is [Mirtel Ilves](personal_name)
- My name is [Milana Mihhailov](personal_name)
- My name is [Emma Pärn](personal_name)
- My name is [Saskia Pavlov](personal_name)
- [Marta Semenov](personal_name)
- I'm called [Lenna Koppel](personal_name)
- I'm called [Olivia Andreev](personal_name)
- I'm called [Adeele Alekseev](personal_name)
- I'm called [Emilia Luik](personal_name)
- I'm called [Saara Kaasik](personal_name)
- [Arina Lepik](personal_name)
- [Sandra Oja](personal_name)
- [Veronika Raudsepp](personal_name)
- [Eva Kuusk](personal_name)
- [Alisa Karu](personal_name)
- [Anna Fjodorov](personal_name)
- [Polina Nikolaev](personal_name)
- [Stella Kütt](personal_name)
- [Amelia Põder](personal_name)
- [Elisabeth Vaher](personal_name)
- [Elli Popov](personal_name)
- [Hanna Stepanov](personal_name)
- [Iiris Volkov](personal_name)
- [Isabel Moroz](personal_name)
- [Marleen  Lepp](personal_name)
- [Melissa Koval](personal_name)
- [Viktoria Kivi](personal_name)
- [Annabel Kallas](personal_name)
- I have a [fever of 37.5 C](medical_issue)
- I got a [fever of 38.5 C](medical_issue)
- I have a [fever of 39.5 C](medical_issue)
- I got a [fever of 39.3 C](medical_issue)
- I have a [fever of 39.5 C](medical_issue)
- I seem to have a [fever of 37.3 C](medical_issue)
- I have a [fever](medical_issue)
- I got a [fever](medical_issue)
- I have a [fever of 37.5](medical_issue)
- I got a [fever of 37.5](medical_issue)
- I have a [38.5 C fever](medical_issue)
- I got a [39.5 C fever](medical_issue)
- I have a [37.1 C fever](medical_issue)
- I got a [37.2 C fever](medical_issue)
- I have a [runny nose](medical_issue)
- I got a [runny nose](medical_issue)
- I have a [cough](medical_issue)
- I got a [cough](medical_issue)
- I have a [sore throat](medical_issue)
- I got a [sore throat](medical_issue)
- I have a [throat ache](medical_issue)
- I got a [throat ache](medical_issue)
- My id is [36812156010](personal_id)
- My id is [38709184221](personal_id)
- My personal id is [36112032755](personal_id)
- My personal id is [37411092737](personal_id)
- [35411272720](personal_id)
- [34908184247](personal_id)
- [36303210352](personal_id)

<!-- Entity roles/groups https://rasa.com/docs/rasa/nlu/entity-extraction/#entities-roles-and-groups -->
- I would like to get health insurance for traveling from [Estonia]{"entity": "country", "role": "origin"} to [Finland]{"entity": "country", "role": "destination"}.
- I'd like to get health insurance for traveling from [Latvia]{"entity": "country", "role": "origin"} to [Lithuania]{"entity": "country", "role": "destination"} please.
- I want to insure my health for traveling from [Poland]{"entity": "country", "role": "origin"} to [France]{"entity": "country", "role": "destination"} please.
- I'm going to go to [Denmark]{"entity": "country", "role": "destination"} from [Sweden]{"entity": "country", "role": "origin"} and I'd like some health insurance.
- Could I get insurance for going to [Norway]{"entity": "country", "role": "destination"} from [Germany]{"entity": "country", "role": "origin"}?
- Is it possible to get health insurance for flight from [Russia]{"entity": "country", "role": "origin"} to [China]{"entity": "country", "role": "destination"} somehow?
- Hello. I'm looking for health insurance, because I want to travel to [Morocco]{"entity": "country", "role": "destination"}. I am currently in [France]{"entity": "country", "role": "origin"}.
- I am from [Belarus]{"entity": "country", "role": "origin"} and I want to go to [Spain]{"entity": "country", "role": "destination"}. Can I get some health insurance?
- Hello I want health insurance.
- I am going to go on a travel trip, and I'd like health insurance.
- I'd like health insurance.
- I want to go to [Japan]{"entity": "country", "role": "destination"}. How do i get insurance?
- Ill depart from [Korea]{"entity": "country", "role": "origin"}
- I'm from [Yemen]{"entity": "country", "role": "origin"}
- I'm in [Turkey]{"entity": "country", "role": "origin"}
- oh, im currently in [Brazil]{"entity": "country", "role": "origin"}
- Ill travel to [United States]{"entity": "country", "role": "destination"}
- I'd like to insure my trip to [Germany]{"entity": "country", "role": "destination"} 
- I'm going to [Latvia]{"entity": "country", "role": "destination"}
- I'm going to [Latvia]{"entity": "country", "role": "destination"}
- I want to go to [United Kingdom]{"entity": "country", "role": "destination"}
- Ill go to [Britain]{"entity": "country", "role": "destination"}
- I am from [New Zealand]{"entity": "country", "role": "origin"}, I'd like some health insurance
<!-- Regex for personal_id (still need to provide training examples) -->
<!-- Regex assistance only works with CRFEntityExtractor  -->
## regex:personal_id
- [3-6]{1}[0-9]{2}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}[0-9]{4}
