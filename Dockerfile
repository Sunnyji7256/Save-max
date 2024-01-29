#https://github.com/Sunnysaloni
#https://t.me/Noob_to_pro_hack
#https://t.me/Sunny_ki_duniya

FROM python:3.9.2-slim-buster
RUN mkdir /app && chmod 777 /app
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git python3 python3-pip ffmpeg
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash","bash.sh"]
