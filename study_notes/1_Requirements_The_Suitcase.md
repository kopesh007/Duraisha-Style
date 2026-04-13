# 💼 Deployment Step 1: The Suitcase (Requirements)

### ❓ What is it?
The `requirements.txt` file is a plain text file that lists every Python library (like Django, mysqlclient, etc.) your project needs to survive.

### 🎯 The Purpose:
When you move your project to a cloud server, you don't send the `virtual` folder (it's too big and only works on your Windows laptop). Instead, you send this "Shopping List." The server reads the list and automatically downloads exactly what you need.

### 🛠️ How we did it:
We ran the command:
`pip freeze > requirements.txt`
- `pip freeze`: Lists all installed tools.
- `>`: "Pours" that list into a file.

---

### ⚠️ The "Encoding Trap" (Our first error!)
**The Error:** When we first ran this in PowerShell, the file was saved in **UTF-16 encoding**. 
**What happened:** When Render (the server) tried to read the list, it couldn't understand the "Language" of the file. It looked like gibberish to the server, so the deployment failed.

**The Solution:** We had to convert the file to **UTF-8 encoding** (the global language of the internet). 

---

### 💡 Pro Tip:
Always double-check your `requirements.txt` after installing a new tool (like Gunicorn or WhiteNoise) to make sure they are added to the list!
