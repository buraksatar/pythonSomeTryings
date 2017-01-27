#1 Installing Conda

https://www.continuum.io/downloads

#2 upgrade conda

conda upgrade --all

#3 some codes
conda list

conda install numpy scipy pandas

#creating enviroment
conda create -n env_name python=2 list of packages

conda create -n IntroDataAnalysis python=2 numpy pandas

source activate my_env

source deactivate
deactivate

# List environments
conda env list

# Remove environments
conda env remove -n env_name

# FOR JUPITER
to install - conda install jupyter notebook
to open - jupyter notebook 
