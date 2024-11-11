import numpy as np
from qiskit import QuantumCircuit

qc= QuantumCircuit(3)

qc.h(0)
qc.p(np.pi/2,0)
qc.cx(0,1)
qc.cx(0,2)
measure=qc.measure_all(inplace=False)
from qiskit.primitives import StatevectorSampler
sampler= StatevectorSampler()
job = sampler.run([measure],shots=1000)
result = job.result()
print(f" {result._pub_results}")