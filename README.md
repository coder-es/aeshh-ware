# aeshh File Nuker 
Basic windows system file nuker written in python allowing: file deleting, file spamming, background changing and misc

This project was written as part of learning some basics with file spamming and overwriting. This program is made to function as a file nuker correctly but shouldnt be subsituted or used for malicous intent. 

Note: This repository contains examples of malicious files. It should be used for educational purposes only. Usage of files in this repository for any other purpose might cause you legal issues, even though the provided examples are very simple. It is advised to follow the instructions.

### INSTALLATION

1. make sure you have downloaded the latest version of [python3](https://python.org/downloads/) and [git](https://git-scm.com/download/win)

2. make sure you have the pyaescryptor and secrets pip modules installed before by using:

```
   pip install pyAesCrypt #AND# pip install secrets
```

3. clone this project into python by using:

```
   git clone https://github.com/coder-es/aeshh.git
   ```

4. change variables inside code to your needs
   
5. turn .py file into a .exe file by switching to directory where pnuker file is using:

```
   C:\Users\Name>cd C:\Users\Name\Path\Path
   ```
6. Change file .exe using code:

```
   pyinstaller --onefile pythonScriptName.py
```
7. Afterwards go back to the directory you were in before using:

```
   C:\Users\Name>cd C:\Users\Name\Path\Path
   ```

8. You will see a few new folders added, open the **dist** folder ans in there will be the .exe file.


**NOTE**
if you get an error message, you may need to install [Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
