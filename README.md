# 🚀 AI Lead Generator (Hybrid AI System)

## 📌 Overview

AI Lead Generator is a **full-stack AI-powered application** that automatically finds and qualifies potential business leads (especially small IT companies) using a hybrid approach:

* 🌐 Web Search (Google / SerpAPI)
* 🕷️ Web Scraping (BeautifulSoup)
* 🤖 AI Processing (LLM - Ollama / OpenAI)
* 💾 Data Storage (Text File)

👉 The system collects real-world company data, analyzes it, and generates **structured leads with outreach messages**.

---
## 📸 UI Preview

### 🏠 Home Screen
![Home](./assets/Screenshot2.png)

### 📊 Results
![Results](./assets/Screenshot1.png)

---

## 🧠 Key Features

* 🔍 **Smart Lead Discovery**
  Finds local businesses (Noida, Gurgaon, Delhi NCR)

* 🌐 **Google-Based Search**
  Uses SerpAPI for accurate Indian market results

* 🕷️ **Automated Web Scraping**
  Extracts useful company data from websites

* ✉️ **Email Extraction**
  Identifies potential contact emails from scraped data

* 🤖 **AI-Powered Analysis**
  Generates:

  * Company summary
  * Potential IT needs
  * Outreach message

* 💾 **Automatic Saving**
  Stores generated leads into a `.txt` file

* 🌐 **Frontend Interface (React)**
  Simple UI to input queries and view results

---

## 🧱 Tech Stack

### 🖥️ Frontend

* React.js

### ⚙️ Backend

* FastAPI

### 🧠 AI / LLM

* Ollama (LLaMA 3) 🆓
* OpenAI (optional, paid alternative)

### 🔧 Tools & Libraries

* LangChain
* BeautifulSoup
* Requests
* SerpAPI (Google Search)
* Python Regex

---

## 🏗️ Architecture

```
User Input (React UI)
        ↓
FastAPI Backend
        ↓
Google Search (SerpAPI)
        ↓
Web Scraping (BeautifulSoup)
        ↓
AI Processing (LLM)
        ↓
Structured Output
        ↓
Saved to File + Displayed in UI
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kuku-kodes/AI-agent-.git
cd ai-lead-generator
```

---

### 2️⃣ Create virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file:

```env
SERPAPI_API_KEY=your_serpapi_key
OPENAI_API_KEY=your_openai_key   # optional
```

---

### 5️⃣ Run backend

```bash
uvicorn api:app --reload --port 5000
```

---

### 6️⃣ Run frontend

```bash
cd ai-lead-frontend
npm install
npm start
```

---

## ▶️ Usage

1. Open browser → `http://localhost:3000`
2. Enter query:

   ```
   IT companies in Noida
   ```
3. Click **Generate Leads**
4. View:

   * Company details
   * Emails
   * Outreach messages

👉 Results are also saved in:

```
leads_output.txt
```

---

## 🧪 Example Output

```
Company: XYZ Tech Solutions  
Email: contact@xyz.com  
Summary: Small IT service provider focusing on cloud solutions  
Outreach: We can help improve your infrastructure...
```

---

## ⚠️ Limitations

* Local LLM (Ollama) may produce less structured output
* Web scraping depends on website structure
* API-based search (SerpAPI) may require paid plan for heavy usage

---

## 🔥 Future Improvements

* 📊 Database integration (MongoDB / PostgreSQL)
* 🎨 Advanced UI (cards, dashboards)
* 📧 Automated email sending
* 🧠 Multi-agent system
* 🌍 Deployment (Vercel + Render)

---

## 👨‍💻 Author

**Kaushlendra Kumar Verma**

---

## 💡 Inspiration

This project demonstrates how to combine:

* AI + Web Scraping
* Backend + Frontend
* Automation + Real-world business use case

👉 A step towards building **AI-powered SaaS products** 🚀

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repo
* 🍴 Fork it
* 🧠 Build something awesome with it

---

