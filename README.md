# expense-manager

### Project Setup

1. **Clone the repository:**
   ```sh
   git clone git@github.com:vusallyv/expense-manager.git
   cd expense-manager
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

### Available API Endpoints

#### Expense Endpoints

- **List all expenses:**
  ```
  GET /api/expenses/
  ```

- **Retrieve a specific expense:**
  ```
  GET /api/expenses/{id}/
  ```

- **Create a new expense:**
  ```
  POST /api/expenses/
  ```
  **Request Body:**
  ```json
  {
    "user": <user_id>,
    "title": "Some title",
    "amount": "100.0",
    "date": "2024-11-22",
    "category": "Travel"
  }
  ```

- **Update an existing expense:**
  ```
  PUT /api/expenses/{id}/
  ```
  **Request Body:**
  ```json
  {
    "amount": "150.0",
    "title": "Updated title",
    "category": "Food",
    "date": "2023-10-02"
  }
  ```

- **Partially update an existing expense:**
  ```
  PATCH /api/expenses/{id}/
  ```
  **Request Body:**
  ```json
  {
    "amount": "120.0"
  }
  ```

- **Delete an expense:**
  ```
  DELETE /api/expenses/{id}/
  ```

- **Get expenses within a date range:**
  ```
  GET /api/expenses/date_range/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&user=<user_id>
  ```

- **Get category summary for a specific month and year:**
  ```
  GET /api/expenses/category_summary/?user=<user_id>&month=<MM>&year=<YYYY>
  ```

#### Documentation Endpoints

- **Swagger UI:**
  ```
  GET /swagger/
  ```

- **ReDoc:**
  ```
  GET /redoc/
  ```
