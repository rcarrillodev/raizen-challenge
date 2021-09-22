# RAIZEN | Code Challenge Solution

This project contains my approach for the RAIZEN Code challenge (see **Challenge_spec.md** for more info).

The project contains a Docker file to build an image of the service that can be deployed using docker-compose.

----

##How to deploy with docker

- Ensure that you have docker and docker-compose installed
- Run `docker build . -t sensors-service` (this will create our image)
- Deploy the database and the service by executing: 
  ```
  docker-compose up
  ```

The docker-compose will pull the mysql server and seed the data from the `sensors-database/sensor-data.csv` file.

Once it finished the deployment the service will be available through `localhost:8000/sensors/v1/data`

---
The API is documented in the OpenAPI3 file located in `sensors/schema/resources/sensors-schema.yml`

---

Thanks for your time! 
Rafael Carrillo
@rcarrillodev