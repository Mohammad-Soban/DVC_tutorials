### This is the complete tutorial on how to work with DVC

### Why To Version Data?
- Data is as important as code which can be changed over time.
- With the change in data the model performance can also change and the artifacts generated can also change.
- To keep track of the data and the artifacts generated, we need to version the data.
- DVC is a version control system for data which is open-source and works with Git.

### What is DVC?
- DVC stands for Data Version Control.
- DVC is an open-source version control system for data science and machine learning projects.
- DVC is designed to handle large files, data sets, machine learning models, and code.
- DVC is built to make ML models shareable and reproducible.

### How DVC Works?
- DVC connects to Git repositories and stores file contents in cloud storage (AWS S3, Google Cloud, Azure or even local storage).
- DVC gives a unique hash key to each file and stores the hash key in the DVC file which can be stored with each version of git.
- It means that for every new version of git, we will have a unique hash key for each data file which needs to be mapped to that version of git and this key is stored in the git repository. It acts as a pointer to the data file stored in the cloud storage.

### DVC Installation
- Open the terminal in the folder where you want to install DVC and run the following command: `pip install dvc`

### DVC Initialization
- To initialize DVC in the project run the following command: `dvc init`
- This will create a `.dvc` folder in the project which will store the cache and the DVC configuration.

### DVC Configuration

