# Use apache+php as source
FROM php:7.2-apache


# update & install
RUN apt-get update && apt-get install -y --no-install-recommends \
	mysql-client \
	mysql-server \
	python3 \
	python3-pip \
	python3-numpy \
	python3-matplotlib

	
# copy '/' structure
COPY /root/ /

# copy main
COPY main /

# execute main command
CMD /main
