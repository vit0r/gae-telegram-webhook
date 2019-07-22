# -*- coding: utf-8 -*-

import yaml
from httplib2 import Http


class TGHookSend(object):
    @classmethod
    def get_http(cls):
        """Send http request without validade ssl certificate"""
        http = Http()
        http.force_exception_to_status_code = True
        http.disable_ssl_certificate_validation = True
        return http

    @classmethod
    def get_conf(cls):
        """Get values from file bot_conf.yaml"""
        try:
            with open('bot_conf.yaml', mode='r') as bot_conf:
                return yaml.safe_load(bot_conf)['bot_conf']
        except ValueError as ex:
            raise ex

    @staticmethod
    def send_web_hook():
        """Set your bot in endpoit api"""
        try:
            bot_conf = TGHookSend.get_conf()
            set_web_hook = '{}{}?url={}'.format(bot_conf['apiTelegramUrl'], bot_conf['token'], bot_conf['yourEndPoint'])
            TGHookSend.get_http().request(set_web_hook, method='GET')
        except ValueError as ex:
            raise ex

    @staticmethod
    def send_text_message(message, chat_id):
        """Send message to chat id"""
        try:
            bot_conf = TGHookSend.get_conf()
            http = TGHookSend.get_http()
            msg = str(message).replace(' ', bot_conf['urlSpaceCode'])
            telegram_url = '{}{}{}?chat_id={}&text={}'.format(bot_conf['apiTelegramUrl'], bot_conf['token'],
                                                              bot_conf['sendMessage'],
                                                              chat_id, msg)
            return http.request(telegram_url, method='GET')
        except ValueError as ex:
            raise ex
