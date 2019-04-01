FROM ubuntu:latests

RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-flask -y
RUN apt install python3-pip -y
RUN apt install git
 


