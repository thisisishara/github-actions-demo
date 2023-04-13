# github-actions-demo
This repo demonstrated how github actions can be utilized to do dev and prod deployments of a simple flask app while using semver for automatically version based on formatted commit messages

1. First, you need to set up your repository with two branches: main and dev. The main branch is your production branch, and the dev branch is your development branch. All changes should be made on the dev branch, and once they have been tested and are ready for production, they should be merged into the main branch.

2. Next, you need to set up a CI/CD pipeline to automatically deploy your app to a development environment whenever changes are made to the dev branch. You can use a tool like Jenkins, Travis CI, or CircleCI to set up your pipeline.

3. Once your pipeline is set up, you need to configure it to use semantic versioning based on your commit messages. You can use the semantic-release library to do this.

4. To use semantic-release, you need to install it in your Flask app's repository. You can do this by running the following command in your repository's root directory:

```bash
npm install semantic-release @semantic-release/git @semantic-release/changelog @semantic-release/exec
```

5. Next, you need to create a .releaserc file in your repository's root directory. This file contains the configuration for semantic-release. Here is an example .releaserc file:

```json
{
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    "@semantic-release/npm",
    [
      "@semantic-release/git",
      {
        "assets": [
          "CHANGELOG.md",
          "package.json"
        ],
        "message": "chore(release): ${nextRelease.version}\n\n${nextRelease.notes}"
      }
    ],
    [
      "@semantic-release/exec",
      {
        "prepareCmd": "python setup.py sdist bdist_wheel"
      }
    ],
    "@semantic-release/github"
  ]
}
```
This file tells semantic-release to use the commit-analyzer and release-notes-generator plugins to determine the type of change based on your commit messages, and to generate release notes and changelogs based on those changes. It also tells semantic-release to update the version number in package.json, generate a source distribution and a wheel distribution of your app, and push the changes to Github.

6. Once you have set up your pipeline and configured semantic-release, you need to use standardized commit messages to indicate the type of change you have made. Here is an example of a commit message:

```
feat(api): add new endpoint to retrieve user data
```
In this example, feat indicates that a new feature has been added, api indicates that the change was made to the API, and add new endpoint to retrieve user data is a short description of the change.

7. Finally, whenever you make changes to your app, you should commit them to the dev branch with a standardized commit message. Your CI/CD pipeline will automatically detect the changes, run your tests, and deploy the app to a development environment. If the tests are successful, semantic-release will automatically generate a new version number based on the commit message and create a new release on Github. Once you are ready to deploy to production, you can merge the dev branch into the main branch, and your pipeline will automatically deploy the new version of your app to production.
