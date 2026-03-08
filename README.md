# Secure Authentication & Vulnerability Lab 

A full-stack web application simulation built with **Python (Flask)** and **SQLite** to demonstrate common web vulnerabilities and implement industry-standard security mitigations.

---

##  Key Security Features

### 1. SQL Injection (SQLi) Mitigation
* **Vulnerability:** Demonstrated how string concatenation in SQL queries leads to authentication bypass.
* **Solution:** Implemented **Parameterized Queries** to sanitize user inputs and prevent SQLi attacks.

### 2. Strong Password Policy
* **Validation:** Enforced server-side checks using **Regex**.
* **Requirements:** At least one uppercase letter, one lowercase letter, one digit, and a minimum length of 8 characters.

### 3. Account Lockout Mechanism
* **Protection:** Added a counter for failed login attempts in the database.
* **Action:** Automatically locks accounts after **3 unsuccessful attempts** to mitigate Brute-Force attacks.

### 4. Secure Session Management
* **Fixation Protection:** Implemented **Session ID Regeneration** upon every successful login.
* **Inactivity Timeout:** Configured automatic session expiration after 5 minutes for enhanced security.

---

##  Tech Stack
* **Backend:** Python (Flask Framework)
* **Database:** SQLite3
* **Frontend:** HTML5 & CSS3
