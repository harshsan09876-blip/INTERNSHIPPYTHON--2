import pandas as pd
import logging

#we are here to made the automatic gmail system 
# first step is to make calculation we install pandas
# then logging as because we want to record the data in to the excel sheet.

#configure logging
logging.basicConfig(filename="gmail_automation.log",
 level=logging.INFO,
    format="%(asctime)s - %(levelname)s-%(message)s"
)

try:
    #NOW WE ARE TRYING TO MAKE OUR DATA AS READABLE
    data = {
        "STUDENT":["ARIKA", "KANBAN", "AGILE"],
        "CGPA":[7.09, 8.09, 9.67],
        "SKILLS":[12, 14, 10]
    }
    # Create data frame
    df = pd.DataFrame(data)

    # Generate Excel report
    df.to_excel("business_report.xlsx", index=False)
    logging.info("Business report generated successfully.")
    print("The business report generated successfully")

except Exception as e:
    logging.error("Failed to generate business report: %s", e)
    
    