
---

# 📸 Instagram Unfollower App  

**GitHub Repository:** [DevXAlchemy/instagram-unfollower-app](https://github.com/DevXAlchemy/instagram-unfollower-app/tree/dev)  

## 📌 Overview  
Instagram Unfollower App is a simple UI-based tool that helps users track who has unfollowed them on Instagram. Built with **Streamlit**, it leverages the **Instagrapi** library to securely fetch follower and following lists without web scraping.  

## ✨ Features  
- 🔐 **Secure Login** – Users enter their Instagram credentials directly in the UI  
- 🔍 **Check Unfollowers** – Identify users who unfollowed you  
- 🖼 **Display Profile Pictures** of unfollowers  
- 🚀 **One-Click Unfollow** feature  
- ⚡ **Fast & Secure** – Uses Instagrapi instead of web scraping  
- 📊 **Simple UI** – Built with Streamlit for easy interaction  

## 🛠 Tech Stack  
- **Frontend:** Streamlit (Python-based UI)  
- **Backend:** Python (Instagrapi)  

## 📂 Project Structure  
```
instagram-unfollower-app/
│── instagram_unfollowers.py  # Streamlit UI and Python logic for fetching and processing data
│── README.md                 # Project documentation
│── requirements.txt          # Python dependencies
└── .gitignore                # Ignored files
```

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone -b dev https://github.com/DevXAlchemy/instagram-unfollower-app.git
cd instagram-unfollower-app
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application  
```bash
streamlit run instagram_unfollowers.py
```

## 🔑 How It Works  
1. **Login via UI** – Enter your Instagram username & password in the app.  
2. **Fetch Follower Data** – The app retrieves your **followers** and **following** lists.  
3. **Identify Unfollowers** – The app compares both lists and displays users who no longer follow you.  
4. **Unfollow with One Click** – Optionally, unfollow users directly from the app.  

## ⚡ Optimizations  
✅ **Secure Authentication** – Credentials are entered in the UI and not stored  
✅ **Efficient API Usage** – Uses Instagrapi for direct and secure data retrieval  
✅ **One-Click Unfollow** – Easily manage non-followers  

## 🏗 Future Enhancements  
✅ Add session-based login to prevent frequent logins  
✅ Improve UI design with better visualization  
✅ Include additional insights (e.g., inactive followers)  

---