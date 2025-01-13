> # THIS REPO IS UNDER DEVELOPMENT, IT DOESN'T WORK
> ## I have to make it public due to some reasons

# Tweet-Analyzer
#### A Real time, optimized and user friendly model to analyze sentiment of tweets made for the brands by the users of X (Twitter).

<div align="center">
    <img width="300" src="icon.png" alt="Logo" >
</div>

<br/>

> **PROBLEM STATEMENT:**\
  Develop a real-time sentiment analysis pipeline to classify tweets (positive, negative, neutral) about a specific brand, supporting enhanced brand sentiment monitoring.

---
## Run this project
**1.** Download python3 from [here](https://www.python.org/downloads).
    
**2.** Install it on your system.
    
**3.** Run **'setup.py'** by this command ```python setup.py```. If setup.py executed succesfully, it will display a **"setup done perfectly"** message on the terminal.

**4.** If setup.py is successful, execute the below command on the terminal:
```bash
streamlit run app.py
```
**5.** Now open your browser and access this link <a href="localhost:8501">localhost:8501</a>.

---
## 🗄**File Structure**
```
--Tweet-Analyzer
    |
    |-- Tweet_Extractor
    |     |-- base
    |     |     |
    |     |     |-- assets
    |     |     |     |
    |     |     |     |-- auth.json
    |     |     |     |-- args.json
    |     |     |
    |     |     |-- __init__.py
    |     |     |-- auth_keys.py
    |     |     |-- import_lib.py
    |     |     |-- xexceptions.py
    |     |-- __init__.py
    |     |-- extractor.py
    |     |-- setup.py
    |
    |-- Tweet_Sentiment
    |     |
    |     |-- __init__.py
    |     |-- analyzer.py
    |
    |-- Tweet_Visualizer
    |     |
    |     |-- __init__.py
    | 
    |-- .gitattributes
    |-- .gitignore
    |-- app.py
    |-- LICENSE
    |-- README.md
    |-- requirements.txt
    |-- setup.py
```

---
## 📝**Coding Convention**
- **Folder names** : ```Capitalised separated by underscore.```
- **File names** : ```lowercase separated by underscore.```
- **Classes/types** : ```PascalCase.```
- **Class variables** : ```lowercase starting with underscore.```
- **Function names** : ```camelCase.```
- **Function parameters** : ```lowercase starting with '__'.```
- **Local Variables** : ```lowercase.```
- **Global Variables (constant)** : ```UPPERCASE SEPERATED BY '_'.```
- **Global Variables (non-constant)** : ```UPPERCASE trailing by '__'.```
- **Json keys**: ```lowercase separated by hyphen(-)```
---

## 🔗 Developer Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sakshamjoshi.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sakshamjoshi27)
[![Github](https://img.shields.io/badge/Visit_my-Github-purple)](https://github.com/saksham-joshi)
[![X(Twitter)](https://img.shields.io/twitter/follow/sakshamjoshi27
)](https://x.com/sakshamjoshi27)
[![Static Badge](https://img.shields.io/badge/mail_at-social.sakshamjoshi%40gmail.com-aqua)](mailto:social.sakshamjoshi@gmail.com)