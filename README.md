Secure Authentication & Vulnerability Lab 
A full-stack web application simulation built with Python (Flask) and SQLite to demonstrate common web vulnerabilities and implement industry-standard security mitigations.

Features & Security Tasks
The application is divided into two modules: a Vulnerable Login (to demonstrate exploits) and a Secure Login (to demonstrate mitigations).

SQL Injection (SQLi) Mitigation:
Demonstrated how string concatenation leads to authentication bypass.
Implemented Parameterized Queries to sanitize inputs and prevent SQLi attacks.

Strong Password Policy:
Enforced server-side validation using Regex to ensure password complexity (Uppercase, Lowercase, Numbers, min-length 8).

Account Lockout Mechanism:
Implemented a security counter to track failed login attempts in the database.
Automated account locking after 3 unsuccessful attempts to prevent Brute-Force attacks.

Secure Session Management:
Implemented Session ID Regeneration upon successful login to prevent Session Fixation.
Configured session timeouts to ensure automatic logout after inactivity.

Tech Stack:
Backend: Python 3.x, Flask Framework.
Database: SQLite3.
Frontend: HTML5, CSS3.
