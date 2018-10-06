FROM polyhx/python-seed:2018

ADD . .

RUN pip3 install numpy
EXPOSE 3000

CMD ["python3", "server.py"]
