FROM python:latest

WORKDIR /app

COPY . /app

RUN pip3 install flask

EXPOSE 8096


ENTRYPOINT [ "python"] 
CMD ["app.py"]