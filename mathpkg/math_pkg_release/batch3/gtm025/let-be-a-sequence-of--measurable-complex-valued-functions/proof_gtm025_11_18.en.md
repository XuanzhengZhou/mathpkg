---
role: proof
locale: en
of_concept: "let-be-a-sequence-of--measurable-complex-valued-functions"
source_book: gtm025
source_chapter: "Measurable Functions"
source_section: "11.18"
---

Apply (11.15) and (11.14).

(11.19) Remark. Theorems (11.18) and (11.14) both require that the sequence in question converge for every $x \in X$. However, a large portion of our work will deal with the case in which there is some specific measure $\mu$ defined on $\mathcal{A}$, the functions in question are defined only $\mu$-almost everywhere, and the convergence of sequences is only $\mu$-a.e. Thus we would like a corresponding theorem for this case. Such a theorem will require some additional hypothesis about $\mu$, for consider the case that $X = R$, $\mathcal{A} = \mathcal{B}(R)$, $\mu = \lambda$, $P = \text{CANTOR's ternary set}$, $A \subset P$, $A \notin \mathcal{B}(R)$, $f = \xi_A$, and $f_n = 0$ for all $n \in N$. Then each $f_n$ is $\mathcal{B}(R)$-measurable and $f$ is not $\mathcal{B}(R)$-measurable, but $f_n(x) \rightarrow f(x)$ for all $x \in R \cap P'$, i.e., $f_n \rightarrow f \lambda$-a.e. To avoid such irritating situations, it is enough to consider complete measures, defined as follows.
