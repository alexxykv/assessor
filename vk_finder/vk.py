import vk_api
from .access_token import SUPER_SECRET_TOKEN


def _get_api():
    vk_session = vk_api.VkApi(token=SUPER_SECRET_TOKEN)
    api = vk_session.get_api()
    return api

vk = _get_api()
