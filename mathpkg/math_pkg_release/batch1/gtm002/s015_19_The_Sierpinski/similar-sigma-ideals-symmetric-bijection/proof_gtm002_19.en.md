---
role: proof
locale: en
of_concept: similar-sigma-ideals-symmetric-bijection
source_book: gtm002
source_chapter: "19"
source_section: "The Sierpinski-Erdos Duality Theorem"
---

Let $X_{\alpha}$ $(0 \leq \alpha < \Omega)$ be a decomposition of $X$ corresponding to $K$, as constructed in the proof of Theorem 19.5. We may assume that a prescribed member $M \in K$ belongs to the generating class $G$, and that $G_0$ is taken equal to $M$. Then $X_0 = M$, because $M$ cannot be countable. Similarly, let $Y_{\alpha}$ $(0 \leq \alpha < \Omega)$ be a decomposition of $X$ corresponding to $L$, with $Y_0 = N$ for a prescribed $N \in L$. Then

$$M = \bigcup_{0 < \alpha < \Omega} Y_{\alpha} \quad \text{and} \quad N = \bigcup_{0 < \alpha < \Omega} X_{\alpha}.$$

The sets $X_{\alpha}$ and $Y_{\alpha}$, for $0 < \alpha < \Omega$, constitute a decomposition of $X$ into sets of power $\aleph_1$. For each $0 < \alpha < \Omega$, let $f_{\alpha}$ be a one-to-one mapping of $X_{\alpha}$ onto $Y_{\alpha}$. Define $f$ equal to $f_{\alpha}$ on $X_{\alpha}$, and equal to $f_{\alpha}^{-1}$ on $Y_{\alpha}$, for $0 < \alpha < \Omega$. Then $f$ is a one-to-one mapping of $X$ onto itself, $f$ is equal to $f^{-1}$, and $f(X_{\alpha}) = Y_{\alpha}$ for all $0 < \alpha < \Omega$. Since

$$X_0 = \bigcup_{0 < \alpha < \Omega} Y_{\alpha} \quad \text{and} \quad Y_0 = \bigcup_{0 < \alpha < \Omega} X_{\alpha},$$

we have also $f(X_0) = Y_0$. Thus $f(X_{\alpha}) = Y_{\alpha}$ for all $0 \leq \alpha < \Omega$. From the properties of $X_{\alpha}$ and $Y_{\alpha}$ stated in Theorem 19.5 it follows that $f(E) \in L$ if and only if $E \in K$.
