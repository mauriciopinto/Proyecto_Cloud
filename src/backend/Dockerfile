FROM ubuntu

RUN mkdir /home/backend
WORKDIR /home/backend

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt install -y python3 pip
RUN pip install --upgrade pip
COPY . /home/backend

EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
