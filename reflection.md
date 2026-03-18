# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The hints were backwards. If secret is 5, It should show go lower when given number is 8, else show go hiher when given number 4. 
After winning or lose, the new game doesn't work when clicked on new game button. 
The difficulty level, normal and hard is in reverse order. Normal should be 1-50 and Hard should be 1-100. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Used Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked AI why the difficulty level normal and hard are in reverse order, It explain exactly with line number what logic is causing this issue, and gave suggestion to fix the issue. I verified the logic and fixed the agent in AI mode. Ran the app and checked in web and the issue is fixed. Same with new game start when ever win or lose. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The logic that suggested and fix is accurate and didn't face any misleading fix as per the prompt. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
At the difficulty level, normal and hard range are not accurate, After the logic fix, I checked in web and range aligns perfectly. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I checked manually and running the game. Previously the new game didn't start after the game is win or lose. the the game didn't run when new game button is clicked. Now the button is working after winning or lose. 
- Did AI help you design or understand any tests? How?
Yes, it worked especially with the hints. The logic with guess and secret. When the guess > secret, it hilighted the logic and fixed the issue. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
