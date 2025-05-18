# CookieCutter Template Repo

This repo is a template repository through GitHub, which contains some GitHub Actions to run Cookiecutter on copies of it which set up the project based on the info provided in the creation steps. There should be no manual at any stage of the process.

## Setup Steps

1. [Create repo from template](https://github.com/Iamdomchap90/project-template).
2. Enter the repo name for your project, this should follow the guidance in the [Repository Naming Wiki](https://wiki.Iamdomchap90.net/wiki/RepositoryNaming/), eg. `example-client`.
3. Add the clients **live** domain as the description. 
4. Press "Create repository" & wait for the actions to finish.


## Your first PR

As this template ships with very few migrations, it's highly encouraged that the first PR adds any model changes and migrations that are needed for the project. This will allow tests to run without failing due to missing migrations.


## Local development of the Project Template

This will work like any other project. Once you have `project-template` locally you can `cd` into the `{{ cookiecutter.repo }}` and use `docker compose up web`. Note that this deliberately ships with minimal migrations as it is intended to be used as a template for new projects which may change fields/models from the start. `# # ` and `# ` tags will need to be manually removed.