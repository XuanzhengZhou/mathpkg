---
role: proof
locale: en
of_concept: completeness-equivalent-conditions
source_book: gtm048
source_chapter: "0"
source_section: "0.0.6"
---

The equivalence is established as follows (cf. Bishop--Goldberg 5.13).

\textbf{(1) $\Rightarrow$ (2):} Suppose $U_x = M_x$ for all $x \in M$. Let $\gamma: E \to M$ be any geodesic. By definition of the exponential map, for each endpoint of $E$, the condition $U_x = M_x$ guarantees that the exponential map is globally defined, so $\gamma$ can be extended to a maximal geodesic. Since the domain of a maximal geodesic must be open (by local existence and uniqueness of geodesics), and the exponential map being globally defined allows extension beyond any finite endpoint, the maximal domain of $\gamma$ must be all of $\mathbb{R}$.

\textbf{(2) $\Rightarrow$ (1):} Suppose every geodesic can be extended to $\mathbb{R}$. Fix $x \in M$ and take any $X \in M_x$. By the fundamental theorem of geodesics, there exists a unique geodesic $\gamma$ defined on a maximal interval containing $0$ such that $\gamma 0 = x$ and $\gamma_* 0 = X$. By hypothesis, $\gamma$ extends to $\mathbb{R}$, so in particular $[0, 1]$ is contained in its domain. Hence by definition of $U_x$, we have $X \in U_x$. Since $X$ was arbitrary, $U_x = M_x$. Since $x$ was arbitrary, $(M, g)$ is complete.
