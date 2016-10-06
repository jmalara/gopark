#!/usr/local/bin/python3
from modules.ForemanAPI import ForemanConnect
foreman = ForemanConnect()
rows = foreman.getHosts('test')
print(rows)