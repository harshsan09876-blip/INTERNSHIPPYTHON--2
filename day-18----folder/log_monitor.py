import re
#iss module ka use searching karne liye karte hai

import time
#iss module ka use loop chalane ke liye karte hai 

import logging

#configuration

LOG_FILE = "application.log"
ERROR_THRESHOLD = 3
CHECK_INTERVAL = 2

#humnee file ko configure kiya hai aur errorgenerate hai 3 and interval check is 2

#logging setup 
logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# humne data ko logging karne ka amtalab data ko save karna hai aur permanently fetch karna via server

def monitor_log():
    error_count = 0
    
    
    with open(LOG_FILE, "r")as file:
        #move to the end of the file
        file.seek(0, 2)
        
        print("log monitoring system started....")
        print("waiting for new log entries...")
        
        
        while True:
            line = file.readline()
            
            if not line:
                time.sleep(CHECK_INTERVAL)
                continue
            
            #FIND error pttern using regex
            
            if re.search(r"\bERROR\b", line,re.IGNORECASE):
                error_count += 1
                
                print("Error detected: ", line.strip())
                
                
                logging.info(f"Error detected.Error count:{error_count}")
                
                #check wwthetr the threshold is reached
                if error_count >= ERROR_THRESHOLD:
                    alert = (f"ALERT!Error threshold reached:"
                             f"{error_count}errors detected."
                    )
                    
                    print(alert)
                    logging.warning(alert)
                    
                    #reset counter afetr alert
                    error_count = 0
                    
                    monitor_log()
                    