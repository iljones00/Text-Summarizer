# End to End Text Summarization Project

This project is an exploration into building full end-to-end NLP projects using a pretrianed LLM hosted by Hugging Face. I utilize a variety of technologies to build an application API that allows the user to both train and infer for the task of text summarization. 
For this project, I used Docker to create a container for replicability, and create various data structures in Python
that wrap around a Pegasus-CNN pretrained model. More info here --> https://huggingface.co/google/pegasus-cnn_dailymail. 
This model was pretrained on a large daily mail dataset and then fine-tuned on a Dialogue Summarization dataset DialogSum.
More info here --> https://paperswithcode.com/dataset/dialogsum. This dataset contains 13,460 dialogues with their corresponding
human generated summaries and topics. 

After finetuning the model on the dataset, I built a prediction and an inference pipeline linked to FastAPI python application for 
local use. This can be run locally like this:

1. `git clone https://github.com/iljones00/Text-Summarizer`
2. `pip install requirements.txt`
3. `python3 app.py`
4. Once the app is running, go to localhost:8000 to interact with the FastAPI UI. Alternatively you can interact with the api with 
any other HTTP client.
5. Both the train and the predict endpoints should be available.
6. Post a dialog that you would like to summarize and receive the results!

The model was hosted on AWS Sagemaker but I took it down because its expensive lol. You can train the model on EC2 if you would like
but I commented out the CICD for deployment for local use instead.





# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	#optional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI =

    ECR_REPOSITORY_NAME = text-sum


This code is based off of the KrishNaik06 Youtube channel with this repo as a model: https://github.com/krishnaik06/Text-Summarization-NLP-Project/tree/main