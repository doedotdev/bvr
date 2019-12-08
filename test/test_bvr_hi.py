import logging
from bvr.bvr_hi import bvr_hi


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_bvr_hi_called_as_decorator(caplog):

    @bvr_hi
    def hi():
        return 2

    return_value = hi()

    assert return_value == 2
    assert hi.__name__ == "hi"  # Important for decorators to not override method name

    assert len(caplog.records) == 2
    assert caplog.records[0].msg == 'Hi'
    assert caplog.records[0].levelname == 'INFO'
    assert caplog.records[1].msg == 'Hi'
    assert caplog.records[1].levelname == 'INFO'


def test_bvr_hi_called_as_callable_returning_decorator(caplog):

    @bvr_hi()
    def hi():
        return 2

    return_value = hi()

    assert return_value == 2
    assert hi.__name__ == "hi"  # Important for decorators to not override method name

    assert len(caplog.records) == 2
    assert caplog.records[0].msg == 'Hi'
    assert caplog.records[0].levelname == 'INFO'
    assert caplog.records[1].msg == 'Hi'
    assert caplog.records[1].levelname == 'INFO'


def test_bvr_hi_called_as_decorator_with_function_args(caplog):

    @bvr_hi
    def hi(msg):
        logger.info(msg)
        return msg

    return_value = hi("Hello")

    assert return_value == "Hello"
    assert hi.__name__ == "hi"  # Important for decorators to not override method name

    assert len(caplog.records) == 3
    assert caplog.records[0].msg == 'Hi'
    assert caplog.records[0].levelname == 'INFO'
    assert caplog.records[1].msg == 'Hello'
    assert caplog.records[1].levelname == 'INFO'
    assert caplog.records[2].msg == 'Hi'
    assert caplog.records[2].levelname == 'INFO'


def test_bvr_hi_called_as_callable_returning_decorator_with_function_args(caplog):

    @bvr_hi()
    def hi(msg):
        logger.info(msg)
        return msg

    return_value = hi("Hello")

    assert return_value == "Hello"
    assert hi.__name__ == "hi"  # Important for decorators to not override method name

    assert len(caplog.records) == 3
    assert caplog.records[0].msg == 'Hi'
    assert caplog.records[0].levelname == 'INFO'
    assert caplog.records[1].msg == 'Hello'
    assert caplog.records[1].levelname == 'INFO'
    assert caplog.records[2].msg == 'Hi'
    assert caplog.records[2].levelname == 'INFO'
