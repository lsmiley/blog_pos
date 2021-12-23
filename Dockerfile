FROM python:3.9.3

ENV PYTHONUNBUFFERED 1

COPY manage.py gunicorn-cfg.py requirements.txt .env ./

# Set the working directory
WORKDIR /blog_pos

# add the requirements file to the working dir
COPY requirements.txt /blog_pos/

#install the requirements (install before adding rest of code to #avoid rerunning this at every code change-built in layers)
RUN pip3 install -r requirements.txt

COPY blog_pos blog_pos
COPY acctcust acctcust
COPY api api
COPY avproduct avproduct
COPY category category
COPY configmaster configmaster
COPY configtable configtable
COPY labordeliverytype labordeliverytype
COPY labordelivery labordelivery
COPY media media
COPY order order
COPY orderitem orderitem
COPY product product
COPY statusstate statusstate
COPY tntworksheet tntworksheet

#set environment vars to be used
ENV AUTHOR="IBM MSS-Lamiley"

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["gunicorn", "--config", "gunicorn-cfg.py", "blog_pos.wsgi"]

#port from the container to expose to host
EXPOSE 8000

#Tell image what to do when it starts as a container
CMD /code/start.sh