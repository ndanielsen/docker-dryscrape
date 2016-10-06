FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y \
    python-pip \
    python-dev \
    python-lxml \
    build-essential \
    qt5-default \
    libqt5webkit5-dev \
    xvfb \
    git


RUN pip install --upgrade pip && pip install \
    lxml \
    xvfbwrapper \
    bs4 \
    dryscrape

ADD xvfb.init /etc/init.d/xvfb
RUN chmod +x /etc/init.d/xvfb


# copy all files to /app
COPY . /app

# change working directory to /app
WORKDIR /app

# expose port
EXPOSE 5000

# run python
#ENTRYPOINT [""]

# run app
CMD (service xvfb start; export DISPLAY=:10; python get_dc_data.py)
