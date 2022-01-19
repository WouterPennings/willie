# Do not use this. Right now it does boot, but it will not run Loop code. 
# It does not have the rights to read files

FROM python:3.9
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python3", "-u", "willie.py"]
