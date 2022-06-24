FROM ubuntu

RUN mkdir /home/backend
WORKDIR /home/backend

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt install -y python3 pip
RUN pip install --upgrade pip
COPY . /home/backend

RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver"]
