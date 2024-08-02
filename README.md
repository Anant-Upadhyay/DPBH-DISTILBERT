# Dark Pattern Buster

This repository was created for the Dark Pattern Buster Hackathon conducted by IIT-BHU.

## Description

We used data from a research paper accessible [here](https://www.kaggle.com/datasets/anantup/working-dp/data).

We fine-tuned the DistilBERT model for classifying dark patterns into the following categories:

- Urgency
- Not Dark Pattern
- Scarcity
- Misdirection
- Social Proof
- Obstruction
- Sneaking
- Forced Action

Our model achieved a good F1 score of 0.8 on the validation set. For training details, refer to the notebook distilbert.ipynb provided in the repository, along with the output files (Notebook_output).

## How to Use

Our model is deployed using Flask and can be accessed through Docker.

### Steps to Run the Web App:

1. *Download and Set Up Docker Desktop:*
   - [Download Docker Desktop](https://www.docker.com/products/docker-desktop) and install it.

2. *Clone the Repository:*
   - Open your CLI and run:
     bash
     git clone https://github.com/Anant-Upadhyay/DPBH-DISTILBERT.git
     

3. *Start Docker Compose:*
   - Navigate to the cloned repository directory and run:
     bash
     docker compose up -d
     

4. *Launch the Web App:*
   - Open Docker and click on the link to launch the web app on your local server.

## Screenshots

Here are some screenshots of our web app:

1. ![Screenshot 1](Screenshots/Screenshot%20(73).png)
2. ![Screenshot 2](Screenshots/Screenshot%20(74).png)
3. ![Screenshot 3](Screenshots/Screenshot%20(75).png)



