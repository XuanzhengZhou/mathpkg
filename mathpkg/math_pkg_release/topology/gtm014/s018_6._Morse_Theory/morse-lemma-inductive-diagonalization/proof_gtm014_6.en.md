---
role: proof
locale: en
of_concept: morse-lemma-inductive-diagonalization
source_book: gtm014
source_chapter: "6"
source_section: "6. Morse Theory"
---

The Lemma is proved by induction on $r$, where $0 \leq r \leq n$. The induction hypothesis for each $r$ is that there exist smooth functions $h_i: V_r \to \mathbb{R}$ ($1 \leq i \leq r-1$) and a smooth function $s$ on $V_r$ such that:

\begin{itemize}
  \item[(a')] $h_i(0) = 0$ and $\frac{\partial h_i}{\partial x_j}(0) = \pm \delta_{ij}$ for $1 \leq i \leq r-1$, $1 \leq j \leq n$;
  \item[(b')] $s(0) = 0$ and $ds_0 = 0$;
  \item[(c')] $s(x) = \sum_{i,j=r}^{n} v_{ij}(x) u_i(x) u_j(x)$ where $v_{ij} = v_{ji}$ and $v_{rr}(0) \neq 0$;
  \item[(d')] $f(x) = f(0) + (\pm h_1^2(x) \pm \cdots \pm h_{r-1}^2(x)) + s(x)$.
\end{itemize}

For the base case $r = 0$, this holds vacuously with $s = f - f(0)$ via Lemma 6.11 (since $f$ has a critical point at $0$, the first-order coefficients vanish, and the nondegeneracy gives $v_{11}(0) \neq 0$).

For the inductive step from $r$ to $r+1$: From the induction hypothesis,
$$f(x) = f(0) + (\pm h_1^2(x) \pm \cdots \pm h_{r-1}^2(x)) + s(x)$$
where $s(x) = \sum_{i,j=r}^{n} v_{ij}(x) u_i(x) u_j(x)$. Set
$$\delta = \operatorname{sgn}(v_{rr}(0)) = \pm 1,$$
$$h_r = \sqrt{|v_{rr}|} \left(u_r + \sum_{j=r+1}^{n} \frac{v_{rj}}{v_{rr}} u_j\right),$$
and let $g_{ij} = v_{ij} - \frac{v_{ri} v_{rj}}{v_{rr}}$ for $r+1 \leq i, j \leq n$.

Computing $\delta h_r^2$:
$$\delta h_r^2 = v_{rr} u_r^2 + 2 \sum_{j=r+1}^{n} v_{rj} u_r u_j + \sum_{i,j=r+1}^{n} \frac{v_{ri} v_{rj}}{v_{rr}} u_i u_j.$$

And
$$\sum_{i,j=r+1}^{n} g_{ij} u_i u_j = s - \delta h_r^2.$$

Thus
$$f(x) = f(0) + (\pm h_1^2(x) \pm \cdots \pm h_{r-1}^2(x)) + \delta h_r^2(x) + \sum_{i,j=r+1}^{n} g_{ij}(x) u_i(x) u_j(x),$$
which establishes the induction hypothesis for $r+1$. The induction completes at $r = n$, yielding the desired representation.
