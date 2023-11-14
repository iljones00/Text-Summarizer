# End to End Text Summarization Project

This project is an exploration into building full end-to-end NLP projects using a pretrained LLM hosted by Hugging Face. I utilize a variety of technologies to build an application API that allows the user to both train and infer for the task of text summarization. 
For this project, I used Docker to create a container for replicability, and create various data structures in Python
that wrap around a Pegasus-CNN pretrained model. More info here --> https://huggingface.co/google/pegasus-cnn_dailymail. 
This model was pretrained on a large daily mail dataset and then fine-tuned on a Dialogue Summarization dataset DialogSum.
More info here --> https://paperswithcode.com/dataset/dialogsum. This dataset contains 13,460 dialogues with their corresponding
human generated summaries and topics. 

This is one example dialog from the dataset:

Hannah: Hey, do you have Betty's number?
Amanda: Lemme check
Hannah: <file_gif>
Amanda: Sorry, can't find it.
Amanda: Ask Larry
Amanda: He called her last time we were at the park together
Hannah: I don't know him well
Hannah: <file_gif>
Amanda: Don't be shy, he's very nice
Hannah: If you say so..
Hannah: I'd rather you texted him
Amanda: Just text him 🙂
Hannah: Urgh.. Alright
Hannah: Bye
Amanda: Bye bye

Here is the target response:
Hannah needs Betty's number but Amanda doesn't have it. She needs to contact Larry.

And this is the output from the model:
Larry called Betty last time they were at the park together. He's very nice. Hannah wants Amanda to text him. Amanda says she'd rather she text him.

The length of the summary can be cut down further by giving the model a larger length penalty than I am currently using but overall
not bad. When compared to a a non-finetuned model, the pretrained model straight from hugging face returned this:

Amanda: Ask Larry Amanda: He called her last time we were at the park together .<n>Hannah: I'd rather you texted him .<n>Amanda: Just text him.

As you can see the formatting does get improved with a few thousand training examples to what the user may want. 

After finetuning the model on the dataset, I built a prediction and an inference pipeline linked to FastAPI python application for 
local use. This can be run locally like this:

1. `git clone https://github.com/iljones00/Text-Summarizer`
2. `pip install requirements.txt`
3. `python3 app.py`
4. Once the app is running, go to localhost:8000 to interact with the FastAPI UI. Alternatively you can interact with the api with 
any other HTTP client.
5. Both the train and the predict endpoints should be available.
6. Post a dialog that you would like to summarize and receive the results!

My model was trained on Google Colab though it is possible to train it locally on a 16 GB GPU.

The model was hosted on AWS Sagemaker but I took it down because its expensive lol. You can train the model on EC2 if you would like
but I commented out the CICD for deployment to keep it working for local use instead. The trained model is located in the repository at under `/artifacts/model_trainer/pegasus-samsum-model/` and the dataset is located at `/artifacts/data_ingestion/samsum-dataset/`


For reference here are additional instructions for hosting the application on EC2 and have a continuous integration system in place:


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