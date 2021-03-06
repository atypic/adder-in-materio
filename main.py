import ga

import emEvolvableMotherboard
from ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
prot = TBinaryProtocol.TBinaryProtocol(transport)
cli = emEvolvableMotherboard.Client(prot)
transport.open()
cli.ping()
ga.gaLoop(cli, 5000)
transport.close()
