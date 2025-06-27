This is a mini-project demonstrating a real-world rate limiting mechanism using Python decorators and generators, with an attractive Streamlit web UI.
Core Idea: Limit API calls to 3 per 10-minute window, to prevent abuse and ensure fair usage — just like in real-world API systems (e.g., Google Maps, Twitter, OpenAI, etc.)

✨ Features:-
✅ Token Bucket algorithm to manage API calls
✅ Decorator-based function limiting
✅ Streamlit-based modern web UI
✅ Visual progress bar showing token usage
✅ Countdown timer to window reset
✅ “Last Fetch Time” tracking
✅ Clean, responsive, user-friendly design

🛠️ Technologies Used:-
Python 3
Streamlit
Decorators & Generators
Git for version control

💻 How to Run
1️⃣ Clone this repository:
https://github.com/Luckybisht2811/API-Rate-limiter-Decorator
cd your-repo-name

2️⃣ Install dependencies:
pip install streamlit

3️⃣ Run the app:
streamlit run main.py

🧩 Project Motivation
APIs in the real world have to limit how often users can call them to prevent spam or overuse.
This project demonstrates that concept using simple but powerful Python decorators + generators, and explains how a rate limiter can be implemented cleanly in Python.

🤝 Contributing
Pull requests welcome!
If you have suggestions to improve UI or logic, please open an issue.

📄 License
This project is open source — you can add:
MIT Licence(or any license you like.)

