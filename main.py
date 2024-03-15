#starting of the project
import time 
from stopwatch import Stopwatch as prova 
print("hell ow")
print(
    """
    1: default settings 2: 25 minute focus 5 minute break 
    3: Custom time      4:Stop watch mode 
    """
)
user_input = input("Which mode do you want to select :")

if user_input == "4":
    st = prova()  # Instantiate the Stopwatch class with parentheses
    st.start()
    for i in range(100):
        print(st.elapsed_time(), end='\r')
        time.sleep(.2)