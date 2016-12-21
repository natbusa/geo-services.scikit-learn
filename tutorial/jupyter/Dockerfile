FROM jupyter/datascience-notebook 

## all in user mode, no need for root here
WORKDIR /home/$NB_USER/work

# add extra packages
ADD requirements.yml ./
RUN pip install -r ./requirements.yml

# set workdir as home, add a directory for notebooks
WORKDIR /home/$NB_USER

# add notebook files, unfortunaly both ADD and COPY,
# always add files as root, and need to be chown'ed

ADD notebooks ./notebooks

#chown the $NB_USER dir
USER root
RUN chown $NB_USER:users --recursive /home/$NB_USER

# at the end of it, revert to the $NB_USER
USER $NB_USER