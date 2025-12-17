
# AI SOC Analyst

AI SOC Analyst is a Streamlit app that uses **GPT-2** to analyze log files, detect suspicious activity, and provide easy-to-understand explanations.

---

## Features

- Upload `.log` files for analysis  
- Detect suspicious IPs and events  
- GPT-2 generates human-readable explanations  
- Simple web interface using Streamlit  

---

## Installation

1. Clone the repository:  
```bash
git clone <your-repo-url>
cd AI-SOC-Analyst
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Hugging Face token:

```bash
export HF_TOKEN=<your-token>  # Windows: set HF_TOKEN=<your-token>
```

---

## Usage

Run the app:

```bash
streamlit run app.py
```

1. Upload your `.log` file
2. Click **Analyze**
3. View the suspicious activity report

---

## Demo

Here’s how the AI SOC Analyst app looks:

![AI SOC Analyst App](screenshot.png)
---

## Technologies Used

* Python 3
* Streamlit
* GPT-2 (Hugging Face)
* Pandas & Regex for log parsing

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

```

---


