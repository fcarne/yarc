def guarded(condition, default_return=None):
    def decorator(method):
        def guarded_method(*args, **kwargs):
            if callable(condition):
                should_call = condition()
            else:
                should_call = condition

            if should_call:
                return method(*args, **kwargs)
            else:
                return default_return

        return guarded_method

    return decorator
