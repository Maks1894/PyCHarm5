import time

def monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            status = "Success"
            return result
        except Exception as e:
            status = f"Error: {e}"
        finally:
            end_time = time.time()

            log_line = (f" Nazwa funkcji {func.__name__}, czas rozpoczęcia {start_time:.4f} seconds, czas  zakończenia {end_time:.4f} seconds, "
                        f"Arguments: {args}, {kwargs} Status: {status}")
            with open("monitoring.log", "a+") as log:
                log.write(log_line + "\n")
    return wrapper