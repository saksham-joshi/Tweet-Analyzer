> ## UNDER DEVELOPMENT


# Tweet-Analyzer
#### A Real time, optimized and user friendly model to analyze sentiment of tweets made for the brands on X (Twitter).

<div align="center">
    <img width="300" src="./Tweet_Visualizer/static/assets/rounded-corner-logo.png" alt="Logo" >
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
python app.py
```
**5.** Now the terminal wil display a URL like this: ```Running on http://192.168.X.XXX:5000```, access that URL through your browser and surf your website.
<i> <b> *Also, if you want to view your site on other devices through the above URL, then those other devices must be connected to the same network and their system must specify the network as private.* <b> </i>

---
## 🗄**File Structure**
```
--Tweet-Analyzer
    |
    |-- Tweet_Extractor
    |     |
    |     |-- base
    |     |     |
    |     |     |-- assets
    |     |     |     |
    |     |     |     |-- auth.json
    |     |     |     |-- args.json
    |     |     |
    |     |     |-- tweety
    |     |     |     |
    |     |     |     |-- (view from github.com/mahrtayyab/tweety)
    |     |     |
    |     |     |-- __init__.py
    |     |     |-- auth_keys.py
    |     |     |-- import_lib.py
    |     |     |-- xexceptions.py
    |     |
    |     |-- __init__.py
    |     |-- extractor.py
    |     |-- setup.py
    |
    |-- Tweet_Sentiment
    |     |
    |     |-- __init__.py
    |
    |-- Tweet_Visualizer
    |     |
    |     |-- graph
    |     |     |
    |     |     |-- __init__.py
    |     |     |-- generator.py
    |     |
    |     |-- html
    |     |     |
    |     |     |-- project.mobirise
    |     |
    |     |-- static
    |     |     |
    |     |     |-- assets
    |     |     |     |
    |     |     |     |-- animatecss
    |     |     |     |     |
    |     |     |     |     |-- animate.css
    |     |     |     |
    |     |     |     |-- bootstrap
    |     |     |     |     |
    |     |     |     |     |-- css
    |     |     |     |     |     |
    |     |     |     |     |     |-- bootstrap-grid.min.css
    |     |     |     |     |     |-- bootstrap-reboot.min.css
    |     |     |     |     |     |-- bootstrap-min.css
    |     |     |     |     |
    |     |     |     |     |-- js
    |     |     |     |           |
    |     |     |     |           |-- bootstrap.bundle.min.js
    |     |     |     |     
    |     |     |     |-- css
    |     |     |     |     |
    |     |     |     |     |-- fontawesome.min.css
    |     |     |     |
    |     |     |     |-- dropdown
    |     |     |     |     |
    |     |     |     |     |-- css
    |     |     |     |     |     |-- style.css
    |     |     |     |     |
    |     |     |     |     |-- js
    |     |     |     |           |
    |     |     |     |           |-- navbar-dropdown.js
    |     |     |     |     
    |     |     |     |-- font-awesome-solid
    |     |     |     |     |
    |     |     |     |     |-- css
    |     |     |     |     |     |
    |     |     |     |     |     |-- solid.min.css
    |     |     |     |     | 
    |     |     |     |     |-- fonts
    |     |     |     |           |
    |     |     |     |           |-- fa-solid-900.ttf
    |     |     |     |           |-- fa-solid-900.woff2
    |     |     |     |     
    |     |     |     |-- images
    |     |     |     |     |
    |     |     |     |     |-- webp + png files ...
    |     |     |     |     
    |     |     |     |-- mobirise\css
    |     |     |     |     |
    |     |     |     |     |-- fontawesome.min.css
    |     |     |     |     |-- mbr-additional.css
    |     |     |     |
    |     |     |     |-- smoothscroll
    |     |     |     |     |
    |     |     |     |     |-- smooth-scroll.js
    |     |     |     |  
    |     |     |     |-- socicon
    |     |     |     |     |
    |     |     |     |     |-- css
    |     |     |     |     |     |
    |     |     |     |     |     |-- style.css
    |     |     |     |     |
    |     |     |     |     |-- fonts
    |     |     |     |           |
    |     |     |     |           |-- socicon.eot
    |     |     |     |           |-- socicon.svg
    |     |     |     |           |-- socicon.ttf
    |     |     |     |           |-- socicon.woff
    |     |     |     |           |-- socicon-woff2
    |     |     |     |-- theme
    |     |     |     |     |
    |     |     |     |     |-- css
    |     |     |     |     |     |
    |     |     |     |     |     |-- style.css
    |     |     |     |     |
    |     |     |     |     |-- js
    |     |     |     |           |
    |     |     |     |           |-- script.js
    |     |     |     |     
    |     |     |     |-- web\assets
    |     |     |     |     |
    |     |     |     |     |-- mobirise-icons-bold
    |     |     |     |     |     |
    |     |     |     |     |     |-- mobirise-icons-bold.css
    |     |     |     |     |     |-- mobirise-icons-bold.eot
    |     |     |     |     |     |-- mobirise-icons-bold.svg
    |     |     |     |     |     |-- mobirise-icons-bold.ttf
    |     |     |     |     |     |-- mobirise-icons-bold.woff
    |     |     |     |     |
    |     |     |     |     |-- mobirise-icons2
    |     |     |     |           |
    |     |     |     |           |-- mobirise2.css
    |     |     |     |           |-- mobirise2.eot
    |     |     |     |           |-- mobirise2.svg
    |     |     |     |           |-- mobirise2.ttf
    |     |     |     |           |-- mobirise2.woff
    |     |     |     |     
    |     |     |     |-- ytplayer
    |     |     |     |     |
    |     |     |     |     |-- index.js
    |     |     |     |       
    |     |     |     |-- circular-logo.png
    |     |     |     |-- rounded-corner-logo.png
    |     |     |     |-- square-logo.png
    |     |     |
    |     |     |-- img
    |     |          |
    |     |          |-- favicon.ico
    |     |          |-- sorry_image.png
    |     |     
    |     |-- templates
    |     |     |
    |     |     |-- index.html
    |     |
    |     |-- __init__.py
    |     |-- base.py
    |     |-- cache.py
    |     |-- util.py
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

## 💳**Credit**
#### This Project uses <a href="https://github.com/mahrtayyab/tweety/"> Tweet-ns </a> by <a href="https://github.com/mahrtayyab"> @Mahrtayyab </a> to extract tweets from X (Twitter) and I don't claim its ownership and authenticity.

---

## 🔗 Developer Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sakshamjoshi.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sakshamjoshi27)
[![Github](https://img.shields.io/badge/Visit_my-Github-purple)](https://github.com/saksham-joshi)
[![X(Twitter)](https://img.shields.io/twitter/follow/sakshamjoshi27
)](https://x.com/sakshamjoshi27)
[![Static Badge](https://img.shields.io/badge/mail_at-social.sakshamjoshi%40gmail.com-aqua)](mailto:social.sakshamjoshi@gmail.com)