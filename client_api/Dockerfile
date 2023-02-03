FROM python:3.10

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/
COPY . /usr/src/app/

RUN git clone https://github.com/vishnubob/wait-for-it.git
RUN chmod +x ./wait-for-it/wait-for-it.sh

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./wait-for-it/wait-for-it.sh", "$POSTGRES_HOST:$POSTGRES_PORT", "--", "python", "api.py"]