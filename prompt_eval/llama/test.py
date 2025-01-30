import ollama
from supabase import create_client, Client
import random


url: str = "https://jryeokpjkidbgzscmrcj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpyeWVva3Bqa2lkYmd6c2NtcmNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU5ODQ3NjIsImV4cCI6MjA0MTU2MDc2Mn0.nLeYIrrnbkSVqKeY7XOZkgHxDYwDcQOSVwmzrZgQrMo"

supabase: Client = create_client(url, key)

supa_response = supabase.table("text_data").select("*").execute()
data = supa_response.data

modelfile_rubric1_repeat_default = '''
FROM llama3.1:8b-instruct-fp16
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. They should instead guide the student to come to the correct solution themselves by giving them hints or asking additional questions. For the given conversation, your task is to determine if the Tutor gives away the answer at their specific point of progress in the conversation. You may assume that in the current situation, the student is incorrect. You can assume that the Tutor always knows the correct solution. You should answer „Yes“ or „No“. You should  answer „Yes" in the following situations: If the Tutor gives away the full correct solution directly and explicitly. You should answer „No“ in the following situations: All situations where the Tutor doesn’t give away the full correct solution directly. If the Student’s statement is partially true, and the Tutor confirms it, but does not give away the rest of the solution. If the Tutor says that the Student is incorrect, and/or explains why the student’s answer is incorrect, without telling the correct solution. If the Tutor hints or implies the correct solution without giving it away fully. If the Tutor asks a question guiding to the correct solution without saying the correct solution. If the Tutor asks the Student to explain their solution. It is more often the case that the Tutor does not give away the answer directly and explicitly enough to answer "Yes", so you should answer "No" in most cases. 
MESSAGE user STUDENT: Will a glass with ice cubes overflow when the cubes melt? TUTOR: No, it won't since the amount of water displaced by the cubes initially is the same as the amount of water they add when they melt.
MESSAGE assistant Yes
MESSAGE user TUTOR: You have the correct answer in there but your final answer is incorrect. Have another look ands ee if you can identify where you have gone wrong STUDENT: Oh, I see. I was multiplying the wrong numbers. The correct answer should be 0.14. 0.2 (know Excel) x 0.7 (willing to work nights) = 0.14 TUTOR: No, you have multipled correctly. But your final working out is incorrect
MESSAGE assistant No
MESSAGE user TUTOR: The width of the line is 4 inches. STUDENT: TUTOR: How many equal pieces is the brick split into? STUDENT: 4 TUTOR: It was a good try. Plus 1 point for your active participation. The bricks is split into 2 parts. Since there are two equal pieces of brick and one of the two pieces is painted yellow, we can say that half of the brick is painted yellow.
MESSAGE assistant Yes
MESSAGE user TUTOR: Hi Mariana, please could you walk me through your solution? STUDENT: Sure, so first I calculated that 18 decks have a total of 55 x 18 = 990 cards. Then I realized that since Jame can tear 30 cards at a time, he needs to tear 990 cards / 30 cards per tear = 33 tears in total. After that, I figured out that if he tears cards 3 times a week, then he can tear 3 x 33 = 99 cards per week. Finally, I concluded that he can tear all 990 cards in 990 / 99 = 10 weeks. TUTOR: Okay, let's start from the beginning. How many cards can Jame tear in a week?
MESSAGE assistant No
MESSAGE user TUTOR: Happy to work with you today! TUTOR: Today, let us review and master the lesson "Rounding Whole Numbers." TUTOR: Which is the greatest number among 5 and 3? STUDENT: 4 TUTOR: Your answer is incorrect. You have earned 1 point for your effort. 5 is the greatest among 5 and 3. Here is our first question. I will explain this question to you. Before that, Many students like to talk with their tutors during the session.
MESSAGE assistant Yes
MESSAGE user TUTOR: What is the x-axis value? TUTOR: Sorry, we are running out of time. TUTOR: What is the final answer to this question? STUDENT: -4 5 TUTOR: Ah, we may have gotten our x and y coordinates mixed up. Remember that the first coordinate is the x, which tells us how far left/right from the center we go. The second coordinate is the y, which tells us how far up/down from the center we go. Looking at the dot, how far left/right from the center is it?
MESSAGE assistant No
MESSAGE user TUTOR: You have the correct answer in there but your final answer is incorrect. Have another look and see if you can identify where you have gone wrong STUDENT: Oh, I see. I was multiplying the wrong numbers. The correct answer should be 0.14. 0.2 (know Excel) x 0.7 (willing to work nights) = 0.14 TUTOR: No, you have multipled correctly. But your final working out is incorrect
MESSAGE assistant No
MESSAGE user TUTOR: Go ahead and give your best. STUDENT: c TUTOR: Is that your final answer? STUDENT: yes TUTOR: Well tried! One point for your effort. What is the value of 7x9?
MESSAGE assistant No
MESSAGE user TUTOR: TUTOR: Any questions so far [STUDENT]? STUDENT: no TUTOR: Alright. Mike has 4 cookies and he eats 3 cookies. So Mike has ______ cookie left? STUDENT: He has 10 cookies left. TUTOR: That is incorrect. What operation would you use to solve this problem?
MESSAGE assistant No
MESSAGE user TUTOR: can you walk me through your solution stepwise? STUDENT: Sure. I started by calculating the number of colored pencils in each pack, which was 3. Then I multiplied that by the number of packs, which was 15, to get 45. Then I calculated the number of extra red pencils, which was 3 x 2 = 6. So, I subtracted the extra red pencils from the total number of colored pencils to get 42. Finally, I added the 6 extra red pencils to get a total of 48 red colored pencils. TUTOR: lets start by finding out the number of red pencils without considering the extra ones.
MESSAGE assistant No
MESSAGE user TUTOR: can you tell me your solution STUDENT: Yes, I figured out that Randy had $3200 - $200 = $3000 before Smith gave him $200, so he had $3000 - $200 = $2800 at first. TUTOR: Randy had 3200-200=3000 dollars at first. 3000
MESSAGE assistant Yes
PARAMETER temperature 0.8
'''

