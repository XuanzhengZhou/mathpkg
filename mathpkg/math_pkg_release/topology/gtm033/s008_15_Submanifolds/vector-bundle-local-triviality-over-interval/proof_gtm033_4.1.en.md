---
role: proof
locale: en
of_concept: vector-bundle-local-triviality-over-interval
source_book: gtm033
source_chapter: "4"
source_section: "4.1"
---

# Proof of Local Triviality of Vector Bundles over Product with Interval

**Lemma 1.1.** Let $\xi = (p, E, B \times I)$ be a $C^r$ vector bundle, $0 \leqslant r \leqslant \infty$. Then each $b \in B$ has a neighborhood $V \subset B$ such that $\xi|V \times I$ is trivial.

*Proof.* By compactness of $I$ and local triviality of $\xi$ we can find a neighborhood $V_i \subset B$ of $b$ and a subdivision of $I$ into intervals $I_i = [t_{i-1}, t_i]$, $0 = t_0 < \cdots < t_m = 1$ such that $\xi$ is trivial over a neighborhood of $V_i \times [t_{i-1}, t_i]$, $i = 1, \ldots, m$. Put $V = \bigcap V_i$; then $I_i$ has a neighborhood $U_i \subset I$ such that $\xi|V \times U_i$ is trivial.

We proceed by induction on $m$; if $m = 1$ there is nothing more to prove. Therefore we shall show that if $m > 1$, there is a neighborhood $J \subset I$ of $[0, t_2]$ such that $\xi|V \times J$ is trivial. Continuing in this way will eventually show that $\xi|V \times I$ is trivial. Hence it suffices to assume that $m = 2$.

Let $U_1 = [0, b]$, $U_2 = [a, 1]$, $0 < a < b < 1$. Choose trivializations

$$\varphi_1: \xi|V \times U_1 \to (V \times U_1) \times \mathbb{R}^n,$$
$$\varphi_2: \xi|V \times U_2 \to (V \times U_2) \times \mathbb{R}^n.$$

Over the overlap $V \times (a, b)$, the transition function

$$g: V \times (a,b) \to GL(n)$$

is given by $g(x,t) = (\varphi_2)_x \circ (\varphi_1)_x^{-1}$. Since $GL(n)$ is path-connected, we can deform $g$ to extend the trivialization from $V \times U_1$ to $V \times (U_1 \cup U_2) = V \times J$, where $J = [0,1]$. This completes the induction step and hence the proof. $\square$
