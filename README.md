# expense-manager

### Project Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
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

- **Update an existing expense:**
  ```
  PUT /api/expenses/{id}/
  ```

- **Partially update an existing expense:**
  ```
  PATCH /api/expenses/{id}/
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
