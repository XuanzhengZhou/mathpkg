---
role: proof
locale: en
of_concept: "riemann-stieltjes-integrals-are-the-only-nonnegative-linear-functionals"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.50"
---

Let $I$ be any nonnegative linear functional on $\mathfrak{C}_{00}(R)$ and let $\iota$ be the measure constructed from $I$ as in §§ 9 and 10. Use (19.48) to find an $\alpha$ such that $\iota = \lambda_\alpha$ on $\mathcal{B}(R)$. Finally infer from Riesz's representation theorem (12.36) that

$$I(f) = \int_R f \, d\iota = \int_R f \, d\lambda_\alpha = S_\alpha(f)$$

for all $f \in \mathfrak{C}_{00}(R)$. $\square^1$

(19.51) Notation. To simplify our statements, we will write

$$\

Proof. Suppose first that $\alpha$ is absolutely continuous on $[-p, p]$ for all $p \in N$. Let $A$ be any subset of $R$ such that $\lambda(A) = 0$, and let $\varepsilon$ be a positive number. For every $p \in N$, there exists $\delta(p) > 0$ such that $\sum_{k=1}^{n} (\alpha(b_k) - \alpha(a_k)) < \varepsilon$ whenever $\{]a_k, b_k[\}_{k=1}^{n}$ is a pairwise disjoint family of intervals such that $\bigcup_{k=1}^{n} a_k, b_k[\subset [-p, p]$ and $\sum_{k=1}^{n} (b_k - a_k) < \delta(p)$. Since $\lambda(A \cap [-p, p]) = 0$, there are pairwise disjoint intervals $\{]a_k, b_k[\}_{k=1}^{n}$ such that $A \cap [-p, p] \subset \bigcup_{k=1}^{n} a_k, b_k[\subset [-p, p]$ and $\sum_{k=1}^{n} (b_k - a_k) < \delta(p)$. By the choice of $\delta(p)$, we have

$$\sum_{k=1}^{\infty} (\alpha(b_k) - \alpha(a_k)) \leq \varepsilon.$$

In view of (19.47) and the continuity of $\alpha$, we also have $\alpha(b_k) - \alpha(a_k) = \iota([a_k, b_k])$ for all $k \in N$, and so

$$\varepsilon \geq \sum_{k=1}^{\infty} (\alpha(b_k) - \alpha(a_k)) = \sum_{k=1}^{\infty} \iota([a_k, b_k] = \iota(\bigcup_{k=1}^{n} a_k, b_k)),$$

which implies that $\iota(A \cap [-p, p]) \leq \varepsilon$. As $\varepsilon$ is arbitrary, the equalities

$$\iota(A) = \lim_{p \to \infty} \iota(A \cap [-p, p]) = 0$$

follow.

Next suppose that $\

We close this section by obtaining a classical decomposition of measures $\iota$, and with it a corresponding decomposition for functions $\alpha$. We begin by "skimming off" the discontinuous part of $\iota$.
