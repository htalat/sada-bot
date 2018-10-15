## say bye
* bye
	- utter_bye

## add a purchase
* greet
	- utter_greet
* start_purchase_flow
	- utter_ask_item
* enter_data
	- action_store_item
	- slot{"item": "cocomo"}
	- utter_ask_place
* enter_data
	- action_store_place
	- slot{"place": "general store"}
	- utter_ask_amount
* enter_data
	- action_store_amount
	- slot{"amount": "100"}
	- utter_ask_note
* enter_data
	- action_store_note
	- slot{"note": "a note"}
	- action_store_info
	- utter_store_info

## list purchases
* greet
	- utter_greet
* start_list_purchase_flow
	- action_list_purchases
	- utter_list_purchases