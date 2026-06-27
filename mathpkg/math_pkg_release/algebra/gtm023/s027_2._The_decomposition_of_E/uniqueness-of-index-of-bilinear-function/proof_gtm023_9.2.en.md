---
role: proof
locale: en
of_concept: uniqueness-of-index-of-bilinear-function
source_book: gtm023
source_chapter: "9"
source_section: "2. The decomposition of E"
---

Consider two decompositions
$$E = E_1^+ \oplus E_1^- \oplus E_0, \quad E = E_2^+ \oplus E_2^- \oplus E_0$$
with $\Phi$ positive definite on $E_1^+, E_2^+$ and negative definite on $E_1^-, E_2^-$.

Since $\Phi$ is positive definite on $E_2^+$ and negative semidefinite on $E_1^- \oplus E_0$, the intersection $E_2^+ \cap (E_1^- \oplus E_0)$ must be $\{0\}$ (a nonzero vector in the intersection would satisfy both $\Phi(x) > 0$ and $\Phi(x) \leq 0$, contradiction). Hence

$$E_2^+ \cap (E_1^- \oplus E_0) = 0,$$

which implies
$$\dim E_2^+ + \dim E_1^- + \dim E_0 \leq n. \tag{1}$$

From the first decomposition,
$$\dim E_1^+ + \dim E_1^- + \dim E_0 = n. \tag{2}$$

Comparing (1) and (2) yields $\dim E_2^+ \leq \dim E_1^+$. Interchanging the roles of $E_1^+$ and $E_2^+$ gives $\dim E_1^+ \leq \dim E_2^+$. Therefore $\dim E_1^+ = \dim E_2^+$.
