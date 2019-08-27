# pull miniconda
FROM continuumio/miniconda3

# define maintainer
MAINTAINER noi.nguyen "noi.nguyen@boot.ai"

# create environment
RUN conda create -n env_web python=3.7.3
RUN conda activate env_web

# Install Pip and essential build if needed
RUN yes | apt-get -qq update && apt-get install -y build-essential
RUN yes | apt-get install python-pip

# create environment
ENV INSTALL_PATH ~/app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

# copy everything into the folder and move on from there
COPY . $INSTALL_PATH

# install requirements
COPY requirements.txt requirements.txt
RUN yes | pip install -r requirements.txt

# open port
EXPOSE 5000

# turn on backend
ENTRYPOINT ["python"]
CMD ["manage.py"]

