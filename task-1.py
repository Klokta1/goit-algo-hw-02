import queue
import random
import time

request_queue = queue.Queue()

request_counter = 1

def generate_request():
    global request_counter
    new_request = f"Request #{request_counter}"
    request_queue.put(new_request)
    print(f"Заявка {new_request} додана до черги.")
    request_counter += 1

def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Обробка {current_request}...")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Заявка {current_request} оброблена.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

try:
    while True:
        generate_request()
        process_request()
        time.sleep(random.uniform(1, 3))

except KeyboardInterrupt:
    print("Програма завершена.")
