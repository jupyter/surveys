# Jupyter Surveys

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter/surveys/master)

This repository contains datasets and surveys collected by Project Jupyter and IPython.

## Adding data to this repository

To add a dataset to this repository, please create a subdirectory with the syntax `YYYY-MM-short-description` under
the relevant top-level directory. For example, if it is survey data, create the folder under the `surveys` top-level
directory. In that directory, please create a new `README.md` file with a short description of the data, including:

* The date(s) it was collected
* Who collected the data
* What the population was (if human data), where the code can be found (if simulated data), or other relevant information about the source of the data

You may also wish to provide information about how to cite the dataset, such as a DOI. If you do not have a DOI, you can obtain one by uploading the dataset to a service such as [Zenodo](http://zenodo.org/).

Jupyter user surveys
====================

Materials for and results from Jupyter user surveys.

- [May, 2016 Jupyter in Education results](surveys/2016-05-education-survey)
- [December, 2015 Notebook UX survey results](surveys/2015-12-notebook-ux)
- [August, 2018 JupyterLab UX testing results](surveys/2018-09-jupytercon-2018)

IPython user surveys
====================

Materials for and results from IPython user surveys.

We ran IPython user surveys in 2011 and 2013 and the results are included in this repo. The writeups are also on the
IPython website:

- [2011 survey results](http://ipython.org/usersurvey2011.html)
- [2013 survey results](http://ipython.org/usersurvey2013.html)

## Licensing

The default license of all data in this repository is [CC0](LICENSE). If a dataset uses a different license, it should be
included it in the subdirectory for the dataset. Any subdirectory licenses take precedence over the repository license.
