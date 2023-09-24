FROM python:3.8
LABEL authors="novar"
WORKDIR /home/novar/PycharmProjects/BoxChatMangaDetection

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python","./app.py"]

ENTRYPOINT ["top", "-b"]