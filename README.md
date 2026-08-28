# 🔥 AI Code Roaster

An AI-powered Python application that reviews and roasts your Python code using the Gemini API. 🤖🔥

Paste your code, and the AI will analyze it, point out mistakes in a funny Hinglish style, suggest better code, and give you a skill level and score.

## ✨ Features

- 🤖 AI-powered code review using Google Gemini API
- 🔥 Funny Hinglish code roasting
- 🐛 Identifies genuine mistakes in your Python code
- 💡 Suggests improved code
- 📊 Gives a programming level:
  - Beginner 🐣
  - Intermediate 🚀
  - Advanced 🧠
- ⭐ Gives your code a score out of 10
- 🔁 Option to roast multiple pieces of code

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- python-dotenv

## 📂 Project Structure

```text
AI-Code-Roaster/
│
├── .env                  # API key (not uploaded to GitHub)
├── .gitignore
├── main.py               # Main application
│
├── 01_import.py
├── 02_pip.py
├── 03_requirements.py
├── 04_gemini_api.py
│
├── instruction.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/devgilhotra/AI-Code-Roaster.git
```

### 2. Go to the project folder

```bash
cd AI-Code-Roaster
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install google-genai python-dotenv
```

## 🔑 Setup API Key

Create a `.env` file in the root directory:

```env
GEMINI_API=your_api_key_here
```

> ⚠️ Never upload your `.env` file or API key to GitHub.

## ▶️ Run the Project

```bash
python main.py
```

## 💻 Example

```text
print apna code paste karo
Code finish hone ke baad END likho

> rint("helo world)
> END

Gemini se poch rha hoon...

🔥 Roast:
Bhai ye kaunsa Python likh rahe ho? 😂

Better code:

print("Hello World")

Level: Beginner 🐣
Score: 1/10
```

## 🎯 What I Learned

While building this project, I learned about:

- Environment variables and `.env` files
- API keys and keeping secrets secure
- Using the Google Gemini API
- Creating a Gemini client
- Prompt engineering
- Functions in Python
- Loops and user input
- Git and GitHub basics
- Using `.gitignore` to protect sensitive files

## 🚀 Future Improvements

- Add different roast levels 🔥
- Add support for more programming languages
- Create a GUI using Streamlit
- Add code complexity analysis
- Add error explanations
- Save previous code reviews

## 👨‍💻 Author

**Dev Gilhotra**

If you like this project, feel free to ⭐ the repository!