# User_Connect 🔐

A **secure authentication system** built using **JWT (JSON Web Tokens)**.

This project implements:
✔ User Registration  
✔ User Login  
✔ Token-based Authentication  
✔ Protected Dashboard (only accessible with valid JWT)

---

## 🧠 Project Overview

User_Connect demonstrates how token-based authentication works in real-world applications.

After successful login:
- A **JWT token** is generated
- The token is used to access **protected routes**
- Unauthorized users are restricted from accessing the dashboard

This project focuses on **security, authentication flow, and backend logic**.

---

## ✨ Features

- User registration with validation  
- Secure login system  
- JWT token generation & verification  
- Protected dashboard route  
- Logout functionality (token removal)  

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend logic |
| Flask / Django | Web framework |
| JWT | Authentication |
| HTML/CSS | Frontend UI |
| SQLite / MySQL | Database |
| Git | Version control |

---

## 🔐 Authentication Flow

1. User registers
2. User logs in with credentials
3. Server generates JWT token
4. Token is stored (session / local storage)
5. Token is verified for protected routes
6. Dashboard is accessible only with valid token

---

## 🚀 How to Run Locally

1. Clone the repository:
