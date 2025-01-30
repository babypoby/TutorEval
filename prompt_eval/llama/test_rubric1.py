import ollama
from supabase import create_client, Client
import random


url: str = "https://jryeokpjkidbgzscmrcj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpyeWVva3Bqa2lkYmd6c2NtcmNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU5ODQ3NjIsImV4cCI6MjA0MTU2MDc2Mn0.nLeYIrrnbkSVqKeY7XOZkgHxDYwDcQOSVwmzrZgQrMo"

supabase: Client = create_client(url, key)

supa_response = supabase.table("text_data").select("*").execute()
data = supa_response.data
data = random.sample(data, 100)


modelfile_1= '''
FROM llama3.1:8b
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. They should instead guide the student to come to the correct solution themselves by giving them hints or asking additional questions. For the given conversation, your task is to determine if the Tutor gives away the answer at their specific point of progress in the conversation. You should answer „Yes“, „No“, or „Not Applicable“. You should  answer „Yes" in the following situations: If the Tutor gives away the full correct solution directly and explicitly. You should answer „No“ in the following situations: All situations where the Tutor doesn’t give away the full correct solution directly. If the Student’s statement is partially true, and the Tutor confirms it, but does not give away the rest of the solution. If the Tutor says that the Student is incorrect, and/or explains why the student’s answer is incorrect, without telling the correct solution. If the Tutor hints or implies the correct solution without giving it away fully. If the Tutor asks a question guiding to the correct solution without saying the correct solution. If the Tutor asks the Student to explain their solution. You should  „Not Applicable“ if it is impossible to answer the question. For example if the Student is correct and/or the Tutor confirms that the Student is fully correct. Notice that you should answer „Not Applicable“ and „Yes“ not so often since these situations are exceptions.
MESSAGE user STUDENT: Will a glass with ice cubes overflow when the cubes melt? TUTOR: No, it won't since the amount of water displaced by the cubes initially is the same as the amount of water they add when they melt.
MESSAGE assistant Yes
MESSAGE user TUTOR: walk me through STUDENT: Blake gave Connie $x initially and the land tripled in value, so Connie sold it for $60,000. She gave half of the money to Blake, which was $30,000, so that means $x + $30,000 = $60,000. To find out how much Blake initially gave Connie, we need to subtract $30,000 from both sides, so $x = $60,000 - $30,000 = $40,000. TUTOR: f $60,000 is triple what Connie bought the land for, then the initial cost, which is the amount given to her by Blake, was $60,000/3 = $20,000. 20,000
MESSAGE assistant Yes
MESSAGE user TUTOR: Happy to work with you today! TUTOR: Today, let us review and master the lesson "Rounding Whole Numbers." TUTOR: Which is the greatest number among 5 and 3? STUDENT: 4 TUTOR: Your answer is incorrect. You have earned 1 point for your effort. 5 is the greatest among 5 and 3. Here is our first question. I will explain this question to you. Before that, Many students like to talk with their tutors during the session.
MESSAGE assistant Yes
MESSAGE user TUTOR: Your answer is nearly right! We just need to focus on the last part. you added the sum but if she's baked cakes she'll be taking away from the numbers so 15 cakes take away the five she made is? STUDENT: Oh, right! So Louise needs to bake 15-5 = 10 more cakes. 10 TUTOR: Absolutely!
MESSAGE assistant Not Applicable
MESSAGE user TUTOR: What is the x-axis value? TUTOR: Sorry, we are running out of time. TUTOR: What is the final answer to this question? STUDENT: -4 5 TUTOR: Ah, we may have gotten our x and y coordinates mixed up. Remember that the first coordinate is the x, which tells us how far left/right from the center we go. The second coordinate is the y, which tells us how far up/down from the center we go. Looking at the dot, how far left/right from the center is it?
MESSAGE assistant No
MESSAGE user STUDENT: What is the correct syntax for comparing strings in Python? TUTOR: Have you compared other things before in Python?
MESSAGE assistant No
MESSAGE user TUTOR: You have the correct answer in there but your final answer is incorrect. Have another look and see if you can identify where you have gone wrong STUDENT: Oh, I see. I was multiplying the wrong numbers. The correct answer should be 0.14. 0.2 (know Excel) x 0.7 (willing to work nights) = 0.14 TUTOR: No, you have multipled correctly. But your final working out is incorrect
MESSAGE assistant No
MESSAGE user TUTOR: Hi , could you please walk me through your ? STUDENT: Sure. In September, Julie earned 25 x $4 = $100 for mowing lawns. In September, Julie earned 3 x $8 = $24 for pulling weeds. In September, Julie earned a total of $100 + $24 = $124. If Julie worked the same number of hours in October, she would earn the same amount, $124. Therefore, Julie earned $124 in September and October combined. TUTOR: how much money did she earn in September and October refers to what is the total amount of money earned by her in september and october collectively.
MESSAGE assistant No
MESSAGE user TUTOR: Hello Michael can you walk me through your workings? STUDENT: Sure. I started by calculating the number of M&Ms that Colleen added to the batch. She added 108/3 = 36 M&Ms. Then, I added the total number of chocolate pieces (108 + 36 = 144). Finally, I divided the total number of pieces by the number of cookies (144/48 = 3). This means that the average number of chocolate pieces in each cookie is 3 - 1 = 2. TUTOR: Brilliant. This is great. If we are looking for the average number of chocolate pieces (which includes chocolate chips and M&M's) what is the average?
MESSAGE assistant No
MESSAGE user TUTOR: JIan please walk me through your answer STUDENT: I started by figuring out how many mistakes Leo had. Since Madeline had half as many mistakes, I knew that Leo had 4 mistakes. Then I figured out that Brent had 1 more mistake than Leo, so he had 5 mistakes. I then knew that Brent had 25 points, so each correct answer was worth 5 points. Then I figured out that Madeline had 5 correct answers (5 x 5 = 25) and 2 mistakes, so her total score was 15 out of 20 possible points. TUTOR: I like how you were able to identify the total number of mistakes made by each student.
MESSAGE assistant No
MESSAGE user TUTOR: Go ahead and give your best. STUDENT: c TUTOR: Is that your final answer? STUDENT: yes TUTOR: Well tried! One point for your effort. What is the value of 7x9?
MESSAGE assistant No
MESSAGE user TUTOR: TUTOR: Any questions so far [STUDENT]? STUDENT: no TUTOR: Alright. Mike has 4 cookies and he eats 3 cookies. So Mike has ______ cookie left? STUDENT: He has 10 cookies left. TUTOR: That is incorrect. What operation would you use to solve this problem?
MESSAGE assistant No
MESSAGE user TUTOR: Let me know if you need any help along. TUTOR: Read the question carefully. TUTOR: Is that your final answer? STUDENT: yes TUTOR: Great try! When we find area we can count the total number of boxes. How many total boxes are within the rectangle?
MESSAGE assistant No
PARAMETER temperature 0.8

'''

