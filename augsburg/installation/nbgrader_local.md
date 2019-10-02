# Local installation of nbgrader

These instructions explain how nbgrader can be installed locally for demonstration
purposes and experimentation. The setup is not intended to be used in production.

The installation will be done on a Linux system and it is assumed that two users called
`teacher` and `student` have been created by means of
```
sudo adduser teacher
```
and correspondingly for the second user.
 
## Setting up a conda environment

We will use `miniconda` to set up the environment containing the required Python
packages. Alternatively, one could create an environment on top of a full Anaconda
installation, in particular, if one needs scientific libraries anyway.

### Installing `miniconda`

The latest version of `miniconda` can be obtained from
https://docs.conda.io/en/latest/miniconda.html. For our purposes, we choose
`Miniconda Linux 64-bit` for Python 3.7, the most recent Python version at the
time of writing. After downloading, it is recommended to verify the SHA256 checksum
by running
```
sha256sum Miniconda3-latest-Linux-x86_64.sh
```
and comparing the result with the checksum given on the download web page.

`miniconda` can either be installed system-wide or locally for the user `teacher`.
We will do the latter and assume that we are already logged in as `teacher`. The
installation can be run with
```
bash Miniconda3-latest-Linux-x86_64.sh
```
which will ask for acceptance of the license agreement and for the installation path
and offers to modify the `.bashrc` to automatically include the path to the `bin`
directory of `miniconda` into the path. Otherwise, one needs to call `conda` with
the full path or run
```
export PATH=$HOME/miniconda3:$PATH
```
where we have assumed that `miniconda` has been installed into the subdirectory
`miniconda3` of the user's home directory. We mention that a silent installation
of `miniconda` can be carried out by means of
```
bash Miniconda3-latest-Linux-x86_64.sh -b -p <PATH>
```
where `<PATH>` has to be replaced by the installation path.

### Installing Jupyter, Jupyterhub and nbgrader

On top of the `miniconda` installation, we create a conda environment containing 
Jupyterhub and nbgrader
```
conda create --name nbgrader python=3.7
```
where `nbgrader` will be the name of the new environment and can be named
differently. Here, we again use the most recent version of Python at the time of
writing.

We now activate our new environment
```
conda activate nbgrader
```
and install Jupyter, Jupyterhub and nbgrader
```
conda install jupyter
conda install jupyterhub
conda install -c conda-forge nbgrader
```

As an alternative, one can create a YAML file describing the environment. In our
case, the file `environment.yml` would read
```
name: nbgrader
channels:
  - conda-forge
  - defaults
dependencies:
  - jupyter
  - jupyterhub
  - nbgrader
```
Further dependencies can be added if required. The environment is then created by
means of
```
conda env create --file environment.yml
```
Now, the new environment can be activated by
```
conda activate nbgrader
```

The environment can be deactivated at any time, if necessary, by means of
```
conda deactivate
```

A prerequisite for Jupyterhub is `configurable-http-proxy`. We can now install
it globally by
```
sudo ./miniconda3/envs/nbgrader/bin/npm install -g configurable-http-proxy
```

With this installation procedure so far, parts of nbgrader will be enabled system-wide
even though we only want the user `teacher` to have the ability to create assignments,
to access the formgrader, and to possibly access the course list.

To list the enabled extensions, run
```
jupyter serverextension list
```
and
```
jupyter nbextension list
```
which will result in
```
config dir: /home/teacher/miniconda3/envs/nbgrader/etc/jupyter
    nbgrader.server_extensions.formgrader  enabled
    - Validating...
      nbgrader.server_extensions.formgrader  OK
    nbgrader.server_extensions.validate_assignment  enabled
    - Validating...
      nbgrader.server_extensions.validate_assignment  OK
    nbgrader.server_extensions.assignment_list  enabled
    - Validating...
      nbgrader.server_extensions.assignment_list  OK
    nbgrader.server_extensions.course_list  enabled
    - Validating...
      nbgrader.server_extensions.course_list  OK
```
and
```
Known nbextensions:
  config dir: /home/teacher/miniconda3/envs/nbgrader/etc/jupyter/nbconfig
    notebook section
      jupyter-js-widgets/extension  enabled
      - Validating: OK
      create_assignment/main  enabled
      - Validating: OK
      validate_assignment/main  enabled
      - Validating: OK
    tree section
      formgrader/main  enabled
      - Validating: OK
      assignment_list/main  enabled
      - Validating: OK
      course_list/main  enabled
      - Validating: OK

```
respectively. The configuration directory in the conda environment
(`.conda/envs/nbgrader`) lists the availability for all users having access to 
the environment.

