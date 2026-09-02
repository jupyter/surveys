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

The folder name becomes the page URL on [jupyter.github.io/surveys](https://jupyter.github.io/surveys), so `surveys/2026-08-foundation-survey` is served at `/2026-08-foundation-survey`.

You may also wish to provide information about how to cite the dataset, such as a DOI. If you do not have a DOI, you can obtain one by uploading the dataset to a service such as [Zenodo](http://zenodo.org/).

## Build the documentation

The documentation site in `docs/` is built with [MyST](https://mystmd.org) and deployed to GitHub Pages automatically on merge to `master`.
To build it locally, install [nox](https://nox.thea.codes) and run:

```bash
nox -s docs       # build static HTML in docs/_build/html
nox -s docs-live  # start a live-reloading dev server
```

Both sessions first run `docs/build.py links`, which symlinks each survey folder into `docs/` and adds an `index.md` next to each `README.md`. Those symlinks are ignored by git and are what gives each page its URL. `nox -s docs` then runs `docs/build.py redirects`, which writes a redirect page for each URL the site served before the folder names were used.

Jupyter user surveys
====================

Materials for and results from Jupyter user surveys are in the [`surveys/`](surveys/) folder.
See [jupyter.github.io/surveys](https://jupyter.github.io/surveys) for a browseable list.

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