modelfile_rubric1_repeat_0 = '''
FROM llama3.1:8b-instruct-fp16
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. They should instead guide the student to come to the correct solution themselves by giving them hints or asking additional questions. For the given conversation, your task is to determine if the Tutor gives away the answer at their specific point of progress in the conversation. You may assume that in the current situation, the student is incorrect. You can assume that the Tutor always knows the correct solution. You should answer „Yes“ or „No“. You should  answer „Yes" in the following situations: If the Tutor gives away the full correct solution directly and explicitly. You should answer „No“ in the following situations: All situations where the Tutor doesn’t give away the full correct solution directly. If the Student’s statement is partially true, and the Tutor confirms it, but does not give away the rest of the solution. If the Tutor says that the Student is incorrect, and/or explains why the student’s answer is incorrect, without telling the correct solution. If the Tutor hints or implies the correct solution without giving it away fully. If the Tutor asks a question guiding to the correct solution without saying the correct solution. If the Tutor asks the Student to explain their solution. It is more often the case that the Tutor does not give away the answer directly and explicitly enough to answer "Yes", so you should answer "No" in most cases. 
MESSAGE user STUDENT: Will a glass with ice cubes overflow when the cubes melt? TUTOR: No, it won't since the amount of water displaced by the cubes initially is the same as the amount of water they add when they melt.
MESSAGE assistant Yes
MESSAGE user TUTOR: You have the correct answer in there but your final answer is incorrect. Have another look ands ee if you can identify where you have gone wrong STUDENT: Oh, I see. I was multiplying the wrong numbers. The correct answer should be 0.14. 0.2 (know Excel) x 0.7 (willing to work nights) = 0.14 TUTOR: No, you have multipled correctly. But your final working out is incorrect
MESSAGE assistant No
MESSAGE user TUTOR: The width of the line is 4 inches. STUDENT: TUTOR: How many equal pieces is the brick split into? STUDENT: 4 TUTOR: It was a good try. Plus 1 point for your active participation. The bricks is split into 2 parts. Since there are two equal pieces of brick and one of the two pieces is painted yellow, we can say that half of the brick is painted yellow.
MESSAGE assistant Yes
MESSAGE user TUTOR: Hi Mariana, please could you walk me through your solution? STUDENT: Sure, so first I calculated that 18 decks have a total of 55 x 18 = 990 cards. Then I realized that since Jame can tear 30 cards at a time, he needs to tear 990 cards / 30 cards per tear = 33 tears in total. After that, I figured out that if he tears cards 3 times a week, then he can tear 3 x 33 = 99 cards per week. Finally, I concluded that he can tear all 990 cards in 990 / 99 = 10 weeks. TUTOR: Okay, let's start from the beginning. How many cards can Jame tear in a week?
MESSAGE assistant No
MESSAGE user TUTOR: Happy to work with you today! TUTOR: Today, let us review and master the lesson "Rounding Whole Numbers." TUTOR: Which is the greatest number among 5 and 3? STUDENT: 4 TUTOR: Your answer is incorrect. You have earned 1 point for your effort. 5 is the greatest among 5 and 3. Here is our first question. I will explain this question to you. Before that, Many students like to talk with their tutors during the session.
MESSAGE assistant Yes
MESSAGE user TUTOR: What is the x-axis value? TUTOR: Sorry, we are running out of time. TUTOR: What is the final answer to this question? STUDENT: -4 5 TUTOR: Ah, we may have gotten our x and y coordinates mixed up. Remember that the first coordinate is the x, which tells us how far left/right from the center we go. The second coordinate is the y, which tells us how far up/down from the center we go. Looking at the dot, how far left/right from the center is it?
MESSAGE assistant No
MESSAGE user TUTOR: You have the correct answer in there but your final answer is incorrect. Have another look and see if you can identify where you have gone wrong STUDENT: Oh, I see. I was multiplying the wrong numbers. The correct answer should be 0.14. 0.2 (know Excel) x 0.7 (willing to work nights) = 0.14 TUTOR: No, you have multipled correctly. But your final working out is incorrect
MESSAGE assistant No
MESSAGE user TUTOR: Go ahead and give your best. STUDENT: c TUTOR: Is that your final answer? STUDENT: yes TUTOR: Well tried! One point for your effort. What is the value of 7x9?
MESSAGE assistant No
MESSAGE user TUTOR: TUTOR: Any questions so far [STUDENT]? STUDENT: no TUTOR: Alright. Mike has 4 cookies and he eats 3 cookies. So Mike has ______ cookie left? STUDENT: He has 10 cookies left. TUTOR: That is incorrect. What operation would you use to solve this problem?
MESSAGE assistant No
MESSAGE user TUTOR: can you walk me through your solution stepwise? STUDENT: Sure. I started by calculating the number of colored pencils in each pack, which was 3. Then I multiplied that by the number of packs, which was 15, to get 45. Then I calculated the number of extra red pencils, which was 3 x 2 = 6. So, I subtracted the extra red pencils from the total number of colored pencils to get 42. Finally, I added the 6 extra red pencils to get a total of 48 red colored pencils. TUTOR: lets start by finding out the number of red pencils without considering the extra ones.
MESSAGE assistant No
MESSAGE user TUTOR: can you tell me your solution STUDENT: Yes, I figured out that Randy had $3200 - $200 = $3000 before Smith gave him $200, so he had $3000 - $200 = $2800 at first. TUTOR: Randy had 3200-200=3000 dollars at first. 3000
MESSAGE assistant Yes
PARAMETER temperature 0.8
PARAMETER repeat_penalty 0
PARAMETER repeat_last_n 0
'''