We now restrict `create_assignment`, `formgrader`, and  `course_list` to the
user `teacher` by
```
jupyter nbextension disable --sys-prefix create_assignment/main
jupyter nbextension enable --user create_assignment/main
```
```
jupyter nbextension disable --sys-prefix formgrader/main --section=tree
jupyter serverextension disable --sys-prefix nbgrader.server_extensions.formgrader
jupyter nbextension enable --user formgrader/main --section=tree
jupyter serverextension enable --usero nbgrader.server_extensions.formgrader
```
```
jupyter nbextension disable --sys-prefix course_list/main --section=tree
jupyter serverextension disable --sys-prefix nbgrader.server_extensions.course_list
jupyter nbextension enable --user course_list/main --section=tree
jupyter serverextension enable --user nbgrader.server_extensions.course_list
```
The configuration can be verified by means of 
```
jupyter serverextension list
jupyter nbextension list
```
resulting in the following two lists
```
config dir: /home/teacher/.jupyter
    nbgrader.server_extensions.formgrader  enabled
    nbgrader.server_extensions.course_list  enabled
config dir: /home/teacher/miniconda3/envs/nbgrader/etc/jupyter
    nbgrader.server_extensions.formgrader disabled
    nbgrader.server_extensions.validate_assignment  enabled
    nbgrader.server_extensions.assignment_list  enabled
    nbgrader.server_extensions.course_list disabled
```
and
```
Known nbextensions:
  config dir: /home/teacher/.jupyter/nbconfig
    notebook section
      create_assignment/main  enabled
    tree section
      formgrader/main  enabled
      course_list/main  enabled
  config dir: /home/teacher/miniconda3/envs/nbgrader/etc/jupyter/nbconfig
    notebook section
      jupyter-js-widgets/extension  enabled
      create_assignment/main disabled
      validate_assignment/main  enabled
    tree section
      formgrader/main disabled
      assignment_list/main  enabled
      course_list/main disabled

```
respectively. The configuration stored in the user's directory `.jupyter` and its
subdirectory shows the extensions enabled for this user while these extensions
are now disabled for system-wide use.

## Setting up Jupyterhub

The connection to the server should be secured which in our simple case can be
done by means of a self-signed certificate. Such a certificate can be generated
by
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout jupyterhub.key -out jupyterhub.pem
```
According to the option `-days`, the certificate will be valid for 365 days. The
generated file `jupyterhub.pem` should be put in the directory `/etc/ssl/certs`
while the file `jupyterhub.key` should be put in `/etc/ssl/private`.

Moving files to these directories will typically require system administrator privileges
which can be achieved by means of `sudo`. If it is done with a newly created `teacher`
account, this user might need to be added to the `sudo` group. This step can be done
by a user already in this group by executing
```
sudo adduser teacher sudo
```
To set the owner and permissions use
```
sudo chown root:root /etc/ssl/certs/jupyterhub.pem
sudo chmod 644 /etc/ssl/certs/jupyterhub.pem
sudo chown root:ssl-cert /etc/ssl/private/jupyterhub.key
sudo chmod 640 /etc/ssl/private/jupyterhub.key
```

The paths to these files should be stored in the Jupyterhub configuration file.
First generate such a file by
```
jupyterhub --generate-config
```
and modify the corresponding entries to read
```
## Path to SSL certificate file for the public facing interface of the proxy
#  
#  When setting this, you should also set ssl_key
c.JupyterHub.ssl_cert = '/etc/ssl/certs/jupyterhub.crt'

## Path to SSL key file for the public facing interface of the proxy
#  
#  When setting this, you should also set ssl_cert
c.JupyterHub.ssl_key = '/etc/ssl/private/jupyterhub.key'
```

Jupyterhub will need to store a database and a Cookie secret. A good place
to do so is `/srv/jupyterhub` which needs to be created and should belong
to `root`.
```
sudo mkdir -p /srv/jupyterhub
```
Later, `/srv` will also contain a subdirectory acting as an exchange directory
for nbgrader.

Now, we can set the corresponding options in the Jupyterhub configuration
```
## File in which to store the cookie secret.
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'

## url for the database. e.g. `sqlite:///jupyterhub.sqlite`
c.JupyterHub.db_url = '/srv/jupyterhub/jupyterhub.sqlite'
```

We also need to define a Jupyterhub spawner
```
#  Some spawners allow shell-style expansion here, allowing you to use
#  environment variables. Most, including the default, do not. Consult the
#  documentation for your spawner to verify!
c.Spawner.cmd = ['/home/teacher/miniconda3/envs/nbgrader/bin/jupyterhub-singleuser']
```

Finally, a natural place to store the configuration is `/etc/jupyterhub` and
we move it there, even though it could be kept in a different place as well.
```
sudo mkdir -p /etc/jupyterhub
sudo mv jupyterhub_config.py /etc/jupyterhub
```

We now should be able to start Jupyterhub by
```
sudo ./miniconda3/envs/nbgrader/bin/jupyterhub -f /etc/jupyterhub/jupyterhub_config.py
```
and access it by pointing the web browser to `https://127.0.0.1:8000`. The web
browser might complain about our self-signed certificate. We can exceptionally
accept the certificate for our purposes but a self-signed certificate should not
be used in production.

## Setting up nbgrader for a course
