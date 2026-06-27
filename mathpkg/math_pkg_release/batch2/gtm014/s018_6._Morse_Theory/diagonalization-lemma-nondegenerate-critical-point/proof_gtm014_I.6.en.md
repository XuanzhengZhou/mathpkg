---
role: proof
locale: en
of_concept: diagonalization-lemma-nondegenerate-critical-point
source_book: gtm014
source_chapter: "I"
source_section: "§6. Morse Theory"
---

The Lemma is proved by induction on $r$. The induction hypothesis for each $r$ with $0 \leq r \leq n$ is that there exist smooth functions $h_i: V_r \to \mathbf{R}$ ($1 \leq i \leq r$) such that $h_i(0) = 0$, $\frac{\partial h_i}{\partial x_j}(0) = \pm \delta_{ij}$, and

$$f(x) = f(0) + (\pm h_1^2(x) \pm \cdots \pm h_{r-1}^2(x)) + s(x)$$

where $s(x) = \sum_{i,j=r}^{n} v_{ij}(x)u_i(x)u_j(x)$ with $u_i(x) = x_i$ for $i \geq r$ and $v_{ij}$ smooth. By the nondegeneracy hypothesis and after a linear change of variables, we may assume $v_{rr}(0) \neq 0$, so $v_{rr}$ is nonzero near $0$.

Define $g_{ij} = v_{ij} - \frac{v_{rj}v_{ri}}{v_{rr}}$ for $r+1 \leq i,j \leq n$. Then one computes:

(i) $$\delta h_r^2 = v_{rr}u_r^2 + 2 \sum_{j=r+1}^{n} v_{rj}u_ru_j + \sum_{i,j=r+1}^{n} \frac{v_{ri}v_{rj}}{v_{rr}}u_iu_j$$

and

(ii) $$\sum_{i,j=r+1}^{n} g_{ij}h_ih_j = \delta h_r^2 + s.$$

Thus we obtain

$$f(x) = f(0) + (\pm h_1^2(x) \pm \cdots \pm h_{r-1}^2(x)) - \delta h_r^2(x) + \sum_{i,j=r+1}^{n} g_{ij}h_i(x)h_j(x).$$

This advances the induction to $r+1$. After $n$ steps, the sum over $i,j$ is vacuous and the desired representation is obtained.
