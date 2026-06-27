---
role: proof
locale: en
of_concept: quantum-fourier-transform-factorization-lemma
source_book: gtm053
source_chapter: "8"
source_section: "8.5"
---
The quantum Fourier transform $\Phi_n^t$ is defined by its action on basis states. The Hadamard gate $U_1^{(k)}$ creates an equal superposition on qubit $k$, while the controlled phase gates $U_2^{(kj)}$ introduce relative phases $\exp(i\pi/2^{j-k})$. The product formula follows from the definition of the QFT as the unitary operator mapping $|a\rangle$ to $\frac{1}{\sqrt{N}}\sum_{c=0}^{N-1} \exp(2\pi iac/N)|c\rangle$, where $N = 2^n$. The bit-reversal order in the product accounts for the fact that QFT reverses bit order. The total gate count is $\sum_{k=0}^{n-1}(1 + (n-1-k)) = O(n^2)$.
