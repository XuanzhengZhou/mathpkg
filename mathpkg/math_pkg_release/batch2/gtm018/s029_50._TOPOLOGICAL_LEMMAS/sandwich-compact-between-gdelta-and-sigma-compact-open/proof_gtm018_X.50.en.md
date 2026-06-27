---
role: proof
locale: en
of_concept: sandwich-compact-between-gdelta-and-sigma-compact-open
source_book: gtm018
source_chapter: "X"
source_section: "50"
---

Since there exists a bounded open set $V$ such that $C \subset V \subset U$, there is no loss of generality in assuming that $U$ is bounded. Let $f$ be a function in $\mathfrak{F}$ such that $f(x) = 0$ for $x$ in $C$ and $f(x) = 1$ for $x$ in $X - U$ (Theorem B). Define

$$U_0 = \{x : f(x) < \tfrac{1}{2}\}, \qquad C_0 = \{x : f(x) \leq \tfrac{1}{2}\}.$$

Clearly $C \subset U_0 \subset C_0 \subset U$. By Theorem C, $C_0$ is a closed $G_\delta$. The fact that $C_0$ is compact follows from the boundedness of $U$. The fact that $U_0$ is $\sigma$-compact follows from the representation

$$U_0 = \bigcup_{n=1}^{\infty} \{x : f(x) \leq \tfrac{1}{2} - \tfrac{1}{2^n}\},$$

where each set $\{x : f(x) \leq \frac{1}{2} - \frac{1}{2^n}\}$ is a closed subset of the compact set $C_0$, hence compact.
