---
role: proof
locale: en
of_concept: relative-approximation-theorem
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 2.5 — Relative Approximation Theorem

**Theorem 2.5.** Let $U \subset \mathbb{R}^m$ and $V \subset \mathbb{R}^n$ be open subsets, and $f: U \to V$ a $C^r$ map. Let $K \subset U$ be closed and $W \subset U$ open, such that $f$ is $C^s$ on a neighborhood of $K - W$. Then every neighborhood $\mathcal{N}$ of $f$ in $C^r_S(U,V)$ contains a $C^r$ map $h: U \to V$ which is $C^s$ in a neighborhood of $K$, and which equals $f$ on $U - W$.

*Proof.* We may assume $V = \mathbb{R}^n$ (see proof of Theorem 2.4). Let $A \subset U$ be an open set containing the closed set $K - W$ such that $f|A$ is $C^s$. Let $W_0 \subset U$ be open, with

$$K - A \subset W_0 \subset \overline{W}_0 \subset W.$$

Let $\{\lambda_0, \lambda_1\}$ be a $C^\infty$ partition of unity for the open cover $\{W, U - \overline{W}_0\}$ of $U$. Thus $\lambda_0$ and $\lambda_1$ are $C^\infty$ maps $U \to [0,1]$ such that $\lambda_0 + \lambda_1 = 1$, $\lambda_0 = 0$ on a neighborhood of $U - W$ and $\lambda_1 = 0$ on a neighborhood of $\overline{W}_0$.

Define

$$G: C^r_S(U, \mathbb{R}^n) \to C^r_S(U, \mathbb{R}^n)$$

by

$$G(g)(x) = \lambda_0(x) g(x) + \lambda_1(x) f(x).$$

Then $G(g) = g$ in $W_0$ and $G(g) = f$ in $U - W$. Clearly $G(g)$ is $C^r$ on every open set on which both $f$ and $g$ are $C^r$. It is easy to prove $G$ continuous. Since $G(f) = f$, there is an open set $\mathcal{N}_0 \subset C^r_S(U, \mathbb{R}^n)$ containing $f$ such that

$$G(\mathcal{N}_0) \subset \mathcal{N}.$$

By Theorem 2.4 there is a $C^s$ map $g \in \mathcal{N}_0$. Then $h = G(g)$ has the required properties.

QED
