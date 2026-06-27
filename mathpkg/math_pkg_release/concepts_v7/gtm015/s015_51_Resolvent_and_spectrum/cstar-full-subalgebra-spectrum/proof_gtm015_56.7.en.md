---
role: proof
locale: en
of_concept: cstar-full-subalgebra-spectrum
source_book: gtm015
source_chapter: "56"
source_section: "56.7"
---

# Proof of C*-algebra full subalgebra preserves spectrum

Proof. Assuming $x \in B$ and $0 \in \sigma_B(x)$, it is to be shown that $0 \in \sigma_A(x)$. Since $x$ is not invertible in $B$, either $x^*x$ or $xx^*$ must fail to be invertible in $B$. Suppose, for example, that $y = x^*x$ is singular in $B$, thus $0 \in \sigma_B(y)$. Since $y^* = y$, we have $\sigma_B(y) \subset \mathbb{R}$ by hypothesis, thus $0$ must be a boundary point of $\sigma_B(y)$; citing (56.5), we have $0 \in \sigma_A(y)$. Thus $x^*x$ is not invertible in $A$; a fortiori, $x$ is not invertible in $A$, that is, $0 \in \sigma_A(x)$. This shows that $B$ is a full subalgebra of $A$, and therefore $\sigma_B(x) = \sigma_A(x)$ for all $x$ in $B$ (53.8). {Concerning the hypothesis on $B$, see (56.12).}
