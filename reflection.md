# Reflection – Static Code Analysis Lab

### 1. Which issues were easiest and hardest to fix?
The easiest issue to fix was the **mutable default argument** — changing `logs=[]` to `logs=None` was straightforward.  
The hardest was identifying and replacing the **broad exception** handling because it required analyzing what errors might actually occur and adjusting the try–except blocks carefully.

---

### 2. Did the static analysis tools report any false positives?
Yes, **Pylint** reported the use of `global` as a design issue.  
In this small script, using a global dictionary for inventory is acceptable, so that warning can be safely ignored.  
Otherwise, all other findings were valid and helpful.

---

### 3. How would you integrate static analysis tools into your workflow?
Static analysis tools like **Pylint**, **Flake8**, and **Bandit** can be integrated into the workflow by:
- Running them locally before each commit using a pre-commit hook, or  
- Setting up **GitHub Actions** so that every pull request automatically runs these checks.  
This ensures consistent code quality and prevents security issues from reaching production.

---

### 4. What improvements did you observe after applying the fixes?
After applying the fixes, the code became:
- More secure (no `eval`, no bare `except`)
- Easier to read and maintain due to consistent naming and docstrings  
- Safer for file operations and data handling  
- Clearer with proper logging and input validation  

Overall, static analysis significantly improved both **security and readability** of the code.
