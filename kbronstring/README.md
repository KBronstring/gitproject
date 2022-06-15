# Azure Devops


## Getting Started
1. Go to https://azure.microsoft.com/en-us/services/devops/ and Sign in into Azure Devops. 
2. Select the provided organization and project.
3. Check that there is a repository called kbronstring.
4. Create a pipeline base on the previous repository. Confirm that it runs without errors.

Contact with the teacher if the repository is not present, you cannot access it or the pipeline presents errors.



## Question 1 Branching strategy 25%

Take a look to the provided repository and its branching strategy. If you think that the branching strategy is not the more adequate, modify it accordingly and **push your changes**. 

Add below a list of the branches that you think that are necessary including a small summary:

```
Popular branching model.
Main branches
    master
    develop

Supporting branches
    Feature branches
    Release branches
    Hotfix branches

I would add a backup one as well
```

## Question 2 Adding script steps 25%

Take a look to the provided ```azure-pipelines.yml```. The following steps should be added to the develop branch **following best practices on doing pull requests**:

1. Install and run **flake8** in the folders ```app``` and  `tests`.
2. Install and run **isort**, which is to sort imports alphabetically, in the folders ```app``` and  `tests`.
3. Install and run **black**, which is a Python code formatter, in the folders ```app``` and  `tests`.



## Question 3 Kubernetes templates 25%

Take a look to the provided yaml files in the folder ```manifests```. Check for inconsistencies in those files and modify them accordingly. Finally, add those changes to the develop branch **following best practices on doing pull requests**.



## Question 4 Adding new tests 25%

Take a look to the application and the tests provided in the folders ```app``` and ```tests``` respectively. The following tests should be added to the develop branch **following best practices on doing pull requests**:

1. Test that the REST API will return as output 'Empty input' if no number is provided.
2. Test that the REST API will return as output 'Not a numerical value' if a string is provided.
3. Any additional test that might be interesting, at least there is one more.



Finally, add all the changes to the production branch **following best practices on doing pull requests**.