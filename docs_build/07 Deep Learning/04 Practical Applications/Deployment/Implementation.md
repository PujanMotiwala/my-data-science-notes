## Refer:
https://www.youtube.com/watch?v=19LQRx78QVU&t=43s

## Steps
Install: 
- anaconda: Jupyter lab is amazing
- if error occurs while firing jupyter notebook or lab from cmd:
	- try: running "activate base"
creating an Environment Creation workflows:
- install git
- create a new env:
	- go to the folder ImageClassification on cmd
	- "python -m venv <name of env>"
- Activate the env (in VS code & jupyter lab)
	- .\imageclassification\Scripts\activate
	- ( for mac in bash/zsh "source <venv>/bin/activate")
	- pip install ipykernal (didn't work at first, but I installed/update - restart vscode for pip to work in activated venv: )
	- check in pip list if installed (ipykernal)
- Deactivate: "deactivate"
- Use it:
	- python -m ipykernel install --name=img_class_cnn_venv

- Check how many kernals available:
	- jupyter kernelspec list
- Specifically for vs code:
	- open user settings with ctrl + shift + P
	- type: "env"
	- Python: Create Environment
	- select "Venv"
	- Enter Interpreter path
		- Browse and select python within your virtual env folder
	- Restarting VS code (might not be necessary but)
	- now you see additional kernal with the name of your project
- Specifically for vs code:
	- run jupyter lab or notebook and change the kernel to your virtual env project name

- Uninstalling virtual env:
	- jupyter kernelspec uninstall <name of kernel>
	- y

## Install TensorFlow for deeplearning
- pip install: https://www.tensorflow.org/install/source_windows
	- Looks at system requirements
	- !pip install tensorflow 
	- Diversion: still kernal does not work after selection,
	  - Updating the setting `jupyter.kernels.trusted`:
		  -   Copy the fully qualified path to the kernelspec, e.g. `D:\Py_pro\Image_Class\ImageClassification\imageclassification\share\jupyter\kernels\python3\kernel.json`
		  - Open the VS User Settings UI using the command `Preferences: Open User Settings` from the `Command Palette`.
		-   Search for the setting `jupyter.kernels.trusted`
		-   Add a new value into the list using the `Add` button
			- ex: *c:\ProgramData\jupyter\kernels\img_class_cnn_venv\kernel.json*
		-   Re-load VS Code
		- activate env again
	- Microsoft Visual C++ Build Tools - Desktop dev with C++
		- https://visualstudio.microsoft.com/downloads/



### Note: the above steps didn't work, so I tried new steps:
- Create python environment: Venv
- if not automated:
	- activate env
	- go in the env folder (keep it in virtual_envs folder)
	- pip install ipykernal
	- confirm: python -m ipykernel install --name=env_name
	- Open the VS User Settings UI using the command `Preferences: Open User Settings` from the `Command Palette`.
		-   Search for the setting `jupyter.kernels.trusted`
		-   Add a new value into the list using the `Add` button
			- ex: *c:\ProgramData\jupyter\kernels\img_class_cnn_venv\kernel.json*
		-   Re-load VS Code
		- activate env again