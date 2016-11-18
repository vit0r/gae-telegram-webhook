# -*- coding: utf-8 -*-

from tg_send import TGHookSend
from nose.tools import assert_equals


def test():
    # set your chat id to receive message here
    your_chat_id = None
    result = TGHookSend.send_text_message(message='hello =)', chat_id=your_chat_id)
    assert_equals(result.__getitem__(0).status, 200)


# call send message test
test()


def test_set_web_hook():
    result = TGHookSend.send_web_hook()
    assert_equals(result.__getitem__(0).status, 200)

# test_set_web_hook()
