
# Reference Notes

* Random notes, hopefully helpful on occasion.  Probably not helpful on first look.
  
# Linting

* pep8 code style
* Can check for linter errors before submitting a pull request:
  ```sh
  # (some configuration in setup.cfg)
  pycodestyle
  ```

# Unit Tests

You may notice a lack of unit tests in this codebase. Though tests exist, I omitted them because they rely on extensive
use of real world wallet data. For the sake of all users' privacy, I do not include these tests. I'm open to ideas for
alternatives or PRs for non-invasive tests, since obviously this is non-optimal.

Note to contributors: I encourage you to be proactive with changes before I find a solution to the testing problem.
Private tests are run for most txs types and perfection without those tests is not expected.  Of course, try to be 
perfect :).
  
# Docker

Sample of using a docker container

```sh
# build the docker container
docker build --platform linux/amd64 --tag staketaxcsv .

# Run/enter/mount docker container 
docker run --platform linux/amd64 -it --volume $PWD:/staketaxcsv staketaxcsv bash

# See README.md Usage section to run script(s)
```

# Run CSV job with no transaction limit

This is a common support request.  I provide some details here for those interested.  Steps:

  1. Follow `Install` section or `Docker` section to install python/packages.  For those familiar with docker, I recommend `Docker` section.
  3. Run CSV script using --limit flag

```
# Load environment variables from sample.env (add to ~/.bash_profile or ~/.bashrc to avoid doing every time)
set -o allexport
source sample.env
set +o allexport

# Run CSV job with custom high transaction limit
python3 report_sol.py <wallet_address> --limit 100000 --format all
```

# Ideal Configuration

Default code was made to work out of the box. These are changes that require manual actions. They improve reliability
(RPC Node settings) or speed (DB Cache) when compared to default version.

## RPC Node settings

* Default `sample.env` points to public RPC nodes.  This generally works, up to a point.
* Edit/uncomment `sample.env` to change to point to more reliable private RPC node(s).
  * Examples for private RPC nodes (Figment, Quicknode) are included.

## DB Cache

Use of a database for caching is ideal to speed up certain RPC queries (especially SOL). Here is the script usage to
enable caching:

```sh
cd src

# --cache flag requires working implementation of Cache class (common/cache.py)
python3 report_osmo.py <wallet_address> --cache
```

To enable --cache, you must configure an aws connection for the boto3 code found in src/common/Cache.py:

* One method: `aws configure`
  * See here to install AWS CLI: <https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html>
  * See here to use `aws configure`: <https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html>

Alternatively, you may implement your own Cache class (common/cache.py).

# Installing python 3.9 on macOS

* Personal method--google is probably better

  ```sh
  # Install brew (see https://brew.sh/)
  
  # python 3.9.9
  brew install openssl readline sqlite3 xz zlib
  brew install pyenv
  pyenv install 3.9.9
  
  # use virtualenv
  brew install virtualenv
  virtualenv -p ~/.pyenv/versions/3.9.9/bin/python3.9 env
  source env/bin/activate
  
  # install pip packages (same as README.md)
  pip3 install -r requirements.txt
  ```
