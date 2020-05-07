FROM python:alpine

WORKDIR /app
COPY *.py Dockerfile requirements.txt ./

RUN pip install -r requirements.txt

ENV FLASK_APP=controller.py
ENV FLASK_ENV=development

ENV MONGO_URL="mongodb+srv://itba:3XhpA67NKDLe2rQ@itba-cluster-nitkh.mongodb.net/test?retryWrites=true&w=majority"

CMD [ "flask", "run", "--host=0.0.0.0"]