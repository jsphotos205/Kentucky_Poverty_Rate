# Kentucky Poverty Rate Model

This is a predictive model that works with population, governmental transfers, and employment data from the State of Kentucky to see if there are any tendencies for a county to be above or below the average poverty rate taken from 2003-2019.

### Libraries:

This project is written in **Python** and uses the following Python libraries installed:

* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [SciPy Stats](https://docs.scipy.org/doc/scipy/tutorial/stats.html)
* [Sklearn](https://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html).

### Steps for installation:

From your terminal at your desired location within your computer's file structure run:

`git clone https://github.com/jsphotos205/kentucky_poverty_rate.git`

Create a new Anaconda enviroment:

`conda create -n "WHATEVERNAMEYOUWANTofenv"`

Then activate newly created Anaconda enviroment:

`conda activate "WHATEVERNAMEYOUWANTofenv"`

From the terminal while located in the folder of kentucky_poverty_rate run:

`pip install -r requirements.txt`

The user might run into issues installing `sklearn`, this can be resolved by using the following command to install it:

`python 3 -m pip install scikit-learn`

#### Code Kentucky Data Analysis 1 Project Requirements :

* Standard Python data structures
* Read in data from local .csv file
  * Line 3
* Clean data
  * Line 5
* Python functions
* Pandas calculations
  * Line 7
* Seaborn Plots
  * Line 9
* Markdown and README


Throughout kentucky_pov_ml.ipynb look to the markdown notes for further information on the code presented.

### Further work to be done:

Write a program where a user can input individual county data that feeds to the model for predictive analysis of choosen county.
