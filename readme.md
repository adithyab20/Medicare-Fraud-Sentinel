# 🛡️ Medicare Fraud Sentinel: A Personal Deep Dive into Healthcare AI

## 💡 The Core Mission
I built the **Medicare Fraud Sentinel** to tackle a massive real-world challenge: the billions of dollars lost annually to healthcare fraud and billing errors. As a Data Science professional, my goal was to move beyond simple spreadsheets and build an intelligent, automated system that can "smell" suspicious activity in vast government datasets before it becomes a financial drain.

## 🛠️ How I Built It

### 🏗️ Phase 1: The Engineering Foundation
No AI model is better than the data it consumes. I started by building a custom ingestion engine in Python. The real challenge here was dealing with the unpredictable nature of government portals—links can break, and file structures often shift. I engineered a robust solution using `Pandas` and `Requests` that handles complex, multi-sheet Excel workbooks, ensuring that the raw data is cleaned, normalized, and ready for analysis without manual intervention.

### 🔍 Phase 2: Finding the Narrative
Before jumping into machine learning, I acted as a data detective. In my exploratory phase, I realized that looking at total spending was a trap—larger states will naturally always spend more. I engineered a "Payment Per Enrollee" feature to level the playing field, allowing me to compare a small territory to a massive state fairly. Using `Seaborn` and `Matplotlib`, I visualized the first red flags in regions like New Jersey, New York, and Florida, where spending per person was significantly higher than the national average.

### 🧠 Phase 3: The AI "Sentinel"
To take this to the next level, I implemented an **Isolation Forest**—an unsupervised machine learning algorithm. Unlike traditional models that need to be told exactly what fraud looks like, this AI works by isolating data points that are simply "too different" from the norm. By training this model on service utilization and payment patterns, the system automatically flagged 7 high-risk regional anomalies. It didn't just find the high-spenders like Arizona and Florida; it identified "hidden" anomalies in places like American Samoa, where the patterns were mathematically distinct from the rest of the country.

## 🏆 The Impact
The result is a project that doesn't just show data—it provides a verdict. I’ve created a reusable pipeline that takes messy, raw healthcare files and outputs a prioritized list of regions that require an audit. This project demonstrates how robust data engineering and anomaly-detection AI can be combined to protect public resources and uncover hidden fiscal risks.

---

## 💻 Tech Stack & Tools
* **The Brain:** Python 3.11 with Scikit-Learn for the AI core.
* **The Engine:** Pandas and OpenPyXL for heavy-duty data engineering.
* **The Vision:** Matplotlib and Seaborn for uncovering regional spending stories.
* **The Lab:** Jupyter Notebooks for prototyping and Git for version control.