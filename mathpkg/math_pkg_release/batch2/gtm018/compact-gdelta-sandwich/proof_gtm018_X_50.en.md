---
role: proof
locale: en
of_concept: compact-gdelta-sandwich
source_book: gtm018
source_chapter: "X"
source_section: "50"
---

Since there exists a bounded open set $V$ with $C \subset V \subset U$, there is no loss of generality in assuming $U$ is bounded. Let $f$ be a function in $\mathfrak{F}$ such that $f(x) = 0$ for $x$ in $C$ and $f(x) = 1$ for $x$ in $X - U$. Write $U_0 = \{x: f(x) < \frac{1}{2}\}$ and $C_0 = \{x: f(x) \leq \frac{1}{2}\}$. Clearly $C \subset U_0 \subset C_0 \subset U$ and $C_0$ is a closed $G_{\delta}$; it is compact by boundedness of $U$; $U_0$ is $\sigma$-compact since $U_0 = \bigcup_{n=1}^{\infty} \{x: f(x) \leq \frac{1}{2} - \frac{1}{2^n}\}$.
