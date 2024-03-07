<h1 align="center">Vehicles Backend</h1>

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. First of all, clone the repository and then follow the steps below.

### Prerequisites <a name = "prerequisites"></a>
To run it locally you need to have `docker` and `docker-compose` installed.
First you need to clone the repository and then run the following commands to get the project up and running.

  - Step 1: `docker-compose build` # will build the image
  - Step 2: `docker-compose up -d` # will start the image, this will run a development server for the app in localhost:8000

You can also do it in one step by running `docker-compose up --build -d`

There is another way if you don't have docker installed. You can use `make` to run the project. 
  - Step 1: `make install` # will create a new environment with venv, then will install the required dependencies listed in requirements.txt
  - Step 2: `make run` # will run a development server for the app in localhost:8000

## Making requests to the API <a name = "requests"></a>

The API is now running at `http://localhost:8000`. You can use tools like Postman or cURL to make requests to the API.

```bash
curl -X GET http://localhost:8000/api/v1/vehicles/
```

You can filter and sort by using query parameters. For example, to filter by cars and sort by year:

```bash
curl -X GET http://localhost:8000/api/v1/vehicles/?vehicle_type=CARS&ordering=year
```

You can also use the browsable API by visiting `http://localhost:8000/api/v1/vehicles/` in your web browser.
The browsable API is a built-in feature of Django REST Framework that allows for easy exploration of the API. We can use it to test the API endpoints and make requests. We also can filter and sort the data.

The admin interface is running at `http://localhost:8000/admin/`. Access it through the web browser. To log in you can use the superuser account that was created earlier automatically when the app started.

Credentials for the admin interface are as follows:

```bash
    username: admin
    password: admin
```

In this interface you can add, edit and delete vehicles. There are also features such as filtering and searching for vehicles. You can manage the users and groups which can access the admin interface as well.


## 🔧 Running the tests <a name = "tests"></a>

`docker-compose run web python manage.py test`

or

`make test`

## 🚀 Planned Enhancements <a name = "enhancements"></a>

    - Data: Add soft delete functionality to the API to handle data deletion.
    - Configure a production database like PostgreSQL to replace the default SQLite database.
    - Authentication: Implement API authentication to secure endpoints.
    - Pagination: Add pagination to API responses to handle large datasets efficiently.
    - External Image Storage: Configure external storage solutions like AWS S3 with Django storages for media files.
    - Image Processing: Develop features for automatic image retouching and resizing, and deliver images in multiple resolutions.
    - Environment-Specific Settings: Create multiple settings files to support various environments (development, testing, production).
    - Error Management with Sentry: Integrate Sentry for real-time error logging and aggregation.
    - API Caching with Redis: Implement Redis as a caching backend to replace LocMemCache for improved performance across multiple servers.
    - Deployment: Automate deployment with CI/CD pipelines using Github Actions.

