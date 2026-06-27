---
role: proof
locale: en
of_concept: characterization-of-circuit-chains
source_book: gtm040
source_chapter: "9"
source_section: "10"
---

If $P$ represents a circuit, then it has a regular measure $\alpha$ and is $\alpha$-reversible by Proposition 9-127. Its states communicate since the circuit is connected.

Conversely, suppose $P$ is a transition matrix with the stated properties. Introduce the electric circuit with the states of $P$ as terminals and with $c_{ij} = \alpha_i P_{ij}$. The circuit is well defined since $c_{ii} = \alpha_i P_{ii} = 0$ and $c_{ij} = \alpha_i P_{ij} = \alpha_j P_{ji} = c_{ji}$. Since the states communicate, the circuit is connected. To see that $P$ represents the circuit, note that $\alpha_i = \sum_k c_{ik}$, so $P_{ij} = c_{ij} / \sum_k c_{ik}$, and the argument of Proposition 9-125 shows $P$ represents the circuit.
