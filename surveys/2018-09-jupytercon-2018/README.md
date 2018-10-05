# JupyterLab UX Survey

This folder contains user-testing data collected at JupyterCon 2018 (August 2018) by Cal Poly Interns and Tim George (@tgeorgeux).

The goal of the testing was to answer specific questions about JupyterLab UX. See the [analysis notebook](analysis/questions-to-answer.ipynb) for details.

## How to run the notebooks

1. Clone this repository.
2. Change directories to `surveys/2018-09-jupytercon-2018`.
3. Install dependencies.
    - If you use `pipenv`, call `pipenv install` int this directory.
    - If you use `pip`, call `pip install -r requirements.txt`
4. Run JupyterLab and open the `analysis/questions-to-answer.ipynb` notebook.
5. Run all cells.


## Data

**phosphor test**

- Code: Code name for user
- Test: test number
- Tab: are tab drop zones available in test (Y/N)
- Center: are center drop zones available in test (Y/N)
- L/B: box or line drop hints
- Task: task id.
- ST: start time
- CT: completion time.
- ToT: Time on Task
- Init: First move
- CFA: Correct first move 
- aCFA: Move used to correct a mistake.
- CEDZ: Center Edge Dropzone
- FS: First success score. (0 if first move was correct, 1 if second move was correct, 2 is failed.)
- Notes: User notes
- source: What dropzone the user started with
- target: what drop zone the user ended in
- position: the position of the target drop zone

**jupyterlab test**

- Code Name: Name of user
- Subtask #: Subtasks
- Correct Path: Solution to task
- Time User Started: time the user started
- First Action: Was the first action orrect
- First Success: were they successful on the first try?
- Second success: Were the successful on the second try?
- Eventual success: did they eventually succeed.
- Notes: notes about user.

## Credits

Cal Poly interns (Summer 2018), @ellisonbg, @tgeorgeux, @zsailer. 