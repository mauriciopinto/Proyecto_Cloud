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
#RUN apt install ca-certificates -y
#RUN apt update 
#RUN apt install curl -y 
#RUN apt install gnupg -y
#RUN apt install lsb-release -y
#RUN mkdir -p /etc/apt/keyrings
#RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
#RUN  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu bionic stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
#RUN apt update
#RUN DEBIAN_FRONTEND=noninteractive apt install docker-ce -y

#RUN DEBIAN_FRONTEND=noninteractive apt install docker-ce-cli -y
#RUN DEBIAN_FRONTEND=noninteractive apt install conteinerd.io -y
#RUN DEBIAN_FRONTEND=noninteractive apt install docker-compose-plugin -y
 
CMD ["python3", "manage.py", "migrate", "--run-syncdb"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
