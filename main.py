### VK thinkerBOT

### Импортируем либы Вконтакте, и модуль с двумя классами. Бот будет через Longpoll #####
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import _botFunc
import time

# Уазать token и screen_name
vk_session = vk_api.VkApi(token='', api_version=5.95)
vk = vk_session.get_api()
vkDict = vk.utils.resolveScreenName(screen_name='')
vkIdCommunities = vkDict.get('object_id')
longpoll = VkBotLongPoll(vk_session, vkIdCommunities)

def _letActivatemod(thisMessage):
	""" Функция вызыввает основную функцию обработчик, атрибутом принимает сообщение ВК и передает его.
	"""
	fromModule = _botFunc._letAcceptmessageVK(thisMessage)
	return fromModule


def _letprintActivity():
	""" Включает набор сообщения.
	"""
	vk.messages.setActivity(type='typing', peer_id=event.object.peer_id)


for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW:
		vk.messages.markAsRead(message_ids=event.object.message_id, peer_id=event.object.peer_id)
		### Для беседы модуль пока не сделан, только 1 на 1.
		if event.object.peer_id != event.object.from_id: # Conference
			if event.object.text.lower() == "Привет":
				vk.messages.send(peer_id=event.object.peer_id, message="Приветствую!", random_id=0)

		elif event.object.peer_id == event.object.from_id:
			inmessageVK = event.object.text.lower().split()
			_letprintActivity()
			oitgoingMessage = _letActivatemod(inmessageVK)
			while True:
				_letprintActivity()
				if oitgoingMessage:
					vk.messages.send(user_id=event.object.from_id, message=oitgoingMessage, random_id=0)
					break
