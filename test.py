import time

print("We will show you what number you are thinking about.")
me = input("Enter number a number: ")
print("Thinking...")
time.sleep(3)  # Delay for 3 seconds
print(f"The number you were thinking about is: {me}")
print("Wait, let me double-check...")
time.sleep(2)  # Add suspense
print("Accessing your mind...")
time.sleep(2)
print("Analyzing brain waves...")
time.sleep(2)
print("Got it!")
time.sleep(1)
print(f"The number you were thinking about is definitely: {me}")