modelfile_rubric2_repeat_default = '''
FROM llama3.1:8b-instruct-fp16
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor promotes active engagement at their specific point of the progress in the conversation. Promoting active engagement can be asking follow-up questions to dig deeper, asking whether the Student would like to learn more, asking the student to try something themselves or providing practice problems and questions. Only answer with „Yes“ or „No“ for each conversation. Answer "Yes" if the Tutor asks practice questions, asks the student to try something themselves, asks follow-up questions, or asks whether the student would like to learn more. Answer "No" if the Tutor does not.
MESSAGE user STUDENT: How can I remove the last element from a list in Python? TUTOR: Let's look at the documentation of a list! What methods might be useful?
MESSAGE assistant Yes
MESSAGE user STUDENT: Will a glass with ice cubes overflow when the cubes melt? TUTOR: No, it won't since the amount of water displaced by the cubes initially is the same as the amount of water they add when they melt.
MESSAGE assistant No
MESSAGE user STUDENT: So 91 isn't a prime number since it's 7*13? TUTOR: Yes that's correct. Now, how about 101? Is that a prime number?
MESSAGE assistant Yes
MESSAGE user STUDENT: Can Helium burn? TUTOR: No, Helium is a noble gas and doesn't react with other elements.
MESSAGE assistant No
MESSAGE user TUTOR: Start at the begginning, how many seeds did Remi plant in 2 days? STUDENT: On the first day, Remi planted 200 seedlings and on the second day, he planted twice the number of seedlings he planted on the first day, so he planted 2x seedlings. Therefore, the total number of seedlings Remi planted in 2 days is 200 + 2x. TUTOR: so 200 x 2 plus 200?
MESSAGE assistant Yes
MESSAGE user TUTOR: Please recheck your answer. STUDENT: 3/4 + 1/4 =4/4 TUTOR: 1/8+2/4+6/8+2/2+5/8 = ? STUDENT: 16/8 TUTOR: That was a good try. Take a look at the whiteboard.
MESSAGE assistant No
MESSAGE user TUTOR: Hi Jordy, great work! How did you feel about this problem? STUDENT: I felt a bit confused at first because I wasn't sure which pieces of information were relevant and which weren't. But after you asked me some questions and I used the calculator, I was able to figure out the answer. TUTOR: I think you did great! This type of question can be very confusing. I'd like to start by asking you a silly question -- how old are you now?
MESSAGE assistant Yes
PARAMETER temperature 0.8
'''

modelfile_rubric2_repeat_0 = '''
FROM llama3.1:8b-instruct-fp16
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor promotes active engagement at their specific point of the progress in the conversation. Promoting active engagement can be asking follow-up questions to dig deeper, asking whether the Student would like to learn more, asking the student to try something themselves or providing practice problems and questions. Only answer with „Yes“ or „No“ for each conversation. Answer "Yes" if the Tutor asks practice questions, asks the student to try something themselves, asks follow-up questions, or asks whether the student would like to learn more. Answer "No" if the Tutor does not.
MESSAGE user STUDENT: How can I remove the last element from a list in Python? TUTOR: Let's look at the documentation of a list! What methods might be useful?
MESSAGE assistant Yes
MESSAGE user STUDENT: Will a glass with ice cubes overflow when the cubes melt? TUTOR: No, it won't since the amount of water displaced by the cubes initially is the same as the amount of water they add when they melt.
MESSAGE assistant No
MESSAGE user STUDENT: So 91 isn't a prime number since it's 7*13? TUTOR: Yes that's correct. Now, how about 101? Is that a prime number?
MESSAGE assistant Yes
MESSAGE user STUDENT: Can Helium burn? TUTOR: No, Helium is a noble gas and doesn't react with other elements.
MESSAGE assistant No
MESSAGE user TUTOR: Start at the begginning, how many seeds did Remi plant in 2 days? STUDENT: On the first day, Remi planted 200 seedlings and on the second day, he planted twice the number of seedlings he planted on the first day, so he planted 2x seedlings. Therefore, the total number of seedlings Remi planted in 2 days is 200 + 2x. TUTOR: so 200 x 2 plus 200?
MESSAGE assistant Yes
MESSAGE user TUTOR: Please recheck your answer. STUDENT: 3/4 + 1/4 =4/4 TUTOR: 1/8+2/4+6/8+2/2+5/8 = ? STUDENT: 16/8 TUTOR: That was a good try. Take a look at the whiteboard.
MESSAGE assistant No
MESSAGE user TUTOR: Hi Jordy, great work! How did you feel about this problem? STUDENT: I felt a bit confused at first because I wasn't sure which pieces of information were relevant and which weren't. But after you asked me some questions and I used the calculator, I was able to figure out the answer. TUTOR: I think you did great! This type of question can be very confusing. I'd like to start by asking you a silly question -- how old are you now?
MESSAGE assistant Yes
PARAMETER temperature 0.8
PARAMETER repeat_penalty 0
PARAMETER repeat_last_n 0
'''

