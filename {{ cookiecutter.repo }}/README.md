# {{ cookiecutter.client_name }}
---
## Client Live Domain
---

Dev Site: https://develop-{{ cookiecutter.repo }}.dev.Iamdomchap90.net

Live Site: {{ cookiecutter.live_domain }}

## Overview
---

- Python Version: `3.11`
- Poetry Version: `1.4.2`
- Django Version: `4.1.4`
- Infrastructure: `Dokku`
- ...

## Requirements
---

- Docker ([Windows](https://docs.docker.com/docker-for-windows/install/), [OSX](https://docs.docker.com/docker-for-mac/install/), [Linux](https://docs.docker.com/install/linux/docker-ce/centos/))
- Make ([Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows), [OSX](https://formulae.brew.sh/formula/make), [Linux](https://askubuntu.com/a/1363822))
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Poetry](https://python-poetry.org/docs/#installation) (optional)

Once you have the required dependencies you can get up and running with a single command:

```bash
make
```

This will create a `virtualenv` for you with the correct Python version and install the project requirements. It also symlinks `manage.py` into the target environment `/root/.local/bin` folder so you can call `manage.py` from anywhere within the poetry shell.

## Running the Project Locally
---

Before first running the project, bring up the database and wait for it to start with:

```bash
docker compose up db -d
```

Then run the initial set of migrations with:

```bash
docker compose run web src/manage.py migrate
```

Once this is complete you can stop the database with:

```bash
docker compose stop db
```

After you have run the setup instructions above, you can run the project as normal with either:

```bash
docker compose up web
```

Alternatively, if you wish to avoid `docker compose` capturing output (so you can use debugging tools like `pdb`) you can run directly via:

```bash
docker compose run --service-ports web src/manage.py runserver 0.0.0.0:8000
```

### Local Mail Delivery

In order to easily test emails, this project uses MailHog.

The `mail` container will automatically start with `web` and provides a nice web
interface accessible locally via http://0.0.0.0:8025

### Application Index Pages

Application index pages extend a slightly different template `index-base.html`, which contains common settings for index pages and should be inherited for applications where suitable (e.g. `news/index.html`).

### Password Reset Flow

Currently the password reset is purely for admin accounts. Therefore templates/registration/password_reset_complete.html has been overwritten to return to admin login instead of a 'regular' member login. To expand functionality to use for both a membership and admin login. the registration/login.html template will need to be added (along with others) and the current template can be removed.


## Frontend - Building
---

### Requirements

- NPM ([Windows/OSX/Linux](https://nodejs.org/en/download/))
- Yarn ([Windows/OSX/Linux](https://classic.yarnpkg.com/lang/en/docs/install/))
- Docker ([Windows](https://docs.docker.com/docker-for-windows/install/), [OSX](https://docs.docker.com/docker-for-mac/install/), [Linux](https://docs.docker.com/install/linux/docker-ce/centos/))
- Make ([Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows), [OSX](https://formulae.brew.sh/formula/make), [Linux](https://askubuntu.com/a/1363822))
- [Docker Compose](https://docs.docker.com/compose/install/)

### Building the Frontend Locally

navigate into the `./frontend` directory and run
```bash
make build
make watch
```
Which will compile from SASS and ES6 (in `build/src/`) to CSS and JS. This build directory is also symlinked from `build/dist/` to `src/core/static/dist/`.

## Tests
---

You can run tests by either:

```bash
make test
```

or

```bash
docker compose run web bash
DEPLOY_ENV=test python src/manage.py collectstatic --noinput
DEPLOY_ENV=test pytest src/
```


## Deployment
---

### Requirements

- [Local SSH Config](https://wiki.Iamdomchap90.net/wiki/ConnectOverSSH/)

### Dokku - Setup Infrastructure

Infrastructure for the project can be set up through the use of the [dokku-tools](https://github.com/Iamdomchap90/dokku-tools), documentation for doing so can be found  in the [wiki](https://wiki.Iamdomchap90.net/wiki/SettingUpADokkuInstance/).

### Dokku - Automated Deployment

Automated continuous deployment is handled through the GitHub Actions files located in `.github/workflows`. For more information on how these work, refer to the [full documentation](https://wiki.Iamdomchap90.net/wiki/GitHubWorkflowDocs/).

### Dokku - Manual Deployment

Before deploying a project manually you may optionally want to install the [official dokku client](https://dokku.com/docs/deployment/remote-commands/). Giant specfic instructions can be found [here](https://wiki.Iamdomchap90.net/wiki/InfrastructureInstallLocalClient/).

In order to manually deploy a project to a server you will first need to add it as a git remote with:

```bash
git remote add <shortname> dokku@giant-<env>:<dokku-env>-{{ cookiecutter.client_name }}
```

Where `<shortname>` is the name you wish to reference when pushing (usually  `dokku-dev` or `dokku-live`), `<env>` is the envrionment you wish to push to (e.g. `dev`), and `<dokku-env>` is the prefix for the respective environment (e.g. `develop`)

Once this has been done you can then run either of the below commands to deploy manually:

```bash
make dev-deploy
```

or

```bash
git push <shortname> develop
```
