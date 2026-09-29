- Password Strength Checker

- What it does

This is a Python password strength checker that evaluates a password against several basic security rules. It scores a password out of 6 and rates it as Weak, Medium or Strong.

- How to run

Requires Python 3

Run the program using:

```bash
python password_checker.py
```

- Security Checks

The program checks whether the password:

* Contains at least 8 characters
* Contains an uppercase letter
* Contains a lowercase letter
* Contains a number
* Contains a special character
* Is not included in a small list of common passwords

- Example Output

```text
$ python password_checker.py

Enter a password to check: password123

Password Strength: Medium
Score: 3 / 6

Checks:
✓ At least 8 characters
✗ Contains uppercase letter
✓ Contains lowercase letter
✓ Contains a number
✗ Contains special character
✗ Not a common password
```


- Why I built it 

I built this project to practise applying security-related skills in Python and to develop my programming skills for future digital-related projects, including cybersecurity, and degree apprenticeship applications.

The project also helped me practise breaking a problem into smaller, reusable functions.

- How it works

Each security requirement has its own function. The results are then combined to calculate an overall score.

The scoring system is:

0-2 checks passed = Weak
3-4 checks passed = Medium
5-6 checks passed = Strong

- Running the tests

The project includes automated tests for the individual password-checking functions and the overall password checker.

Run the tests using:

```bash
python -m unittest test_password_checker.py -v
```

The tests check different password requirements, including length, uppercase and lowercase letters, numbers, special characters, common passwords, password ratings and invalid input.

- Limitations

This is a basic educational password checker and should not be used as a complete password-security solution.

It does not check passwords against real breached-password databases. It also does not analyse whether a password is easy to guess because it contains personal information or predictable patterns.

The common-password list used by the program is also very small compared with real-world password databases.

- Future Improvements

If I developed the project further, I would:

- Use a much larger common-password dataset
- Check passwords against a breached-password database using an appropriate privacy-preserving method
- Detect predictable patterns
- Improve the scoring system
- Add a graphical user interface
- Improve input handling for additional edge cases



- Tools used

- GitHub
- Visual Studio Code
- Python

