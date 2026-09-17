# Personal Expense Tracker API

A simple REST API built with Python and Flask for managing personal expenses

The API allows you to:

* Add expenses
* View all expenses
* Update an expense
* Delete an expense
* Calculate total spending
* Calculate spending by category
* Search expenses by category
* Store expense data in a JSON file
* Run the application using Docker

## Technologies Used

* Python
* Flask
* JSON
* Docker
* Git & GitHub
* Postman

## Project Structure

```text
Personal Expense Tracker/
├── main.py
├── practice.py
├── app.py
├── expense.json
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Running the Project Locally

### 1. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 2. Run the Flask API

```bash
py app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint                        | Description                       |
| ------ | ------------------------------- | --------------------------------- |
| GET    | `/`                             | Check if the API is running       |
| GET    | `/expenses`                     | Get all expenses                  |
| POST   | `/expenses`                     | Add a new expense                 |
| PUT    | `/expenses/<index>`             | Update an expense                 |
| DELETE | `/expenses/<index>`             | Delete an expense                 |
| GET    | `/expenses/total`               | Calculate total spending          |
| GET    | `/expenses/category/<category>` | Calculate spending for a category |
| GET    | `/expenses/search/<category>`   | Search expenses by category       |

## Running with Docker

### 1. Build the Docker image

```bash
docker build -t expense-tracker-api .
```

### 2. Run the Docker container

```bash
docker run -p 5000:5000 expense-tracker-api
```

The API can then be accessed at:

```text
http://127.0.0.1:5000
```

## Data Storage

Expense data is stored in:

```text
expense.json
```

The application loads the data when it starts and saves changes back to the JSON file when expenses are added, updated, or deleted.

## Testing

The API endpoints were tested using Postman for different operations and validation cases.

The Dockerized application was also tested through the browser to verify that the Flask API runs correctly inside a Docker container.