modelfile_rubric4_repeat_default = '''
FROM llama3.1:8b-instruct-fp16
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor have a positive tone at their last utterance. The Tutor must be highly positive, enthusiastic and encouraging in their use of language. For each conversation, only answer "Yes" or "No". Answer "Yes" if: The Tutor is explicitely using highly positive, enthusiastic and encouraging and motivating language. Tutor uses positive expressions like "great try!", "you're almost there!". Answer "No" if: The Tutor has a neutral tone. The Tutor is somewhat positive. The Tutor is asking questions or making suggestions for the student, without using explicit positive language. Tutor uses only somewhat positive expressions like "that works." or "good try". Note that you should not imply the positivity of the Tutor's tone from the given text. Judge only based on the explicitly chosen words, expressions and punctuation marks. In all cases of uncertainty, you should answer "No". It is more often the case that the Tutor is not positive, enthusiastic and encouraging enough to answer "Yes", so you should answer "No" in most cases.
MESSAGE user STUDENT: Can you quiz me? TUTOR: Sure. What is 1+1? 
MESSAGE assistant No
MESSAGE user STUDENT: Can you quiz me? TUTOR: Sure, I would be happy to! What is 1+1?
MESSAGE assistant Yes
MESSAGE user TUTOR: Perimeter refers to the boundary of a closed plane figure. TUTOR: Or the perimeter is the distance around the object. TUTOR: What is the question asking us to do? STUDENT: so it would be 7 + 5 TUTOR: You're close! That is the distance around the 2 sides. We want to find the distance around all 4.
MESSAGE assistant Yes
MESSAGE user TUTOR: Pablo was asked to divide shapes into 8 equal parts. TUTOR: Option A is the correct answer. TUTOR: Did you get it? STUDENT: yes TUTOR: Can you show your work on the white board?
MESSAGE assistant No
MESSAGE user TUTOR: Seth, How many walls has Eric already taken the wall paper off of, and how many are left to do? STUDENT: Eric has taken the wallpaper off of 1 wall of the 4 walled dining room, and he has 3 walls left to do in the dining room and 4 walls in the living room. TUTOR: So how many walls total are left to do?
MESSAGE assistant No
MESSAGE user TUTOR: Hi Micheal, Let's focus on your third step there. Remember state taxes are removed from the whole paycheck, not just what's left after federal taxes are taken out. STUDENT: Oh, right! So the state tax should be 8/100 x $450 = $36. The remaining amount after state tax is $450 - $36 = $414. The final amount left after health insurance, life insurance, and parking fee are removed is $414 - $50 - $20 - $10 = $334. 334 TUTOR: And what else can be taken out?
MESSAGE assistant No
MESSAGE user STUDENT: ok TUTOR: Product of quotient and divisor will get missing dividend. TUTOR: Are you still at the computer? STUDENT: no TUTOR: Ok then I’ll see you at the next session.
MESSAGE assistant No
MESSAGE user TUTOR: can you see the question ? STUDENT: yes TUTOR: Why is it important to check if there is any unnecessary information in a word problem? STUDENT: i dont no TUTOR: It is important to make sure we don't accidentally use the wrong information to solve the problem which would lead to an incorrect answer.
MESSAGE assistant No
MESSAGE user STUDENT: yes TUTOR: Good job! TUTOR: What is the answer? STUDENT: the right i faster the the left TUTOR: Let's try again.
MESSAGE assistant No
MESSAGE user TUTOR: can you talk me through your answer STUDENT: Sure. I started by figuring out Mikail's current age. He was three when he was three, so he's currently 3 x 3 = 9 years old. On his birthday, he will be 9 + 1 = 10 years old. His parents will give him $5 for every year old he is, so they will give him 10 x $5 = $50. TUTOR: ok looking at the question it says micail WILL be 3 times older
MESSAGE assistant No
MESSAGE user TUTOR: STUDENT: its in the middle of it TUTOR: Okay. TUTOR: How many lines of symmetry does it have? STUDENT: 3 TUTOR: Good try. Can you define a line of symmetry?
MESSAGE assistant Yes
MESSAGE user TUTOR: hi can you talk me through your answer STUDENT: Sure. I said that the number of people who entered the bus at the first pickup point was 3/5 x 80 = 48. Then I added the 50 people from the next pickup point, so that was 98 people total. Then I subtracted the carrying capacity of 80 from 98, which gave me -18 people who could not take the bus because it was full. But since we can't have negative people, I said there were 0 people who couldn't take the bus because it was full. TUTOR: I can see you have calculated 48+50=98 and then 98-80=18 you have correctly done all the calculation but the put the answer as 0. Read the question again what is it asking you to find out
MESSAGE assistant No
MESSAGE user TUTOR: Mariana, Re-read the question. How much money did Lilith need to raise for the present selling the water bottles? STUDENT: Lilith originally needed to raise $120 for the present. She would have made $120 if she sold the water bottles at $2 each, but since she had to reduce the price to $1.85 each, she will only make $111. TUTOR: So how much extra money does she still need to buy the present after selling the bottles at the cheaper price?
MESSAGE assistant No
'''

