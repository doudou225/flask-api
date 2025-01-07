FROM python:3-alpine3.15
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 3333
CMD python ./api.py
