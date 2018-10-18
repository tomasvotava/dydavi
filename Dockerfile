# Use apache+php as source
FROM php:7.2-apache

# copy apache config

# copy php config

# copy web app code

# update
RUN apt-get update && apt-get install -y --no-install-recommends \
	mysql-client \
	mysql-server \
	python3 \
	python3-pip \
	python3-numpy \
	python3-matplotlib

COPY main /

# enter main command
CMD /main