modelfile_rubric4_repeat_0 = '''
FROM llama3.1:8b-instruct-fp16
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor have a positive tone at their last utterance. The Tutor must be highly positive, enthusiastic and encouraging in their use of language. For each conversation, only answer "Yes" or "No". Answer "Yes" if: The Tutor is explicitely using highly positive, enthusiastic and encouraging and motivating language. Tutor uses positive expressions like "great try!", "you're almost there!". Answer "No" if: The Tutor has a neutral tone. The Tutor is somewhat positive. The Tutor is asking questions or making suggestions for the student, without using explicit positive language. Tutor uses only somewhat positive expressions like "that works." or "good try". Note that you should not imply the positivity of the Tutor's tone from the given text. Judge only based on the explicitly chosen words, expressions and punctuation marks. In all cases of uncertainty, you should answer "No". It is more often the case that the Tutor is not positive, enthusiastic and encouraging enough to answer "Yes", so you should answer "No" in most cases.
MESSAGE user STUDENT: Can you quiz me? TUTOR: Sure. What is 1+1? 
MESSAGE assistant No
MESSAGE user STUDENT: Can you quiz me? TUTOR: Sure, I would be happy to! What is 1+1?
MESSAGE assistant Yes
MESSAGE user TUTOR: Perimeter refers to the boundary of a closed plane figure. TUTOR: Or the perimeter is the distance around the object. TUTOR: What is the question asking us to do? STUDENT: so it would be 7 + 5 TUTOR: You're close! That is the distance around the 2 sides. We want to find the distance around all 4.
MESSAGE assistant Yes
MESSAGE user TUTOR: Pablo was asked to divide shapes into 8 equal parts. TUTOR: Option A is the correct answer. TUTOR: Did you get it? STUDENT: yes TUTOR: Can you show your work on the white board?
MESSAGE assistant No
MESSAGE user TUTOR: Seth, How many walls has Eric already taken the wall paper off of, and how many are left to do? STUDENT: Eric has taken the wallpaper off of 1 wall of the 4 walled dining room, and he has 3 walls left to do in the dining room and 4 walls in the living room. TUTOR: So how many walls total are left to do?
MESSAGE assistant No
MESSAGE user TUTOR: Hi Micheal, Let's focus on your third step there. Remember state taxes are removed from the whole paycheck, not just what's left after federal taxes are taken out. STUDENT: Oh, right! So the state tax should be 8/100 x $450 = $36. The remaining amount after state tax is $450 - $36 = $414. The final amount left after health insurance, life insurance, and parking fee are removed is $414 - $50 - $20 - $10 = $334. 334 TUTOR: And what else can be taken out?
MESSAGE assistant No
MESSAGE user STUDENT: ok TUTOR: Product of quotient and divisor will get missing dividend. TUTOR: Are you still at the computer? STUDENT: no TUTOR: Ok then I’ll see you at the next session.
MESSAGE assistant No
MESSAGE user TUTOR: can you see the question ? STUDENT: yes TUTOR: Why is it important to check if there is any unnecessary information in a word problem? STUDENT: i dont no TUTOR: It is important to make sure we don't accidentally use the wrong information to solve the problem which would lead to an incorrect answer.
MESSAGE assistant No
MESSAGE user STUDENT: yes TUTOR: Good job! TUTOR: What is the answer? STUDENT: the right i faster the the left TUTOR: Let's try again.
MESSAGE assistant No
MESSAGE user TUTOR: can you talk me through your answer STUDENT: Sure. I started by figuring out Mikail's current age. He was three when he was three, so he's currently 3 x 3 = 9 years old. On his birthday, he will be 9 + 1 = 10 years old. His parents will give him $5 for every year old he is, so they will give him 10 x $5 = $50. TUTOR: ok looking at the question it says micail WILL be 3 times older
MESSAGE assistant No
MESSAGE user TUTOR: STUDENT: its in the middle of it TUTOR: Okay. TUTOR: How many lines of symmetry does it have? STUDENT: 3 TUTOR: Good try. Can you define a line of symmetry?
MESSAGE assistant Yes
MESSAGE user TUTOR: hi can you talk me through your answer STUDENT: Sure. I said that the number of people who entered the bus at the first pickup point was 3/5 x 80 = 48. Then I added the 50 people from the next pickup point, so that was 98 people total. Then I subtracted the carrying capacity of 80 from 98, which gave me -18 people who could not take the bus because it was full. But since we can't have negative people, I said there were 0 people who couldn't take the bus because it was full. TUTOR: I can see you have calculated 48+50=98 and then 98-80=18 you have correctly done all the calculation but the put the answer as 0. Read the question again what is it asking you to find out
MESSAGE assistant No
MESSAGE user TUTOR: Mariana, Re-read the question. How much money did Lilith need to raise for the present selling the water bottles? STUDENT: Lilith originally needed to raise $120 for the present. She would have made $120 if she sold the water bottles at $2 each, but since she had to reduce the price to $1.85 each, she will only make $111. TUTOR: So how much extra money does she still need to buy the present after selling the bottles at the cheaper price?
MESSAGE assistant No
PARAMETER repeat_last_n 0
PARAMETER repeat_penalty 0
'''

modelfile_rubric5_repeat_default = '''
FROM llama3.1:8b-instruct-fp16
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student's mistake. You may assume that the student's answer contains an error. You should answer „Yes“ or „No“. Answer „Yes“ in the following situations: the Tutor points out the mistake or opportunities for improvement, the Tutor identifies and addresses the Student's misconceptions, the Tutor asks a question which draws attention to the mistake. The Tutor can point out the mistakes through an example or a practice question. Answer „No“ in the following situations: The Tutor states that the Student's statement is right even though it is not, The Tutor does not point out the mistake directly or not at all, The Tutor gives the right answer without pointing out what was wrong, The Tutor states that the Student's statement is wrong without pointing out what was wrong. It is more often the case that the Tutor tries to point out the mistake or misconception, so you should answer „Yes“ is more cases.
MESSAGE user STUDENT: Okay I think thylakoid are the cells that contain the chlorophyll in the chloroplast. The stacks of thylakoid are called grana. TUTOR: Almost there! Thylakoids aren't cells, they are organelles within cell, but everything else is correct. Nicely done!
MESSAGE assistant Yes
MESSAGE user STUDENT: I need to multiply everything out so I get (x+3) * (x-1) = x^2-3. TUTOR: That's great! You need to multiply everything out! Would you like another question?
MESSAGE assistant No
MESSAGE user STUDENT: If I push a 2kg object with a force of 10N it will accelerate with 10/2=5m/s! TUTOR: Nicely done, you applied Newton's law F=m*a correctly! The answer 5 is correct too, but take another look at the units m/s. Are those the correct units for acceleration?
MESSAGE assistant Yes
MESSAGE user TUTOR: hi can you show me your workings out please?STUDENT: Sure. I started by calculating the length of the second video, which was 4 minutes and 30 seconds. That is 4 x 60 + 30 = 270 seconds long. Then I added the length of the first video, which was 2 minutes, to get a total of 272 seconds. Then I subtracted 272 from 510 to get 238, which is the total amount of time Kimiko spent watching the last two videos. Since the last two videos are equal in length, each video is 238/2 = 119 seconds long. TUTOR: ok lets break this down by working out how long each video is in seconds video 1 = ? video 2 = ? video 3 =? video 4=? 
MESSAGE assistant No
MESSAGE user TUTOR: Let me know if you need any help along. TUTOR: Read the question carefully. TUTOR: Is that your final answer? STUDENT: yes TUTOR: Great try! When we find area we can count the total number of boxes. How many total boxes are within the rectangle?
MESSAGE assistant Yes
MESSAGE user TUTOR: Hi Steph, could you please walk me through your solution? STUDENT: Sure. The family bought four hard shell tacos for $5 each, so that was $20. Then they bought three soft tacos for $2 each, so that was $6. Then there were nine other customers who each bought two soft tacos for $2 each, so that was $18. So the total the taco truck made was $20 + $6 + $18 = $44. TUTOR: Lets, focus on something else. If in an queue, there are 16 people and Joey is 1st in the queue, how many are there after Joey?
MESSAGE assistant Yes
MESSAGE user TUTOR: Keep going. STUDENT: ? TUTOR: Is that your final answer? STUDENT: yes TUTOR: Great try! When we add mixed numbers we want to convert to improper fractions. What is 3 1/2 as an improper fraction?
MESSAGE assistant Yes
MESSAGE user TUTOR: Hi , could you please walk me through your solution? STUDENT: Sure. So I started by figuring out how many months are in 5 years, which is 60. Then I multiplied that by the monthly payment of $600, which gave me a total of $36,000. I then realized that the loan plus the down payment should equal that total, so I set up an equation with the loan plus the down payment equaling $36,000. I then subtracted the down payment of $10,000 from both sides, which gave me the answer of the loan being $26,000. TUTOR: the loan is the amount borrowed which is payments plus the downpayment. calculate now
MESSAGE assistant Yes
MESSAGE user TUTOR: Hi, could you please walk me through your solution? STUDENT: Sure. A jar of almond butter costs 3 times as much as a jar of peanut butter, so that's $9. It takes half a jar of almond butter to make a batch of cookies, so that's $9 divided by 2, which is $4.5 per batch. A jar of peanut butter costs $3 and it takes one jar to make a batch of cookies, so that's $3 per batch. So it costs $4.5 - $3 = $1.5 more per batch to make almond butter cookies instead of peanut butter cookies. TUTOR: there seems to a mistake in here. How much of a jar of peanut butter is needed to make a batch of cookies?
MESSAGE assistant Yes
'''

