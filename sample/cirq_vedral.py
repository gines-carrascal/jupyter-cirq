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

print(qubits)

# Create a circuit
circuit = cirq.Circuit()

for i in range(n):
    if sumando_1[i] == "1":
        circuit.append(X(a[n - (i+1)]))
for i in range(n):
    if sumando_2[i] == "1":
        circuit.append(X(b[n - (i+1)]))
        
for i in range(n-1):
    circuit.append(CCX(a[i], b[i], c[i+1]))
    circuit.append(CX(a[i], b[i]))
    circuit.append(CCX(a[i], b[i], c[i+1]))

circuit.append(CCX(a[n-1], b[n-1], b[n]))
circuit.append(CX(a[n-1], b[n-1]))
circuit.append(CCX(a[n-1], b[n-1], b[n]))

circuit.append(CX(c[n-1], b[n-1]))

for i in range(n-1):
    circuit.append(CCX(c[(n-2)-i], b[(n-2)-i], c[(n-1)-i]))
    circuit.append(CX(a[(n-2)-i], b[(n-2)-i]))
    circuit.append(CCX(a[(n-2)-i], b[(n-2)-i], c[(n-1)-i]))
    
    circuit.append(CX(c[(n-2)-i], b[(n-2)-i]))
    circuit.append(CX(a[(n-2)-i], b[(n-2)-i]))

circuit.append(cirq.measure(*b, key='m'))  # Measurement.
print("Circuit:")
print(circuit)


# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)
