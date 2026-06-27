---
role: proof
locale: en
of_concept: mapping-cylinder-collapse-to-subcomplex
source_book: gtm010
source_chapter: "5"
source_section: "5"
---

Let $K = K_0 \cup e_1 \cup \dots \cup e_r$ where the $e_i$ are the cells of $K - K_0$ arranged in order of increasing dimension. Then $K_i = K_0 \cup e_1 \cup \dots \cup e_i$ is a subcomplex of $K$. Set $M_i = M_{f|K_i}$ and claim that $M_i \searrow M_{i-1}$ for all $i$.

Let $\varphi_i$ be a characteristic map for $e_i$. Then $K \cup M_{f|K_{i+1}} = K \cup M_{f|K_i} \cup [e^{n-1} \times (0,1) \cup e^n \times (0,1)]$. Letting $q$ be the quotient map, $q \circ (\varphi \times 1): (I^n \times I, I^{n-1} \times I) \to K \cup M_{f|K_{i+1}}$ gives characteristic maps for these cells and meets the specifications for an elementary collapse. Hence $K \cup M_{f|K_{i+1}} \searrow K \cup M_{f|K_i}$. The result follows by induction.