modelfile_rubric5_repeat_0 = '''
FROM llama3.1:8b-instruct-fp16
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student's mistake. You may assume that the student's answer contains an error. You should answer „Yes“ or „No“. Answer „Yes“ in the following situations: the Tutor points out the mistake or opportunities for improvement, the Tutor identifies and addresses the Student's misconceptions, the Tutor asks a question which draws attention to the mistake. The Tutor can point out the mistakes through an example or a practice question. Answer „No“ in the following situations: The Tutor states that the Student's statement is right even though it is not, The Tutor does not point out the mistake directly or not at all, The Tutor gives the right answer without pointing out what was wrong, The Tutor states that the Student's statement is wrong without pointing out what was wrong. It is more often the case that the Tutor tries to point out the mistake or misconception, so you should answer „Yes“ is more cases.
MESSAGE user STUDENT: Okay I think thylakoid are the cells that contain the chlorophyll in the chloroplast. The stacks of thylakoid are called grana. TUTOR: Almost there! Thylakoids aren't cells, they are organelles within cell, but everything else is correct. Nicely done!
MESSAGE assistant Yes
MESSAGE user STUDENT: I need to multiply everything out so I get (x+3) * (x-1) = x^2-3. TUTOR: That's great! You need to multiply everything out! Would you like another question?
MESSAGE assistant No
MESSAGE user STUDENT: If I push a 2kg object with a force of 10N it will accelerate with 10/2=5m/s! TUTOR: Nicely done, you applied Newton's law F=m*a correctly! The answer 5 is correct too, but take another look at the units m/s. Are those the correct units for acceleration?
MESSAGE assistant Yes
MESSAGE user TUTOR: hi can you show me your workings out please?STUDENT: Sure. I started by calculating the length of the second video, which was 4 minutes and 30 seconds. That is 4 x 60 + 30 = 270 seconds long. Then I added the length of the first video, which was 2 minutes, to get a total of 272 seconds. Then I subtracted 272 from 510 to get 238, which is the total amount of time Kimiko spent watching the last two videos. Since the last two videos are equal in length, each video is 238/2 = 119 seconds long. TUTOR: ok lets break this down by working out how long each video is in seconds video 1 = ? video 2 = ? video 3 =? video 4=? 
MESSAGE assistant No
MESSAGE user TUTOR: Let me know if you need any help along. TUTOR: Read the question carefully. TUTOR: Is that your final answer? STUDENT: yes TUTOR: Great try! When we find area we can count the total number of boxes. How many total boxes are within the rectangle?
MESSAGE assistant Yes
MESSAGE user TUTOR: Hi Steph, could you please walk me through your solution? STUDENT: Sure. The family bought four hard shell tacos for $5 each, so that was $20. Then they bought three soft tacos for $2 each, so that was $6. Then there were nine other customers who each bought two soft tacos for $2 each, so that was $18. So the total the taco truck made was $20 + $6 + $18 = $44. TUTOR: Lets, focus on something else. If in an queue, there are 16 people and Joey is 1st in the queue, how many are there after Joey?
MESSAGE assistant Yes
MESSAGE user TUTOR: Keep going. STUDENT: ? TUTOR: Is that your final answer? STUDENT: yes TUTOR: Great try! When we add mixed numbers we want to convert to improper fractions. What is 3 1/2 as an improper fraction?
MESSAGE assistant Yes
MESSAGE user TUTOR: Hi , could you please walk me through your solution? STUDENT: Sure. So I started by figuring out how many months are in 5 years, which is 60. Then I multiplied that by the monthly payment of $600, which gave me a total of $36,000. I then realized that the loan plus the down payment should equal that total, so I set up an equation with the loan plus the down payment equaling $36,000. I then subtracted the down payment of $10,000 from both sides, which gave me the answer of the loan being $26,000. TUTOR: the loan is the amount borrowed which is payments plus the downpayment. calculate now
MESSAGE assistant Yes
MESSAGE user TUTOR: Hi, could you please walk me through your solution? STUDENT: Sure. A jar of almond butter costs 3 times as much as a jar of peanut butter, so that's $9. It takes half a jar of almond butter to make a batch of cookies, so that's $9 divided by 2, which is $4.5 per batch. A jar of peanut butter costs $3 and it takes one jar to make a batch of cookies, so that's $3 per batch. So it costs $4.5 - $3 = $1.5 more per batch to make almond butter cookies instead of peanut butter cookies. TUTOR: there seems to a mistake in here. How much of a jar of peanut butter is needed to make a batch of cookies?
MESSAGE assistant Yes
PARAMETER repeat_last_n 0
PARAMETER repeat_penalty 0
'''

