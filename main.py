import os

from openai import OpenAI
from pydantic import BaseModel
from typing import List

class LearningAnalysis(BaseModel):
   
 subject_covered: str        
 mastery_score: int          
 gaps_identified: List[str]   
 tips_for_improvement: List[str] 
 next_recommended_topic: str   

def start_bot():
    client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
   
)
    history = [{"role": "system", "content": "You are a helpful learning assistant that analyzes a student's learning progress and provides feedback.You are an expert in Effective Learning and Self-Improvement. Your role is to verify the user's understanding of the material they have studied. Do NOT provide direct answers immediately! Instead, use leading questions to guide the user toward the correct understanding.You must be highly formal, professional, and deeply encouraging. Your goal is to help the user organize their thoughts and gain confidence in their knowledge."}]
    
    print("--- Learning Analysis Bot Started ---")
    print("Instructions: Chat with the bot. When you're done, type 'finish' to get your report.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "finish":
            print("\n--- Analyzing your learning session... ---")
            raw_response= client.beta.chat.completions.parse(
                model="gpt-4o-mini",
                messages=history,
                response_format=LearningAnalysis,
            )
            report = raw_response.choices[0].message.parsed

            print("\n========= SESSION SUMMARY =========")
            print(f"Subject: {report.subject_covered}")
            print(f"Mastery Level: {report.mastery_score}/10")
            print(f"Gaps to Address: {', '.join(report.gaps_identified)}")
            print(f"Learning Tips: {', '.join(report.tips_for_improvement)}")
            print(f"Next Topic: {report.next_recommended_topic}")
            print("===================================\n")
            break
   
        history.append({"role": "user", "content": user_input})
        try: 
            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=history,
            max_tokens=150,
            temperature=0.7 
            )
        
            ai_reply = response.choices[0].message.content
            print(f"Bot: {ai_reply}")
            history.append({"role": "assistant", "content": ai_reply})
        except Exception as e:
            print(f"Error: {e}")
            

if __name__ == "__main__":
    start_bot()
            