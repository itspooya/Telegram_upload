FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "/app/tlg.py" ]