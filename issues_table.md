# Static Code Analysis – Issues and Fixes

| **Issue Type** | **Tool** | **Line(s)** | **Description** | **Fix Approach** |
|----------------|-----------|--------------|------------------|------------------|
| Mutable default argument | pylint | 8 | Function `addItem` used `logs=[]`, causing data to persist across calls | Changed default to `None` and initialized a new list inside the function |
| Bare `except:` | bandit / flake8 / pylint | 19 | Used `except:` without specifying error type | Replaced with `except KeyError` and `except Exception as e` |
| Insecure `eval()` | bandit / pylint | 59 | `eval("print('eval used')")` could execute arbitrary code | Removed completely |
| Unused import | flake8 / pylint | 2 | `logging` imported but unused in original file | Added proper logging setup to use it |
| `open()` without context manager | pylint | 26, 32 | Files opened without `with` and no encoding specified | Used `with open(file, "r"/"w", encoding="utf-8")` |
| Naming style violations | pylint | multiple | Function names used CamelCase (`addItem`) instead of snake_case | Renamed functions to follow `snake_case` convention |
| Missing docstrings | pylint | multiple | Functions lacked docstrings for clarity | Added one-line docstrings to all functions |
| Broad `Exception` catch (post-fix) | pylint | 52, 81 | Still flagged as general catch | Kept intentionally for fallback safety in small scripts |

---

✅ **Summary:**  
All major issues flagged by Bandit, Flake8, and Pylint were addressed.  
Security vulnerabilities (`eval`, `bare except`) were fixed, logging and validation were added, and PEP-8 compliance was improved.
