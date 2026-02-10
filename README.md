# Local Setup Guide: GenAI Workshop (Lessons 5.1 - 5.4)

--

### 1. Create the Environment
Save the `environment.yml` file in your project folder, open your terminal (or Anaconda Prompt), and run:

```bash
conda env create -f environment.yml
```

### 2. Configure Your Keys
Create a file named `.env` in your project folder and paste the following, replacing the placeholders with your actual keys:

```bash
GROQ_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
HF_TOKEN=your_key_here
TELEGRAM_BOT_TOKEN=your_key_here
```

### 3. Initialization Code
Paste this into the **first cell** of your Jupyter Notebook to load your keys and log into Hugging Face automatically.

```python
import os
from dotenv import load_dotenv
from huggingface_hub import login

# Load keys from .env
load_dotenv()

# Required keys for the lessons
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY", "")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN", "")
```

---
### 4. Running the Notebook
1. Start Jupyter: `jupyter notebook`
2. Open your lesson file.
3. Click **Kernel** -> **Change Kernel**.
4. Select **"GenAI Local"**.