FROM cityofzion/neo-privatenet

WORKDIR /opt/neo-python
RUN mkdir /opt/neo-python/sc
COPY sc /opt/neo-python/sc