---
role: proof
locale: en
of_concept: connected-cycle-is-circuit
source_book: gtm054
source_chapter: "III"
source_section: "A"
---

By IIC1, $Z$ is the sum of pairwise-disjoint elementary cycles. Hence by Proposition A9, $\Gamma_Z$ contains a circuit. If $\Gamma_Z$ is not itself a circuit, let $\Delta$ be a largest circuit in $\Gamma_Z$. The set $Z''$ of the edges of $\Delta$ is a cycle by A9. Clearly $Z'' \subset Z$, and $Z''$ is disjoint from the cycle $Z' = Z + Z''$. Let $\Delta' = \Gamma_{Z'}$. If $\Delta$ and $\Delta'$ have no common vertex, then $\Gamma_Z = \Delta \oplus \Delta'$, which contradicts the hypothesis that $\Gamma_Z$ is connected. Thus there exists a vertex $x$ common to $\Delta$ and $\Delta'$. By IIC1, $Z' = Z_1' + \cdots + Z_k'$ where each cycle $Z_i'$ is elementary. Let $\Delta_i' = \Gamma_{Z_i'}$. [The proof continues by showing that the existence of a common vertex allows constructing a larger circuit, contradicting the maximality of $\Delta$. Hence $\Gamma_Z$ must be a circuit.]