modelfile_2 = '''
FROM llama3.1:8b
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor gives away the answer at their specific point of progress in the conversation. You should answer „Yes“, „No“, or „Not Applicable“. You should answer "Yes" if the Tutor gives away the correct answer directly and explicitly. You should answer „No“ for all situations where the Student made an error and the Tutor doesn’t give away the correct answer directly. You should answer „Not Applicable“ if the question is not applicable in the current conversation.
MESSAGE user STUDENT: Will a glass with ice cubes overflow when the cubes melt? TUTOR: No, it won't since the amount of water displaced by the cubes initially is the same as the amount of water they add when they melt.
MESSAGE assistant Yes
MESSAGE user TUTOR: walk me through STUDENT: Blake gave Connie $x initially and the land tripled in value, so Connie sold it for $60,000. She gave half of the money to Blake, which was $30,000, so that means $x + $30,000 = $60,000. To find out how much Blake initially gave Connie, we need to subtract $30,000 from both sides, so $x = $60,000 - $30,000 = $40,000. TUTOR: f $60,000 is triple what Connie bought the land for, then the initial cost, which is the amount given to her by Blake, was $60,000/3 = $20,000. 20,000
MESSAGE assistant Yes
MESSAGE user TUTOR: Happy to work with you today! TUTOR: Today, let us review and master the lesson "Rounding Whole Numbers." TUTOR: Which is the greatest number among 5 and 3? STUDENT: 4 TUTOR: Your answer is incorrect. You have earned 1 point for your effort. 5 is the greatest among 5 and 3. Here is our first question. I will explain this question to you. Before that, Many students like to talk with their tutors during the session.
MESSAGE assistant Yes
MESSAGE user TUTOR: Your answer is nearly right! We just need to focus on the last part. you added the sum but if she's baked cakes she'll be taking away from the numbers so 15 cakes take away the five she made is? STUDENT: Oh, right! So Louise needs to bake 15-5 = 10 more cakes. 10 TUTOR: Absolutely!
MESSAGE assistant Not Applicable
MESSAGE user TUTOR: What is the x-axis value? TUTOR: Sorry, we are running out of time. TUTOR: What is the final answer to this question? STUDENT: -4 5 TUTOR: Ah, we may have gotten our x and y coordinates mixed up. Remember that the first coordinate is the x, which tells us how far left/right from the center we go. The second coordinate is the y, which tells us how far up/down from the center we go. Looking at the dot, how far left/right from the center is it?
MESSAGE assistant No
MESSAGE user STUDENT: What is the correct syntax for comparing strings in Python? TUTOR: Have you compared other things before in Python?
MESSAGE assistant No
MESSAGE user TUTOR: You have the correct answer in there but your final answer is incorrect. Have another look and see if you can identify where you have gone wrong STUDENT: Oh, I see. I was multiplying the wrong numbers. The correct answer should be 0.14. 0.2 (know Excel) x 0.7 (willing to work nights) = 0.14 TUTOR: No, you have multipled correctly. But your final working out is incorrect
MESSAGE assistant No
MESSAGE user TUTOR: Hi , could you please walk me through your ? STUDENT: Sure. In September, Julie earned 25 x $4 = $100 for mowing lawns. In September, Julie earned 3 x $8 = $24 for pulling weeds. In September, Julie earned a total of $100 + $24 = $124. If Julie worked the same number of hours in October, she would earn the same amount, $124. Therefore, Julie earned $124 in September and October combined. TUTOR: how much money did she earn in September and October refers to what is the total amount of money earned by her in september and october collectively.
MESSAGE assistant No
MESSAGE user TUTOR: Hello Michael can you walk me through your workings? STUDENT: Sure. I started by calculating the number of M&Ms that Colleen added to the batch. She added 108/3 = 36 M&Ms. Then, I added the total number of chocolate pieces (108 + 36 = 144). Finally, I divided the total number of pieces by the number of cookies (144/48 = 3). This means that the average number of chocolate pieces in each cookie is 3 - 1 = 2. TUTOR: Brilliant. This is great. If we are looking for the average number of chocolate pieces (which includes chocolate chips and M&M's) what is the average?
MESSAGE assistant No
MESSAGE user TUTOR: JIan please walk me through your answer STUDENT: I started by figuring out how many mistakes Leo had. Since Madeline had half as many mistakes, I knew that Leo had 4 mistakes. Then I figured out that Brent had 1 more mistake than Leo, so he had 5 mistakes. I then knew that Brent had 25 points, so each correct answer was worth 5 points. Then I figured out that Madeline had 5 correct answers (5 x 5 = 25) and 2 mistakes, so her total score was 15 out of 20 possible points. TUTOR: I like how you were able to identify the total number of mistakes made by each student.
MESSAGE assistant No
MESSAGE user TUTOR: Go ahead and give your best. STUDENT: c TUTOR: Is that your final answer? STUDENT: yes TUTOR: Well tried! One point for your effort. What is the value of 7x9?
MESSAGE assistant No
MESSAGE user TUTOR: TUTOR: Any questions so far [STUDENT]? STUDENT: no TUTOR: Alright. Mike has 4 cookies and he eats 3 cookies. So Mike has ______ cookie left? STUDENT: He has 10 cookies left. TUTOR: That is incorrect. What operation would you use to solve this problem?
MESSAGE assistant No
MESSAGE user TUTOR: Let me know if you need any help along. TUTOR: Read the question carefully. TUTOR: Is that your final answer? STUDENT: yes TUTOR: Great try! When we find area we can count the total number of boxes. How many total boxes are within the rectangle?
MESSAGE assistant No
PARAMETER temperature 0.8
'''

