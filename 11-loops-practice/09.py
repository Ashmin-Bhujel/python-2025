# Exponential Backoff
# TODO: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time

waiting_time = 1
max_retries = 5
attemps = 0


while attemps < max_retries:
    print(f"Attemp: {attemps + 1}, Waiting time: {waiting_time}s")
    time.sleep(waiting_time)
    waiting_time *= 2
    attemps += 1