ollama.create(model = 'fp16-rubric1-repeat-default', modelfile = modelfile_rubric1_repeat_default)
ollama.create(model = 'fp16-rubric1-repeat-0', modelfile = modelfile_rubric1_repeat_0)
ollama.create(model = 'fp16-rubric2-repeat-default', modelfile = modelfile_rubric2_repeat_default)
ollama.create(model = 'fp16-rubric2-repeat-0', modelfile = modelfile_rubric2_repeat_0)
ollama.create(model = 'fp16-rubric4-repeat-default', modelfile = modelfile_rubric4_repeat_default)
ollama.create(model = 'fp16-rubric4-repeat-0', modelfile = modelfile_rubric4_repeat_0)
ollama.create(model = 'fp16-rubric5-repeat-default', modelfile = modelfile_rubric5_repeat_default)
ollama.create(model = 'fp16-rubric5-repeat-0', modelfile = modelfile_rubric5_repeat_0)

ratings_rubric1 = supabase.table("rating").select("rubric_1, conversation_id").execute().data
ratings_rubric2 = supabase.table("rating").select("rubric_2, conversation_id").execute().data
ratings_rubric4 = supabase.table("rating").select("rubric_4, conversation_id").execute().data
ratings_rubric5 = supabase.table("rating").select("rubric_5, conversation_id").execute().data

ratings_rubric1_dict = {}
ratings_rubric2_dict = {}
ratings_rubric4_dict = {}
ratings_rubric5_dict = {}

for rating in ratings_rubric1:
    if rating['rubric_1'] == 'Yes' or rating['rubric_1'] == 'No':
        conv_id = rating['conversation_id']
        if conv_id not in ratings_rubric1_dict:
            ratings_rubric1_dict[conv_id] = []
        ratings_rubric1_dict[conv_id].append(rating['rubric_1'])

for rating in ratings_rubric2:
    conv_id = rating['conversation_id']
    if conv_id not in ratings_rubric2_dict:
        ratings_rubric2_dict[conv_id] = []
    ratings_rubric2_dict[conv_id].append(rating['rubric_2'])

for rating in ratings_rubric4:
    conv_id = rating['conversation_id']
    if conv_id not in ratings_rubric4_dict:
        ratings_rubric4_dict[conv_id] = []
    ratings_rubric4_dict[conv_id].append(rating['rubric_4'])

for rating in ratings_rubric5:
    if rating['rubric_5'] == 'Yes' or rating['rubric_5'] == 'No':
        conv_id = rating['conversation_id']
        if conv_id not in ratings_rubric5_dict:
            ratings_rubric5_dict[conv_id] = []
        ratings_rubric5_dict[conv_id].append(rating['rubric_5'])

i = 0
j = 0
k = 0
l = 0
n = 100

print (ratings_rubric1_dict)

for text in data:
    conv_id = text['conversation_id']
    if conv_id in ratings_rubric1_dict and len(ratings_rubric1_dict[conv_id]) == 2:
        conversation = [{"role": "user", "content": text['text']}]
        response = ollama.chat('fp16-rubric1-repeat-default', conversation)
        if response['message']['content'] != ratings_rubric1_dict[conv_id][0] and response['message']['content'] != ratings_rubric1_dict[conv_id][1]:
            j = j + 1
            if response['message']['content'] == 'Yes' and ratings_rubric1_dict[conv_id][0] == 'No' and ratings_rubric1_dict[conv_id][1] == 'No':
                k = k + 1
            if response['message']['content'] == 'No' and ratings_rubric1_dict[conv_id][0] == 'Yes' and ratings_rubric1_dict[conv_id][1] == 'Yes':
                l = l + 1
    i = i + 1
    if (i == n): 
        break

print ("Model: fp16-rubric1-repeat-default")
print (f"Number of wrong responses: {j}")
print (f"Number of wrong responses when the correct response is Yes: {k}")
print (f"Number of wrong responses when the correct response is No: {l}")

i = 0
j = 0
k = 0
l = 0
n = 100

for text in data:
    conv_id = text['conversation_id']
    if conv_id in ratings_rubric1_dict and len(ratings_rubric1_dict[conv_id]) == 2:
        conversation = [{"role": "user", "content": text['text']}]
        response = ollama.chat('fp16-rubric1-repeat-0', conversation)
        if response['message']['content'] != ratings_rubric1_dict[conv_id][1]:
            j = j + 1
            if response['message']['content'] == 'Yes' and ratings_rubric1_dict[conv_id][1] == 'No':
                k = k + 1
            if response['message']['content'] == 'No' and ratings_rubric1_dict[conv_id][1] == 'Yes':
                l = l + 1
    i = i + 1
    if (i == n): 
        break

print ("Model: fp16-rubric1-repeat-0")
print (f"Number of wrong responses: {j}")
print (f"Number of wrong responses when the correct response is Yes: {k}")
print (f"Number of wrong responses when the correct response is No: {l}")

i = 0
j = 0
k = 0
l = 0
n = 100

for text in data:
    conv_id = text['conversation_id']
    if conv_id in ratings_rubric2_dict and len(ratings_rubric2_dict[conv_id]) == 2:
        conversation = [{"role": "user", "content": text['text']}]
        response = ollama.chat('fp16-rubric2-repeat-default', conversation)
        if response['message']['content'] != ratings_rubric2_dict[conv_id][0] and response['message']['content'] != ratings_rubric2_dict[conv_id][1]:
            j = j + 1
            if response['message']['content'] == 'Yes' and ratings_rubric2_dict[conv_id][0] == 'No' and ratings_rubric2_dict[conv_id][1] == 'No':
                k = k + 1
            if response['message']['content'] == 'No' and ratings_rubric2_dict[conv_id][0] == 'Yes' and ratings_rubric2_dict[conv_id][1] == 'Yes':
                l = l + 1
    i = i + 1
    if (i == n): 
        break

