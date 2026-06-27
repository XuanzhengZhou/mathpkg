---
role: proof
locale: en
of_concept: entropy-characterization
source_book: gtm017
source_chapter: "II"
source_section: "f"
---
First, show $L(n) = H(1/n, \dots, 1/n) = \lambda \log n$. By monotonicity and additivity, for integers $r, s$:
$$r^m \leq s^n \leq r^{m+1} \implies mL(r) \leq nL(s) \leq (m+1)L(r).$$
Thus $|L(s)/L(r) - \log s/\log r| \leq 1/n \to 0$, giving $L(n) = \lambda \log n$.

For rational $p_i = g_i/g$, partition an experiment of $g$ equally likely outcomes into groups of size $g_i$. Using additivity:
$$H(p_1, \dots, p_n) = -\lambda \sum p_k \log p_k.$$
Continuity extends this to all real $p_i \geq 0$ with $\sum p_i = 1$.
