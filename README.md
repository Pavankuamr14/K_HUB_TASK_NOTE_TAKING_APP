# Note Taking App

**`Note_Taking_App`** is a full-stack note-taking application built with the FARM stack: FastAPI and MongoDB on the backend, and ReactJS on the frontend.

## Features

* **Create, edit, and delete notes:**  Organize your thoughts and ideas with ease.
* **Categorize notes:**  Keep your notes organized by topic or project.
* **Search notes:**  Quickly find the notes you need.
* **User authentication:**  Securely manage your notes with user accounts.
* **Responsive design:**  Access your notes from any device.

## Getting Started

### Prerequisites

* **Python 3.9.10:**  Make sure you have Python 3.9.10 installed on your system.
* **Node.js and npm (or yarn):**  Install Node.js and npm (or yarn) for the frontend development.
* **MongoDB:**  You'll need a MongoDB instance running. You can use a local instance or a hosted service like MongoDB Atlas.

### Setting up the Backend

1. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```


### How to run Locally?

## Backend

To run the backend, you need to have local mongodb instance running on you can setup a deployed instance using [MongoDB Atlas](https://www.mongodb.com/atlas/database). or use local host mongoDBcompass

### Setting up python environment

Run the following to create a virtual environment for the project. (Assuming you have python installed on local machine) and also make sure you have python 3.9.10 version on you local machine 

```bash
python -m virtualenv env
# OR
python -m venv env
#OR
python -m venv --system-site-packages env
#OR
python3 -m venv env


```

If you're running the deployed instance, make sure to change the database connection string in `.env` file on the backend.

### Setting up `.env` file

To setup `.env` file on the backend_part, create a file named `.env` in `/backend_part/app`.
Add the following in the `.env` file.

```txt
JWT_SECRET_KEY=<RAMDOM_STRING_GENERATE_BY_JWT>
JWT_REFRESH_SECRET_KEY=<RANDOM_SECTURE_LONG_STRING>
MONGO_CONNECTION_STRING=<MONGO_DB_CONNECTION_STRING>
# mongodb://localhost:27017/ <-- for local running instances
```

### Installing dependencies

Assuming you are in the base directory.

```bash
cd backend_part
pip install -r requirements.txt
```

### Activating virtual environment

```bash
# Windows
env/Scripts/activate

# MacOs + Linux
source env/bin/activate
```

### Running the backend_part

Assuming you are in the backend_part directory.

```bash
uvicorn app.app:app --reload
```

<hr>

## Frontend_PART

### Install dependecies

Assuming you are in the base directory.

```bash
cd frontend_part
```

```bash
# yarn
yarn

# npm
npm install
```

### Running frontend_part

```bash
# yarn
yarn start

# npm
npm start
# OR
npm run start

```
### Running Backend_part

```bash
# requirments 
yarn add --dev @babel/plugin-proposal-private-property-in-object

npm i cors  

# starting command
uvicorn app.app:app --reload


```