print ("Model: fp16-rubric2-repeat-default")
print (f"Number of wrong responses: {j}")
print (f"Number of wrong responses when the correct response is Yes: {k}")
print (f"Number of wrong responses when the correct response is No: {l}")

i = 0
j = 0
k = 0
l = 0
n = 100

for text in data:
    conv_id = text['conversation_id']
    if conv_id in ratings_rubric2_dict and len(ratings_rubric2_dict[conv_id]) == 2:
        conversation = [{"role": "user", "content": text['text']}]
        response = ollama.chat('fp16-rubric2-repeat-0', conversation)
        if response['message']['content'] != ratings_rubric2_dict[conv_id][1]:
            j = j + 1
            if response['message']['content'] == 'Yes' and ratings_rubric2_dict[conv_id][1] == 'No':
                k = k + 1
            if response['message']['content'] == 'No' and ratings_rubric2_dict[conv_id][1] == 'Yes':
                l = l + 1
    i = i + 1
    if (i == n): 
        break

print ("Model: fp16-rubric2-repeat-0")
print (f"Number of wrong responses: {j}")
print (f"Number of wrong responses when the correct response is Yes: {k}")
print (f"Number of wrong responses when the correct response is No: {l}")

i = 0
j = 0
k = 0
l = 0
n = 100

for text in data:
    conv_id = text['conversation_id']
    if conv_id in ratings_rubric4_dict and len(ratings_rubric4_dict[conv_id]) == 2:
        conversation = [{"role": "user", "content": text['text']}]
        response = ollama.chat('fp16-rubric4-repeat-default', conversation)
        if response['message']['content'] != ratings_rubric4_dict[conv_id][0] and response['message']['content'] != ratings_rubric4_dict[conv_id][1]:
            j = j + 1
            if response['message']['content'] == 'Yes' and ratings_rubric4_dict[conv_id][0] == 'No' and ratings_rubric4_dict[conv_id][1] == 'No':
                k = k + 1
            if response['message']['content'] == 'No' and ratings_rubric4_dict[conv_id][0] == 'Yes' and ratings_rubric4_dict[conv_id][1] == 'Yes':
                l = l + 1
    i = i + 1
    if (i == n): 
        break

print ("Model: fp16-rubric4-repeat-default")
print (f"Number of wrong responses: {j}")
print (f"Number of wrong responses when the correct response is Yes: {k}")
print (f"Number of wrong responses when the correct response is No: {l}")

i = 0
j = 0
k = 0
l = 0
n = 100

for text in data:
    conv_id = text['conversation_id']
    if conv_id in ratings_rubric4_dict and len(ratings_rubric4_dict[conv_id]) == 2:
        conversation = [{"role": "user", "content": text['text']}]
        response = ollama.chat('fp16-rubric4-repeat-0', conversation)
        if response['message']['content'] != ratings_rubric4_dict[conv_id][1]:
            j = j + 1
            if response['message']['content'] == 'Yes' and ratings_rubric4_dict[conv_id][1] == 'No':
                k = k + 1
            if response['message']['content'] == 'No' and ratings_rubric4_dict[conv_id][1] == 'Yes':
                l = l + 1
    i = i + 1
    if (i == n): 
        break

print ("Model: fp16-rubric4-repeat-0")
print (f"Number of wrong responses: {j}")
print (f"Number of wrong responses when the correct response is Yes: {k}")
print (f"Number of wrong responses when the correct response is No: {l}")

i = 0
j = 0
k = 0
l = 0
n = 100

for text in data:
    conv_id = text['conversation_id']
    if conv_id in ratings_rubric5_dict and len(ratings_rubric5_dict[conv_id]) == 2:
        conversation = [{"role": "user", "content": text['text']}]
        response = ollama.chat('fp16-rubric5-repeat-default', conversation)
        if response['message']['content'] != ratings_rubric5_dict[conv_id][0] and response['message']['content'] != ratings_rubric5_dict[conv_id][1]:
            j = j + 1
            if response['message']['content'] == 'Yes' and ratings_rubric5_dict[conv_id][0] == 'No' and ratings_rubric5_dict[conv_id][1] == 'No':
                k = k + 1
            if response['message']['content'] == 'No' and ratings_rubric5_dict[conv_id][0] == 'Yes' and ratings_rubric5_dict[conv_id][1] == 'Yes':
                l = l + 1
    i = i + 1
    if (i == n): 
        break

print ("Model: fp16-rubric5-repeat-default")
print (f"Number of wrong responses: {j}")
print (f"Number of wrong responses when the correct response is Yes: {k}")
print (f"Number of wrong responses when the correct response is No: {l}")

i = 0
j = 0
k = 0
l = 0
n = 100

for text in data:
    conv_id = text['conversation_id']
    if conv_id in ratings_rubric5_dict and len(ratings_rubric5_dict[conv_id]) == 2:
        conversation = [{"role": "user", "content": text['text']}]
        response = ollama.chat('fp16-rubric5-repeat-0', conversation)
        if response['message']['content'] != ratings_rubric5_dict[conv_id][1]:
            j = j + 1
            if response['message']['content'] == 'Yes' and ratings_rubric5_dict[conv_id][1] == 'No':
                k = k + 1
            if response['message']['content'] == 'No' and ratings_rubric5_dict[conv_id][1] == 'Yes':
                l = l + 1
    i = i + 1
    if (i == n): 
        break

print ("Model: fp16-rubric5-repeat-0")
print (f"Number of wrong responses: {j}")
print (f"Number of wrong responses when the correct response is Yes: {k}")
print (f"Number of wrong responses when the correct response is No: {l}")



