FROM 073645649421.dkr.ecr.eu-central-1.amazonaws.com/python-alpine37:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "demo.py" ]
