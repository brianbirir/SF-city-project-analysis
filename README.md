# SF City Projects Analysis

## Introduction
The goal of this project is to determine the relevancy scores of each record contained in the San Francisco city project list of minutes based on the following criteria:

* The contractor does only large projects of 50,000 square feet or more
* The contractor does not do residential projects
* The contractor in interested in large scale projects


The results obtained from the analysis will help the contractor determined projects relevant to them.


## Setup
### Pre-requisites
The following are required before setting up the project:

* Python 3.6+
* Unix based operating system

Ensure the dataset is either of the following formats:

* Comma Separated Values file - `csv`
* Excel file - `xlsx`


### Installation
* Ensure `virtualenv` is installed in your local development environment

```
pip install virtualenv

```
* Create the Python virtual environment in the root of the project folder and activate it.

```
virtulenv venv

source venv/bin/activate
```
* Once activated, install the required Python libraries from the `requirements.txt`

```
pip install -r requirements.txt

```
## Deployment
* Create a folder called `src` and copy the relevant dataset to this folder.
* Run the following command to run the analysis and get the results. The results will be stored in a folder called `analysis_results` in `csv` format:


```
python main.py "src/FileName.xlsx"
```