modelfile_3 = '''
FROM llama3.1:8b
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor gives away the answer. The Tutor must never give away the answer in full. Instead the Tutor must give hints or ask leading questions to help the Student find the solution by themselves. You should answer "Yes" if the Tutor gives away the answer, even if they ask a question afterward. If the Student’s statement is partially true, and the Tutor explains why it’s only partially correct or what the exceptions are, you should still answer „Yes“. You should answer „No“ if the Tutor doesn’t give away the answer or if the Student’s statement is partially true, and the Tutor confirms it, but does not give away the full answer. You should answer „Not Applicable“ when the question is not applicable in the situation. This can be cases where the student did not attempt to give an answer to a question in the previous utterance, or the Student is correct or when it is not clear whether the Student made a mistake. 
MESSAGE user STUDENT: Will a glass with ice cubes overflow when the cubes melt? TUTOR: No, it won't since the amount of water displaced by the cubes initially is the same as the amount of water they add when they melt.
MESSAGE assistant Yes
MESSAGE user TUTOR: walk me through STUDENT: Blake gave Connie $x initially and the land tripled in value, so Connie sold it for $60,000. She gave half of the money to Blake, which was $30,000, so that means $x + $30,000 = $60,000. To find out how much Blake initially gave Connie, we need to subtract $30,000 from both sides, so $x = $60,000 - $30,000 = $40,000. TUTOR: f $60,000 is triple what Connie bought the land for, then the initial cost, which is the amount given to her by Blake, was $60,000/3 = $20,000. 20,000
MESSAGE assistant Yes
MESSAGE user TUTOR: Happy to work with you today! TUTOR: Today, let us review and master the lesson "Rounding Whole Numbers." TUTOR: Which is the greatest number among 5 and 3? STUDENT: 4 TUTOR: Your answer is incorrect. You have earned 1 point for your effort. 5 is the greatest among 5 and 3. Here is our first question. I will explain this question to you. Before that, Many students like to talk with their tutors during the session.
MESSAGE assistant Yes
MESSAGE user TUTOR: Your answer is nearly right! We just need to focus on the last part. you added the sum but if she's baked cakes she'll be taking away from the numbers so 15 cakes take away the five she made is? STUDENT: Oh, right! So Louise needs to bake 15-5 = 10 more cakes. 10 TUTOR: Absolutely!
MESSAGE assistant Not Applicable
MESSAGE user TUTOR: What is the x-axis value? TUTOR: Sorry, we are running out of time. TUTOR: What is the final answer to this question? STUDENT: -4 5 TUTOR: Ah, we may have gotten our x and y coordinates mixed up. Remember that the first coordinate is the x, which tells us how far left/right from the center we go. The second coordinate is the y, which tells us how far up/down from the center we go. Looking at the dot, how far left/right from the center is it?
MESSAGE assistant No
MESSAGE user STUDENT: What is the correct syntax for comparing strings in Python? TUTOR: Have you compared other things before in Python?
MESSAGE assistant No
MESSAGE user TUTOR: You have the correct answer in there but your final answer is incorrect. Have another look and see if you can identify where you have gone wrong STUDENT: Oh, I see. I was multiplying the wrong numbers. The correct answer should be 0.14. 0.2 (know Excel) x 0.7 (willing to work nights) = 0.14 TUTOR: No, you have multipled correctly. But your final working out is incorrect
MESSAGE assistant No
MESSAGE user TUTOR: Hi , could you please walk me through your ? STUDENT: Sure. In September, Julie earned 25 x $4 = $100 for mowing lawns. In September, Julie earned 3 x $8 = $24 for pulling weeds. In September, Julie earned a total of $100 + $24 = $124. If Julie worked the same number of hours in October, she would earn the same amount, $124. Therefore, Julie earned $124 in September and October combined. TUTOR: how much money did she earn in September and October refers to what is the total amount of money earned by her in september and october collectively.
MESSAGE assistant No
MESSAGE user TUTOR: Hello Michael can you walk me through your workings? STUDENT: Sure. I started by calculating the number of M&Ms that Colleen added to the batch. She added 108/3 = 36 M&Ms. Then, I added the total number of chocolate pieces (108 + 36 = 144). Finally, I divided the total number of pieces by the number of cookies (144/48 = 3). This means that the average number of chocolate pieces in each cookie is 3 - 1 = 2. TUTOR: Brilliant. This is great. If we are looking for the average number of chocolate pieces (which includes chocolate chips and M&M's) what is the average?
MESSAGE assistant No
MESSAGE user TUTOR: JIan please walk me through your answer STUDENT: I started by figuring out how many mistakes Leo had. Since Madeline had half as many mistakes, I knew that Leo had 4 mistakes. Then I figured out that Brent had 1 more mistake than Leo, so he had 5 mistakes. I then knew that Brent had 25 points, so each correct answer was worth 5 points. Then I figured out that Madeline had 5 correct answers (5 x 5 = 25) and 2 mistakes, so her total score was 15 out of 20 possible points. TUTOR: I like how you were able to identify the total number of mistakes made by each student.
MESSAGE assistant No
MESSAGE user TUTOR: Go ahead and give your best. STUDENT: c TUTOR: Is that your final answer? STUDENT: yes TUTOR: Well tried! One point for your effort. What is the value of 7x9?
MESSAGE assistant No
MESSAGE user TUTOR: TUTOR: Any questions so far [STUDENT]? STUDENT: no TUTOR: Alright. Mike has 4 cookies and he eats 3 cookies. So Mike has ______ cookie left? STUDENT: He has 10 cookies left. TUTOR: That is incorrect. What operation would you use to solve this problem?
MESSAGE assistant No
MESSAGE user TUTOR: Let me know if you need any help along. TUTOR: Read the question carefully. TUTOR: Is that your final answer? STUDENT: yes TUTOR: Great try! When we find area we can count the total number of boxes. How many total boxes are within the rectangle?
MESSAGE assistant No
PARAMETER temperature 0.8'''

ollama.create(model='rubric1_vanilla_2', modelfile=modelfile_2)

i = 0
j = 0
for text in data:
    full_conversation =[{"role": "user", "content": text['text']}]
    response = ollama.chat(model='rubric1_vanilla_2', messages=full_conversation)
    print (f"Conversation {i}")
    print( f"Conversation ID: {text['conversation_id']}")
    print(response['message']['content'])
    my_result = supabase.table("rating").select("rubric_1").eq('conversation_id', text['conversation_id']).execute().data
    print (my_result)
    if ((my_result[0]['rubric_1'] != response['message']['content']) and (my_result[1]['rubric_1'] != response['message']['content'])):
        j = j + 1
        print(f"Rating was {my_result[0]['rubric_1']} and {my_result[1]['rubric_1']} but the model predicted {response['message']['content']}")
    i = i + 1

print (f"Number of wrong answers: {j}")