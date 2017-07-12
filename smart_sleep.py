def smart_sleep(to_try, on_exception, max_tries=5, max_period=60,
                init_argument=1.0, value_func=None, *args, **kwargs):
    import datetime
    start = datetime.datetime.now()
    if value_func is None:
        value_func = lambda x: x * 2

    tried = 0
    while True:
        try:
            to_return = to_try(*args, **kwargs)

        except Exception as e:
            on_exception(e)
            # Raising an exception will break the loop
            if tried == max_tries:
                raise

            time_elapsed = datetime.datetime.now() - start
            if time_elapsed.total_seconds() >= max_period:
                raise

            time.sleep(init_argument)  # Block thread for init_argument
            init_argument = value_func(init_argument)

            continue  # Try one more time
        else:
            return to_return  # Break the loop and return result if no errors
