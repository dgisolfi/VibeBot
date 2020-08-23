FROM python:3.8
MAINTAINER Daniel Gisolfi
RUN apt-get update -y \
    && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential

EXPOSE 5080

WORKDIR /bot
COPY ./VibeBot ./VibeBot
COPY setup.py .
COPY README.md .

RUN python3 -m pip install .

CMD ["python3", "-m", "VibeBot"]