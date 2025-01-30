import ollama
from supabase import create_client, Client
import random


url: str = "https://jryeokpjkidbgzscmrcj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpyeWVva3Bqa2lkYmd6c2NtcmNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU5ODQ3NjIsImV4cCI6MjA0MTU2MDc2Mn0.nLeYIrrnbkSVqKeY7XOZkgHxDYwDcQOSVwmzrZgQrMo"

supabase: Client = create_client(url, key)

supa_response = supabase.table("text_data").select("*").execute()
data = supa_response.data
data = random.sample(data, 100)


modelfile= '''
FROM llama3.1:8b
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student’s mistake. You should answer „Yes“, „No“ or „Not Applicable“. Answer „Yes“ if: the Tutor points out the mistake or opportunities for improvement, the Tutor identifies and addresses the Student's misconceptions, the Tutor asks a question which draws attention to the mistake. Answer „No“ if: The Tutor states that the Student's statement is right even though it is not, The Tutor does not point out the mistake directly or not at all, The Tutor gives the right answer without pointing out what was wrong, The Tutor states that the Student's statement is wrong without pointing out what was wrong. Answer „Not Applicable“ if: It is not clear whether the Student made a mistake, The Student's statement does not contain an answer to a question
MESSAGE user STUDENT: Okay I think thylakoid are the cells that contain the chlorophyll in the chloroplast. The stacks of thylakoid are called grana. TUTOR: Almost there! Thylakoids aren't cells, they are organelles within cell, but everything else is correct. Nicely done!
MESSAGE assistant Yes
MESSAGE user STUDENT: I need to multiply everything out so I get (x+3)∗ (x−1) = x^2− 3. TUTOR: That's great! You need to multiply everything out! Would you like another question?
MESSAGE assistant No
MESSAGE user STUDENT: If I push a 2kg object with a force of 10N it will accelerate with 10/2=5m/s! TUTOR: Nicely done, you applied Newton's law F=m∗a correctly! The answer 5 is correct too, but take another look at the units m/s. Are those the correct units for acceleration?
MESSAGE assistant Yes
'''


ollama.create(model='rubric5_vanilla', modelfile=modelfile)

i = 0
j = 0
for text in data:
    full_conversation =[{"role": "user", "content": text['text']}]
    response = ollama.chat(model='rubric5_vanilla', messages=full_conversation)
    print (f"Conversation {i}")
    print( f"Conversation ID: {text['conversation_id']}")
    my_result = supabase.table("rating").select("rubric_5").eq('conversation_id', text['conversation_id']).execute().data
    print (my_result)
    if ((my_result[0]['rubric_5'] != response['message']['content']) and (my_result[1]['rubric_5'] != response['message']['content'])):
        j = j + 1
        print(f"Rating was {my_result[0]['rubric_5']} and {my_result[1]['rubric_5']} but the model predicted {response['message']['content']}")
    i = i + 1

print (f"Number of wrong answers: {j}")