This is a demo using DVC implementing simple workflow to maintain ML model version. 

For advanced use case, we would apply DVC to maintain data versioning as well.

Below is the image for the pictorial representation of the usecase.

![simple-workflow](https://user-images.githubusercontent.com/55927390/134888979-c341dc8d-fc5e-48d8-be44-4531cdb0ca78.png)

Create and activate conda environment in VS Code
	conda create -n dvc-ml python=3.7 -y
	conda activate dvc-ml
	
Create a setup file.

Create a requirements file and install dependencies.

Initialize dvc.

Create the basic directory structure.
	mkdir -p src/utils

Create the config file.
	config/config.yaml
	
Create the stage 1 file and all utils file in src.
	touch src/stage01_loadandsave.py src/utils/all_utils.py
	
Create the dvc.yaml and add the stage.

Execute the dvc repro command to build the pipeline based on the stages.
		dvc repro