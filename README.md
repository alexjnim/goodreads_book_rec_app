# goodreads book recommendeer application

Find more info about this app and see it running [here](https://alexnim.com/coding-projects-book-rec-app.html).

Here contains code for a book recommender application built in Flask. This will include the following features:
- selecting book titles for the recommender system
- select the number of recommendations to retrieve
- shuffle results
- results shown with image and link to google search for more info

# Install

```bash
cd app

python3.9 -m venv book_rec_env

source book_rec_env/bin/activate

pip install -r requirements.txt
```

# Run

```bash
# make sure you're in the "app" folder

python app.py
```

# Data
The raw data for this project has been included in the data folder, however, the source location can be found [here](https://github.com/zygmuntz/goodbooks-10k).

# Files and File Structure Details
- data/ : this contains the base data used to build the similarity matrix 
- resources/ : this contains all the classes and functions used in the application
- static/ : this contains all the CSS and JavaScript code required to render the frontend. 
- templates/ : this contains the frontend HTML

The following files were written for the purpose of deploying the API on Heroku's server. 
- requirements.txt : this contains all the python libraries that need to be installed in order to run the app
- runtime.txt : this tells Heroku the version of Python you are using
- Procfile : this will give instructions to Heroku to run the app using gunicorn

# run flask app

```
cd app

source app_env/bin/activate

flask run
```


# build docker container

```shell
cd app

# login to dockerhub
docker login

# build image
docker build -t alexnimjli/book_rec_flask_app .

# run image as container
docker run <imageID>

# see available containers
docker ps
# enter container
docker exec -it <containerID> bash

# push to dockerhub
docker push alexnimjli/book_rec_flask_app
```

# run service via docker-compose

```shell
docker-compose up
# now open localhost:80

# exit
docker-compose down
```
# run service via minikube

``` shell
minikube start

# now in another terminal
cd kubernetes

kubectl apply -f .

# now back to the minikube terminal
# get service url
minikube service <service_name> --url


```

# next steps

[] - need to build a multi container pod





# resources

https://stackoverflow.com/questions/44532946/should-i-have-separate-containers-for-flask-uwsgi-and-nginx
https://www.baeldung.com/linux/nginx-config-environment-variables
https://philchen.com/2019/07/15/scaling-a-python-flask-app-with-nginx-using-multiple-containers-with-docker-compose
https://linchpiner.github.io/k8s-multi-container-pods.html
https://stackoverflow.com/questions/73785638/deploying-flask-app-with-gunicorn-behind-nginx-on-kubernetes-cluster
https://stackoverflow.com/questions/20766684/what-benefit-is-added-by-using-gunicorn-nginx-flask

https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits
https://www.fullstackpython.com/wsgi-servers.html

https://octopus.com/blog/difference-clusterip-nodeport-loadbalancer-kubernetes

https://levelup.gitconnected.com/implemeting-a-reverse-proxy-server-in-kubernetes-using-the-sidecar-eebba956801a ≈