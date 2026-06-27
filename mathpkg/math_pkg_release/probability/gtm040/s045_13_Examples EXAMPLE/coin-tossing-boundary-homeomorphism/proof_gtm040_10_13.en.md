---
role: proof
locale: en
of_concept: coin-tossing-boundary-homeomorphism
source_book: gtm040
source_chapter: "10"
source_section: "13"
---

**Step 1: Limit of $j_k/n_k$ exists for Cauchy sequences.** If $(n_k, j_k)$ is Cauchy, consider for $n_k \geq 1$ the expression

$$K((1,0), (n_k, j_k)) = 2 \binom{n_k-1}{j_k} / \binom{n_k}{j_k} = \frac{2(n_k-j_k)}{n_k} = 2 - 2\frac{j_k}{n_k}.$$

As $k \to \infty$, the left side converges; hence $\lim j_k/n_k = t$ exists.

**Step 2: Every sequence with converging ratio is Cauchy.** Conversely, suppose $t = \lim j_k/n_k$ exists. For fixed $(m,i)$,

$$K((m,i), (n,j)) = 2^m \binom{n-m}{j-i} / \binom{n}{j}$$

$$= 2^m \frac{[(j) \cdots (j-i+1)][(n-j) \cdots (n-j-m+i+1)]}{(n) \cdots (n-m+1)}.$$

Both numerator and denominator have exactly $m$ factors. Dividing numerator and denominator by $n^m$ and passing to the limit in each factor separately gives

$$\lim_{k \to \infty} K((m,i), (n_k, j_k)) = 2^m t^i (1-t)^{m-i}.$$

Thus the sequence is Cauchy and the limit function is $K((m,i), t) = 2^m t^i(1-t)^{m-i}$.

**Step 3: No point of $S$ is a limit point, and $B \cong [0,1]$.** Since each function $K((m,i), \cdot)$ is continuous in the unit interval topology, and the map is one-to-one from a compact space onto a Hausdorff space, it is a homeomorphism.

**Step 4: Every boundary point is extreme.** Assume $2^m t_0^i(1-t_0)^{m-i}$ is not minimal. By Theorem 10-41 there is a measure $\nu$ on $B_e \subset [0,1]$ with

$$2^m t_0^i(1-t_0)^{m-i} = \int_{B_e} 2^m t^i(1-t)^{m-i} d\nu(t).$$

Specialize to $m=i$ and extend $\nu$ to $[0,1]$:

$$t_0^i = \int_0^1 t^i d\nu(t)$$

for all $i$. By the Weierstrass Approximation Theorem, a measure on $[0,1]$ is completely determined by its moments. Hence $\nu$ is a point mass at $t_0$, and $t_0$ is extreme. Therefore $B_e = B \cong [0,1]$.
