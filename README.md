
README.md


# 💰 Expensify - Expense Manager App
A clean, premium, and production-ready Expense Manager application built with **Django** and **PostgreSQL**. Track your income, manage expenses, set monthly budgets, and visualize your financial health with interactive charts.

## ✨ Features
- **User Authentication**: Secure Login & Sign Up system.
- **Dashboard**: Real-time overview of Income, Expenses, and Balance.
- **Smart Insights**: Interactive donut chart visualizing spending distribution.
- **Transaction Tracking**: Add and view income/expense records with category tagging.
- **Budget Management**: Set monthly budgets per category to stay on track.
- **Modern UI**: Clean, responsive interface with a dark sidebar and glassmorphic elements.
## 🛠️ Tech Stack
- **Backend**: Python, Django 5
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3 (Custom Premium Design), Chart.js
- **Environment**: Python-dotenv for secure configuration
## 🚀 Getting Started
Follow these steps to set up the project locally.
### Prerequisites
- Python 3.10+
- PostgreSQL installed and running
### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/expense-manager.git
   cd expense-manager
   ```
2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install django psycopg2-binary python-dotenv
   ```
4. **Configure Database & Environment**
   - Create a PostgreSQL database named `expense_db`.
   - Create a `.env` file in the root directory:
     ```env
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     ALLOWED_HOSTS=localhost,127.0.0.1
     DB_NAME=expense_db
     DB_USER=postgres
     DB_PASSWORD=your_db_password
     DB_HOST=localhost
     DB_PORT=5432
     ```
5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```
6. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000` in your browser.
