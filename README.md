# SWET-python-flask-react

## TripAdvisor who??

In this project, we set out to kill all competition with our amazing software engineering and testing skills that we definitely didn't just use GPT-4 for... (for school reasons, this is a joke)
 
 ## Prerequisites

- Python
- Node.js
- npm

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
`cd C:\Users\YourUsername\Documents\Example\SWE-gr12-python-flask-react`
That path is just an example. You can simple right click the folder and open Command prompt or Powershell straight into the folder.

3. Install the required Python dependencies with `pip install -r requirements.txt`.
4. Install Node.js and npm if they are not already installed. You can download them from [here](https://nodejs.org/en/download/).
5. Navigate to the React.js directory `SWE-gr12-python-flask-react/client`.
6. Install the required Node.js dependencies with `npm install`.
7. Install Jest and React Testing Library for testing React components: `npm install --save-dev jest @testing-library/react @types/jest`

## Running the Application

1. Start the Flask server.
2. Start the React development server with `npm run dev`.
3. Navigate to port `http://localhost:5173/` and use the app through that link

Tada

## Running the Tests

1. Run your tests with the `jest` command. If you want to run tests whenever a file changes, you can use the `--watch` flag: `npx jest --watch`
2. Add a `jest` script in your `package.json` file if it's not there, but it should be: 

json
"scripts": {
"test": "jest"
}

3. Now you can run your tests with `npm test`.


## Contribution

If you want to work with us, instead of working directly on the main branch, 

1. **Create a new branch for each feature or bug fix:**
    Use GitHub Desktop to create a new branch and switch to it.

2. **Commit Changes:**
    After making changes, use GitHub Desktop to commit those changes to your feature branch.
    Write a descriptive commit message to explain what was done.

3. **Push Changes:**
    Push your committed changes to the remote repository on GitHub. This will create the feature branch on GitHub.

4. **Pull Changes:**
    Regularly pull changes from the remote repository to keep your local copy up to date with your team's work.

5. **Handling Conflicts:**
    If there are merge conflicts when pulling, resolve them in your local copy, commit the changes, and push.

6. **Create Pull Request:**
    Once your feature or bug fix is complete and tested, use GitHub to create a pull request from your feature branch to the main branch.

7. **Review and Merge:**
    Team members can review the code in the pull request and discuss changes.
    Once everything looks good, merge the pull request into the main branch.