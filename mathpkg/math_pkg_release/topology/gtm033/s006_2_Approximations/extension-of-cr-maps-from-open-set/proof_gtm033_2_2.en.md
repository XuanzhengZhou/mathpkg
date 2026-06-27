---
role: proof
locale: en
of_concept: extension-of-cr-maps-from-open-set
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Lemma 2.8 (Extension of $C^r$ maps from an open set)

Let $U$ be a $C^r$ manifold, $0 \leqslant r < \infty$, and $W \subset U$ an open set. Let $V \subset \mathbb{R}^n$ be open, $f \in C^r_S(U,V)$, and put $f(W) = V'$. We construct a neighborhood $\mathcal{N} \subset C^r(W,V')$ of $f|W$ and a continuous map $T: \mathcal{N} \to C^r_S(U,V)$ such that for $g_0 \in \mathcal{N}$, the map

$$T(g_0) = g: U \to V, \qquad
g = \begin{cases} g_0 & \text{on } W \\ f & \text{on } U - W \end{cases}$$

is $C^r$.

Let $\{\varphi_i, U_i\}_{i \in \Lambda}$ be a locally finite family of charts of $U$ which cover the boundary $\operatorname{Bd} W$ of $W$. Let $\{L_i\}_{i \in \Lambda}$ be a family of closed subsets of $U_i$ such that $\bigcup_i L_i$ is a neighborhood of $\operatorname{Bd} W$.

We claim $g$ is $C^r$. It suffices to prove that each map $\lambda_i = (g - f)\varphi_i^{-1} : \varphi_i(U_i) \to \mathbb{R}^n$ is $C^r$. Now

$$\lambda_i = \begin{cases} g_0\varphi_i^{-1} - f\varphi_i^{-1} & \text{on } \varphi_i(W) \\ 0 & \text{on } \varphi_i(U_i - W). \end{cases}$$

Obviously $\lambda_i$ is $C^r$ on $\varphi_i(W)$. By construction of the neighborhood $\mathcal{N}$ (using condition (7)), for $0 \leqslant k \leqslant r$:

$$D^k\lambda_i(y) \mapsto 0 \quad \text{as} \quad d(y,\varphi_i(U_i - W)) \to 0,$$

uniformly in $y \in \varphi_i(W)$. It follows that $\lambda_i$ is $C^r$, with all derivatives $0$ on $\varphi_i(U_i - W)$. Therefore $g$ is $C^r$ and the map $T: C^r(W,V') \to C^r(U,V)$ is well-defined. The continuity of $T$ is left as an exercise.

QED
