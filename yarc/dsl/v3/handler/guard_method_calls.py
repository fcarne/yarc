def guard_method_calls(condition):
    def decorator(cls):
        class GuardedClass(cls):
            def __getattribute__(self, name):
                attr = super().__getattribute__(name)
                if callable(attr):

                    def guarded(*args, **kwargs):
                        if callable(condition):
                            should_call = condition()
                        else:
                            should_call = condition

                        if should_call:
                            return attr(*args, **kwargs)
                        else:
                            return None

                    return guarded
                else:
                    return attr

        return GuardedClass

    return decorator
