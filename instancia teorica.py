from dwave.system import DWaveSampler
import dwave.system
#from dwave.system import Client
import dimod
import time
import hybrid

api="DEV-e689f2c3ebf1c9ded5c1eb78e31859c7fc31f054"
dw=DWaveSampler(token=api)

qubits = dw.nodelist
couplers = dw.edgelist
nodes = {}
edges = {}
for i in qubits:
    nodes[i]=-1

for i in couplers:
    edges[i]=2

bqm = dimod.BinaryQuadraticModel(nodes, edges, 0.0, 'BINARY')

initial_state = hybrid.State.from_problem(bqm)


resultados={}
tiempos={}