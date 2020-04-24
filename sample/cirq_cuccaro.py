import cirq
from cirq.ops import CCX, CX, H, X 

def bitstring(bits):
    return ''.join(str(int(b)) for b in bits)

sumando_1 = input("Primer sumando en binario (4 bits)")
sumando_2 = input("Segundo sumando en binario(4 bits)")

n = 4

a = [cirq.GridQubit(0, i) for i in range(n)]
b = [cirq.GridQubit(1, i) for i in range(n+1)]
c = [cirq.GridQubit(2, i) for i in range(n)]


# Create a circuit
circuit = cirq.Circuit()

for i in range(n):
    if sumando_1[i] == "1":
        circuit.append(X(a[n - (i+1)]))
for i in range(n):
    if sumando_2[i] == "1":
        circuit.append(X(b[n - (i+1)]))

for i in range(1, n):
    circuit.append(CX(a[i], b[i]))

circuit.append(CX(a[1], c[0]))

circuit.append(CCX(a[0], b[0], c[0]))
circuit.append(CX(a[2], a[1]))

circuit.append(CCX(c[0], b[1], a[1]))
circuit.append(CX(a[3], a[2]))

for i in range(2, n-2):
    circuit.append(CCX(a[i-1], b[i], a[i]))
    circuit.append(CX(a[i+2], a[i+1]))

circuit.append(CCX(a[n-3], b[n-2], a[n-2]))
circuit.append(CX(a[n-1], b[n]))

circuit.append(CCX(a[n-2], b[n-1], b[n]))
for i in range(1, n-1):
    circuit.append(X(b[i]))

circuit.append(CX(c[0], b[1]))
for i in range(2, n):
    circuit.append(CX(a[i-1], b[i]))

circuit.append(CCX(a[n-3], b[n-2], a[n-2]))

for i in range(n-3,1,-1):
    circuit.append(CCX(a[i-1], b[i], a[i]))
    circuit.append(CX(a[i+2], a[i+1]))
    circuit.append(X(b[i+1]))

circuit.append(CCX(c[0], b[1], a[1]))
circuit.append(CX(a[3], a[2]))
circuit.append(X(b[2]))

circuit.append(CCX(a[0], b[0], c[0]))
circuit.append(CX(a[2], a[1]))
circuit.append(X(b[1]))

circuit.append(CX(a[1], c[0]))

for i in range(n):
    circuit.append(CX(a[i], b[i]))       

circuit.append(cirq.measure(*b, key='m'))  # Measurement.
print("Circuit:")
print(circuit)


# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)
