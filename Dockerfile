FROM clojure:tools-deps as builder

RUN apt-get update && apt-get install xz-utils stow -y
RUN apt-get install python3-pip -y
RUN python3 -m pip install requests

WORKDIR /opt/vendor/node
COPY ./setup-node.py ./setup-node.py
RUN python3 setup-node.py

WORKDIR /tmp/builder

RUN useradd -m -s /bin/bash bot
USER bot
