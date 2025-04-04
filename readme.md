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
- Also a `.dvcignore` file will be created which will store the files which are to be ignored by DVC.

### DVC Configuration
- We need to now provide the storage path where the data files will be stored.
- To configure the storage path run the following command: `dvc remote add -d storage <path>`
- Note that `storage` is just a name given to the storage path which can be anything. 

### DVC Data Versioning
- To add a data file to DVC run the following command: `dvc add <path to data file>`
- This will help in telling DVC that the `<path to data file>` is to be versioned and all the contents which would be prensent in that folder or that file needs to be .
- This also adds the data file to the `.gitignore` file so that the data file is not tracked by git.
- Also inside the project we get a `.dvc` file which contains the hash key of the data file which is stored in the cloud storage. (Here data.dvc file will be created.)
- After getting the changes in gitignore file and the new data.dvc file, we need to add the changes to git by running the command: `git add .` and then `git commit -m "Message"` so that the changes are saved in the git repository.
- Then we need to push the changes to the remote repository by running the command: `git push origin master`
- Now we need to commit the changes to the DVC by running the command: `dvc commit` and then push the changes to the remote storage by running the command: `dvc push`
- This will push all the files to the remote storage and the data file will be versioned and also another file will be pushed which would store the metadata of the data file and the hash key of the data file.

*NOTE : The above steps can only be done if git is not tracking the `<path to data file>`. Also the git needs to be initialized in the project.*

### If git is already tracking the `<path to data file>`
- If git is already tracking the `<path to data file>` then we need to run the following command: `git rm -r --cached <path to data file>`
- Then we need to run the command git commit -m "Message"
- Then we can add the data file to DVC by running the command: `dvc add <path to data file>`

### To check the status of the data files
- To check the status of the data files run the following command: `dvc status`

### To check the history of the data files
- To check the history of the data files run the following command: `dvc history`
- This will show the history of the data files and the hash keys of the data files.

### To check the contents of the data files
- To check the contents of the data files run the following command: `dvc cat <path to data file>`
- This will show the contents of the data files.
- This will also show the hash key of the data file.
- To get a specific version of the data file run the following command: `dvc checkout <path to data file>`

### To rollback to a previous version of the data file
- To rollback to a previous version of data along with the code, first rollback the code using the command `git checkout <commit id>` to a particular commit id or git pull to get the latest version of the code.
- Then run the command `dvc pull` to get the data file of that commit id or that version.
- This will get the data file of that version and the code will be in sync with the data file.

### To remove a data file from DVC
- To remove a data file from DVC run the following command: `dvc remove <path to data file>`
- This will remove the data file from DVC and also remove the data file from the remote storage.