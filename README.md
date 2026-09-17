 Password Strength Checker

 What it does:

  This is a Python password strength checker that evaluates a password against several basic security rules. Scoring a password out of 6 and rates it as Weak, Medium or Strong.

 Security checks:

The program checks whether the password:

- Contains at least 8 characters
- Contains an uppercase letter
- Contains a lowercase letter
- Contains a number
- Contains a special character
- Is not included in a small list of common passwords

Why I built it:

I built this project to practice applying security-related skills in Python and to develop my programming skills for future digital  related projects (cybersecurity etc) and degree apprenticeship applications.

The project also helped me practice breaking a problem into smaller functions, testing each part individually and handling unexpected inputs. 

 How it works:

Each security requirement has its own  function. The results are then combined to calculate an overall score.

The scoring system is:

- 0–2 checks passed: Weak
- 3–4 checks passed: Medium
- 5–6 checks passed: Strong

 Limitations:

This is a basic educational password checker and should not be used as a complete password-security solution. It does not check passwords against real breached-password databases. It also does not analyse whether a password is easy to guess because it contains personal information or predictable patterns. 

The common-password list used by the program is also very small compared with real-world password databases.

 Future improvements:

If I developed the project further, I would:

- Use a much larger common-password dataset
- Check passwords against a breached-password database using an appropriate privacy-preserving method
- Detect predictable patterns
- Improve the scoring system
- Add a graphical user interface
- Add automated tests
- Improve input handling and error checking

Tools used 

* GitHub
* Visual Studio Code
