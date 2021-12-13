# Platzi_Python_Selenium
Basic automated test cases using Python and Selenium.

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white" /> <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" /> <img src="https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white" />
## Steps:
1. Checkout and download this repo
2. Download chromdriver according to you current Chrome explorer version. [Download here](https://chromedriver.chromium.org/)

3. Install all the required python modules:

```
py get-pip.py
pip install selenium
pip install pyunitreport
pip install python-dotenv
pip install ddt
```

4. Creta an .env file in the root foler of the project and write you environmental variable with the path of the chromedriver.exe. Like this: 

```
CHROMEDRIVER_PATH=C:/Users/myPC/Python_Selenium/chromedriver.exe
```

5. Run any of the files for testing in the src folder. For example:

```
py src/test_001.py
```

## Important Note
:warning: Some of the current methods could be deprecated, depending of the version of selenium you are runing. 
