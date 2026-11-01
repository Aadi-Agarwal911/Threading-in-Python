import threading
import time

def download_file():
    print("Downloading file...")
    time.sleep(3) 
    print("File downloaded!")

def process_data():
    print("Processing data...")
    time.sleep(2) 
    print("Data processed!")

def send_email():
    print("Sending emails...")
    time.sleep(1)
    print("Emails sent!")

thread1 = threading.Thread(target=download_file)
thread2 = threading.Thread(target=process_data)
thread3 = threading.Thread(target=send_email) 

thread1.start()
thread2.start()
thread3.start() 

thread1.join()
thread2.join()
thread3.join()

print("All tasks finished!")