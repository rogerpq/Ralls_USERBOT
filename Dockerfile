FROM rogerpq/Ralls_USERBOT:latest

# نسخ رابط السورس 
RUN git clone https://github.com/rogerpq/Ralls_USERBOT.git /root/userbot
# اخـراج العـمل 
WORKDIR /root/userbot

# لتنـزيل اضافات السورس
RUN pip3 install -U -r resources/setup/requirements.txt

ENV PATH="/home/userbot/resources/setup/bin:$PATH"

CMD ["python3","-m","userbot"]
