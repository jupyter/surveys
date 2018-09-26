# JupyterLab UX Survey

This folder contains user-testing data collected at JupyterCon 2018 (August 2018) by Cal Poly Interns and Tim George (@tgeorgeux).

The goal of the testing was to answer specific questions about JupyterLab UX. See the [analysis notebook](analysis/questions-to-answer.ipynb) for details.

**How to run the notebook**



**Data Columns**

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

## Credits

Cal Poly interns (Summer 2018), @ellisonbg, @tgeorgeux, @zsailer. 