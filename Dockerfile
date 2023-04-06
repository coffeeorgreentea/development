FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /

RUN apt-get update && apt-get install -y git libgl1 libglib2.0-0

RUN pip3 install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD server.py .
EXPOSE 8000

ADD download.py .
RUN python3 download.py

ADD app.py .
CMD python3 -u server.py
