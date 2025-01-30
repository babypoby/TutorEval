from openai import OpenAI
import pandas as pd
import base64
client = OpenAI()

try:
    # List 10 fine-tuning jobs


    retrieval = client.fine_tuning.jobs.retrieve("ftjob-bQMoDs5VhVw7TPeZd7G2CQoa")
    print("Retrieval:", retrieval)

    result_file_id = "ffile-Ev2xgSqcPwTA3538x1E2NP"
    

    # Retrieve and save the result file
    response = client.files.content(result_file_id)
    #print(response.text)
    print(base64.b64decode(response.text))

    with open("result.csv", "wb") as f:
      f.write(base64.b64decode(response.text))




# Print the contents of the file

except Exception as e:
    print("An error occurred:", e)

