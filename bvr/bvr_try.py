from bvr.logger import Logger


def bvr_try(logger_class=None, exception_type=Exception, should_raise=True, custom_exception=None, custom_message=None):

    if not logger_class:
        logger_class = Logger()

    if not hasattr(logger_class, 'error'):
        print('logger_class fail')

    if not isinstance(exception_type, Exception.__class__):
        print('exception_type fail')

    if not isinstance(should_raise, bool):
        print(' should_raise fail')

    if not isinstance(custom_exception, Exception.__class__) or custom_exception is not None:
        print('custom_exception fail')

    if not isinstance(custom_message, str) or custom_message is not None:
        print('custom_message fail')

    def decorator(func):

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as exception:  # pylint: disable=broad-except

                msg = ("ERROR: Caught Exception | "
                       "FUNCTION: {} | "
                       "BASE_EXCEPTION: {} | "
                       "EXCEPTION: {} | "
                       "MESSAGE: {} | "
                       "RAISE: {} ").format(func.__name__,
                                            exception_type.__name__,
                                            type(exception).__name__,
                                            exception,
                                            should_raise)

                logger_class.error(msg)

                if should_raise is True:
                    if custom_exception:
                        raise custom_exception(msg) from exception

                    if not custom_exception:
                        raise

        return wrapper
    return decorator
