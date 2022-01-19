
# Machine Learning DevOps with Microsoft Azure

The objective of this project is to show how we can automate some of the common machine learning tasks using the tools provided by Microsoft Azure. We will focus specially in the automatated creation of Machine Learning models using AutoML and the designing of ML pipelines, which can include any amount of data handling steps like processing of data sets, auto ML operations, publishing of models, etc. 

## Architectural Diagram
### Developing and publishing a model with AutoML
The following diagram shows a summarized process of how a model can be created and published using AutoML
![image](https://user-images.githubusercontent.com/83981857/150114927-1efdea4f-cbfd-4f8b-8176-b0b8f333aa26.png)

1. Data gathering and cleaning: Normally we would have to gather the data related to our ML project and perform some analyse using visualisations or statistical quantities. For this project we are provided with the curated data.
2. Registering the data set: Since we want to use Microsoft Azure for our ML operations we have to publish our data set in a data store on our ML studio
3. Create an AutoML run: Using the AutoML tab from the ML studio we can easily create a run by selecting our registered data set and chossing a previously created compute instance (can be a cluster). Here we have to specify which kind of task we are dealing with (classification, regression) and which part of the data should be used as an objective. The quantity to be optimized on should also be selected (accuracy, AUC, error, etc)
4. Deploy the best model: When completed we can see the whole list of models that the AutoML created. We can publish any of them by 

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
