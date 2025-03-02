Hello, before you start this lab, i want to give you some notes/advices to get the maximum from it:

* You're not supposed to understand everything from the first try, just try to discover and learn something new

* Try to read the codes before executing, to know what it'll create exactly, mainly the docker-compose.yml files and the .py files, you can get assisted by AI on this.

* Try to make a little search about each new technology you find during the lab before getting to action.

* If you get some defficulties, reach me on LinkedIn or Whatsapp

--------------------------

Lab requirement:

* python3

* pip

* docker

--------------------------

Prepare the lab's network

1- First create a docker network named "lab"

--------------------------

Set up the models registry

1- cd 0-mlflow 

2- docker-compose up -d (or: docker compose up -d)
    a- Make sure mlflow and all it's dependencies are up with: docker-compose ps (or docker-compose ps)
    b- In your browser, try to access http://localhost:5000, log in (username:mlflow_admin, password:mlflow_admin) and make sure mlflow is UP

--------------------------

Build the model and register it to the model registry (mlflow)

1- cd 1-model

2- pip install --no-cache-dir -r requirements.txt

3- Process the data: python3 data_processing.py
    a- Make sure a new dirctory created under the directory "data", named "precessed" has been created and make sure that it contains the dataset splits

4- Train the model: python3 model_training.py
    a- Go to mlflow console (http://localhost:5000) and make sure an expirement with the name "hotel_booking_cancellation_detector" has been created
    b- Click on the expirement and try to register it as a model (make a quick search on google or use AI)
    c- Find the accuracy of your model 

5- Evaluate the model: python3 eval.py 
    a- You'll find the results in the folder 1-model/reports
    b- Compare the graphs of a feature that has a data drift detected with the a feature that has no data drift.

--------------------------

Create the API that'll serve the model

1- cd 2-api 

2- docker-compose up -d (or: docker compose up -d)
    a- Make sure the API is up and running: docker-compose ps (or docker-compose ps)
    b- you should find a swagger UI when you browse to htt://localhost:8000/docs

3- install curl to test the API (or use postman if you're familiar with it): sudo apt update && sudo apt install curl

4- test the API: curl -X 'POST' 'http://localhost:8000/predict' -H 'Content-Type: application/json' -d '{"features": [30, 1, 0, 2, 3, 200.5, 0, 1, 1, 0, 2, 5, 1, 0, 1, 5, 2, 3, 1, 0, 6, 1, 1, 0, 2, 3, 0, 1]}'
    a- you should see {prediction: 1 or 0}

--------------------------

Set up an API gateway

1- cd '3-api gateway'

2- docker-compose up -d (or: docker compose up -d)
    a- Make sure the API gateway is up and running: docker-compose ps (or docker-compose ps)

3- Retest your API but this time via the API Gateway: curl -X 'POST' 'http://localhost:8081/gateway/predict' -H 'Content-Type: application/json' -d '{"features": [30, 1, 0, 2, 3, 200.5, 0, 1, 1, 0, 2, 5, 1, 0, 1, 5, 2, 3, 1, 0, 6, 1, 1, 0, 2, 3, 0, 1]}'

4- you should see same results you had when testing the API directly

--------------------------

Set up prometheus and grafana

1- cd 4-prometheus

2- docker-compose up -d (or: docker compose up -d)
    a- Make sure prometheus is up and running: docker-compose ps (or docker-compose ps)

3- cd 5-grafana

4- docker-compose up -d (or: docker compose up -d)
    a- Make sure grafana is up and running: docker-compose ps (or docker-compose ps)

5- Go to http://localhost:3000 and log in (username: admin, password: admin)

6- in the menu on the left, go to "connections", and select "Data sources"

7- Click "Add new data dource"

8- Click "prometheus"

9- in Connection, paste the prometheus server URL: http://prometheus:9090 

10- in the bottom click "save and test", you should see "successfully queried the prometheus API"

11- Click the + button in the upper right corner and select "Import Dashboard"

12- in the "load dashboard by ID" input, paste the following ID 20651, and click load

13- once you see the dashboard, go and retest you API via the API gateway using curl with many requests, get back to your dashboard, you should now see some numbers:
    a- Get the total number of requests you made
    b- Get the average response time
    c- Get the worst latency

--------------------------

Set up Uptime Kuma

1- cd '6-uptime kuma"

2- docker-compose up -d (or: docker compose up -d)
    a- Make sure uptime kuma is up and running: docker-compose ps (or docker-compose ps)

3- Go to http://localhost:3001 and create your admin account

4- Once you're signed in, cretae a new monitor by clicking "Add new Monitor"

5- In URL paste: http://api:8000 

6- decrease the heartbeat interval to 20 seconds

7- Go to the bottom and click save

8- Make sure that the checks are made each 20 seconds and explain based on the monitor config, what checks are being done exactly (what info it gives you as a devops engineer)

--------------------------

Thank you!