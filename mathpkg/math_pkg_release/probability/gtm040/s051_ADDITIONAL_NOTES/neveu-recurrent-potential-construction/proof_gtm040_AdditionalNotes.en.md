---
role: proof
locale: en
of_concept: neveu-recurrent-potential-construction
source_book: gtm040
source_chapter: "Additional Notes"
source_section: "Optimal stopping problems"
---

The construction proceeds as follows. Since $P$ is recurrent with positive regular measure $\alpha$, the operator $U_0 = P + P^2 + \cdots$ diverges, but Neveu shows there exists $h$ with $0 < h \leq 1$ such that $U_h$ is well-defined and satisfies $U_h h = 1$ and $U_h \geq 1\alpha$. Define $V = U_h - 1\alpha \geq 0$. Then $W = \sum_{n=0}^{\infty} (V D_h)^n V$ is a Neumann series. To verify finiteness, note that $V D_h$ is a contraction-like operator and the identities $W h = c 1$ and $\alpha D_h W = c \alpha$ hold by straightforward computation, where $c = (1 - \alpha h)/(\alpha h)$.
