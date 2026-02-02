# AutoDeploy-CI-CD-Pipeline-with-Docker-Jenkins

## About the Project

This project was built to gain **real hands-on experience** with CI/CD and Docker, rather than just learning concepts theoretically.

The main goal was to understand how an application can be **automatically built and deployed** whenever code is pushed to GitHub. For this, I created a simple Python Flask application and set up a **Jenkins pipeline** that builds a Docker image and deploys the application as a running container.

While building this project, I faced and fixed several real-world issues related to Git branches, Jenkins pipelines, and Docker permissions, which helped me understand how CI/CD works in practical environments.

---

## Technologies Used

* Python (Flask)
* Jenkins (Declarative Pipeline)
* Docker
* Git & GitHub
* Linux (Ubuntu)

---

## How the Project Works

1. Code is pushed to the GitHub repository
2. Jenkins pulls the latest code automatically
3. Jenkins builds a Docker image using the Dockerfile
4. Any existing container is stopped and removed
5. A new container is started with the updated image
6. The application becomes available through the browser

The application is deployed on the **Jenkins agent machine** where Docker is installed.

---

## Project Structure

* `app.py` – Simple Python Flask application
* `requirements.txt` – Python dependencies
* `Dockerfile` – Instructions to build the Docker image
* `Jenkinsfile` – CI/CD pipeline configuration
* `README.md` – Project documentation

---

## Jenkins Pipeline Overview

The Jenkins pipeline performs the following steps:

* **Checkout SCM**: Jenkins fetches the latest code from GitHub
* **Build Docker Image**: Docker image is built using the application code
* **Deploy Container**: Old container is removed and a new one is deployed

The pipeline is written using a **Declarative Jenkinsfile**.

---

## Accessing the Application

After a successful pipeline run, the application can be accessed at:

```
http://<jenkins-agent-ip>:5000
```

---

## What I Learned from This Project

* How CI/CD pipelines work in real environments
* Difference between Jenkins controller and agent
* How Docker is used to ensure consistent deployments
* Why infrastructure setup (Docker installation) is separate from pipeline logic
* How to read Jenkins logs and identify where failures are happening
* Troubleshooting real issues like:

  * `master` vs `main` branch errors
  * Duplicate SCM checkout in Jenkins

## Author

**Srilatha Nallala**
Aspiring DevOps / Cloud Engineer
Focused on learning through real-world, hands-on projects


