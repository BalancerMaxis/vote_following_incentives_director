# For a base/default test run:


### Copy constants.py.example to constants.py.
Make sure you copy/not rename so your config file isn't part of changes to the mother branch of your fork.

### Take a quick look at example_op_config.py, which is actvated based on FILE_PREFIX in constants.py
These 2 files are how you control stuff, assuming not too much has changed, the current config should be good enough to do something.

### Go back to the root of the repo and run
```bash
pip3 install -r requirements.txt
python main.py
```

### Check test results in the outputs folder
There's some example outputs there already.

To run for real, you want to follow a pattern similar to that described in `.github/workflows/main.yml`, passing in some arguments to main.