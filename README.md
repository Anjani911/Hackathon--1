This project is a lightweight phishing detection tool developed during a 3-hour hackathon.
It analyzes URLs to identify potential phishing threats using keyword matching and trusted domain verification.

🚀 Features
Keyword-Based Detection
Flags URLs containing common phishing terms like login, verify, or free.

Trusted Domain Check
Recognizes and allows links from a fixed list of trusted websites like google.com, facebook.com, instagram.com, etc.

Web Interface
Flask-powered frontend to submit URLs and see phishing status instantly.

🗂️ Project Structure
graphql
Copy
Edit
Hackathon--1/
├── app.py           # Flask app that connects the HTML form to detector logic
├── detector.py      # Core detection logic (updated with domain check)
├── templates/
│   └── index.html   # HTML form for user input and result display
├── presentation/    # Hackathon presentation files
└── __pycache__/     # Python-generated cache files
🛠️ Setup Instructions
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/Anjani911/Hackathon--1.git
cd Hackathon--1
Install Dependencies
Make sure you have Python installed. Then run:

bash
Copy
Edit
pip install flask
Run the App:

bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000/.

📸 Screenshots
(Add screenshots here if you want later.)

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgments
Thanks to the hackathon team and fellow learners.

Built to better understand how phishing detection works at a basic level.

✅ Last updated on: April 17, 2025 (detector.py logic upgraded with trusted domain handling).