from main import get_api1, get_api2

tasks = [get_api1, get_api2]

for i in range(100):
    # launching tasks one by one
    tasks[i % 2].apply_async(queue='token')

