import logging
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ActionStorePlace(Action):
	"""Stores the users name in a slot"""

	def name(self):
		return "action_store_place"

	def run(self, dispatcher, tracker, domain):

		logger.info('storing place')
		place = next(tracker.get_latest_entity_values('place'), None)

		if not place:
			place = tracker.latest_message.get('text')

		return [SlotSet('place', place)]


class ActionStoreItem(Action):
	"""Stores the users name in a slot"""

	def name(self):
		return "action_store_item"

	def run(self, dispatcher, tracker, domain):

		logger.info('storing item')
		item = next(tracker.get_latest_entity_values('item'), None)

		if not item:
			item = tracker.latest_message.get('text')

		return [SlotSet('item', item)]


class ActionStoreAmount(Action):
	"""Stores the users name in a slot"""

	def name(self):
		return "action_store_amount"

	def run(self, dispatcher, tracker, domain):

		logger.info('storing amount')
		amount = next(tracker.get_latest_entity_values('amount'), None)

		if not amount:
			amount = tracker.latest_message.get('text')

		return [SlotSet('amount', amount)]


class ActionStoreNote(Action):
	"""Stores the users name in a slot"""

	def name(self):
		return "action_store_note"

	def run(self, dispatcher, tracker, domain):

		logger.info('storing note')
		note = next(tracker.get_latest_entity_values('note'), None)

		if not note:
			note = tracker.latest_message.get('text')

		return [SlotSet('note', note)]


class ActionStoreInfo(Action):

	def name(self):
		return "action_store_info"

	def run(self, dispatcher, tracker, domain):
		import datetime
		place = tracker.get_slot('place')
		amount = tracker.get_slot('amount')
		item = tracker.get_slot('item')
		note = tracker.get_slot('note')
		date = datetime.datetime.now().strftime("%d/%m/%Y")
		line_item = [date, place, item, amount, note]
		logger.info('storing the note! ')
		logger.info(line_item)


class ActionListPurchases(Action):
	"""Stores the users name in a slot"""

	def name(self):
		return "action_list_purchases"

	def run(self, dispatcher, tracker, domain):

		logger.info('listing purchases')
