
# Machine Learning DevOps with Microsoft Azure

The objective of this project is to show how we can automate some of the common machine learning tasks using the tools provided by Microsoft Azure. We will focus specially in the automatated creation of Machine Learning models using AutoML and the designing of ML pipelines, which can include any amount of data handling steps like processing of data sets, auto ML operations, publishing of models, etc. 

## Architectural Diagram
### Developing and publishing a model with AutoML
The following diagram shows a summarized process of how a model can be created and published using AutoML
![image](https://user-images.githubusercontent.com/83981857/150114927-1efdea4f-cbfd-4f8b-8176-b0b8f333aa26.png)

1. Data gathering and cleaning: Normally we would have to gather the data related to our ML project and perform some analyse using visualisations or statistical quantities. For this project we are provided with the curated data.
2. Registering the data set: Since we want to use Microsoft Azure for our ML operations we have to publish our data set in a data store on our ML studio
3. Create an AutoML run: Using the AutoML tab from the ML studio we can easily create a run by selecting our registered data set and chossing a previously created compute instance (can be a cluster). Here we have to specify which kind of task we are dealing with (classification, regression) and which part of the data should be used as an objective. The quantity to be optimized on should also be selected (accuracy, AUC, error, etc)
4. Deploy the best model: When completed we can see the whole list of models that the AutoML created. We can publish any of them by exploring it and selecting the "publish" option on ML studio; here we can select on which platform we can to publish the model, either AKS or ACI. This will provide us with an endpoint URL for consume
5. Enable logging: We can communicate to our deployed model using python and enable the logging of application insights. These provide feedback on the funcionality of our model API
6. Check the Swagger docs: Microsoft Azure provides by each deployment of a mode a .json file with documentation for Swagger. We can launch a local Swagger instance and provide it with access to this .json in order to see information regarding the methods of our endpoint (GET and POST requests layout)
7. Consume endpoint: Finally we can send POST requests to our API using the layout of Swagger and a data load. If we do it right we should get a response

To create, publish and consume a pipeline we can define the following steps:
![image](https://user-images.githubusercontent.com/83981857/150120409-d970af4f-a969-4bf8-bd95-000c8ef4a810.png)

1. Define the architecture of our pipeline: The first thing to do is to have a clear view on what our pipeline should do, i.e., to know which is the process that we want to automate. We can do this using a diagram of the ML steps that should be performed
2. Create each step with its configuration: After having a clear picture of the pipeline, we can define each step on the Azure SDK using the different available classes. This should be configured accordingly to what is needed.
3. Define the pipeline object: Having defined each of the steps we can define the pipeline object using the list of steps
4. Create a run from the pipeline using a data set: With the pipeline object available we can submit a run to an experiment by using an available data set
5. Publishing the pipeline: If everything worked fine we can publish the pipeline for consumption. This can be done on the ML studio or in Azure SDK. This will provide an endpoint, just like when publishing a model
6. Consume endpoint: We can proceed to consume the endpoint of the pipeline


## Key Steps
- Register the data set: To register the set on ML studio we just need to upload our .csv file using the Data sets tab
![EduardoGP - Registered Dataset](https://user-images.githubusercontent.com/83981857/150121255-c80d0ebd-5c6b-4e8c-97f2-c02fda47285c.PNG)

- We can start a run of AutoML using the AutoML tab and the registered data set. Here we should also define a compute instance to use. After completion we can check the experiments to see our runs:
![EduardoGP - pipeline and autoML run](https://user-images.githubusercontent.com/83981857/150122584-32f58109-08a6-4888-8365-026c84a843a6.PNG)

- The models created by AutoML can be accessed by exploring the run. We can select the best model from the list and see its accuracy, explanation, etc
![EduardoGP - Best Model AutoML](https://user-images.githubusercontent.com/83981857/150122742-38821e92-f43b-4674-9c85-94df65eb2bff.PNG)

- The deployment of the model can be done in the same tab. In this project we used a ACI with enabled authorization
- We can enable the logging of insights on this same tab or do it progammatically using python:
Before: 
![EduardoGP - Application Insights Off](https://user-images.githubusercontent.com/83981857/150123147-7abe866b-200d-40bb-a7a4-75563329b12a.PNG)
After: 
![EduardoGP - Application Insights ON](https://user-images.githubusercontent.com/83981857/150123175-8301e368-9269-41d3-95c8-2606afdddc5c.PNG)
Loggings:
![EduardoGP - insights](https://user-images.githubusercontent.com/83981857/150123228-c81c42ba-e52c-401c-a002-edd7c951e684.PNG)

- It is always useful to check the generated Swagger documentation. We can run an instance of Swagger and give it access to the generated .json. Here we can see the methods available for our model and the expected responses:
![EduardoGP - model post model](https://user-images.githubusercontent.com/83981857/150123478-54f3e6df-773d-488a-a4c4-af45bf417d9c.PNG)

![EduardoGP - model post answer](https://user-images.githubusercontent.com/83981857/150123485-959c0100-2c86-44b4-9704-28bbc629d4ab.PNG)

- 

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
