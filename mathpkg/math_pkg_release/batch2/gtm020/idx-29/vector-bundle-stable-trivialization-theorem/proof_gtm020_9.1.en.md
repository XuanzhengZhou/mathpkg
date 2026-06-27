---
role: proof
locale: en
of_concept: vector-bundle-stable-trivialization-theorem
source_book: gtm020
source_chapter: "9"
source_section: "1"
---

Proceed by induction on $k \geq m$. The base case $k = m$ is trivial.

Assume $k > m$ and the statement holds for all bundles of dimension less than $k$. Since $m = \langle (n+1)/c - 1 \rangle$, we have $m \geq (n+1)/c - 1$, which rearranges to $n \leq c(m+1) - 1$. Since $k > m$, we have $k \geq m+1$, so $n \leq ck - 1$ also holds.

By Proposition 1.1, $\xi^k \cong \eta' \oplus \theta^1$ for some $(k-1)$-dimensional bundle $\eta'$. By the induction hypothesis applied to $\eta'$, we have $\eta' \cong \eta^m \oplus \theta^{(k-1)-m}$. Therefore:
$$\xi^k \cong \eta' \oplus \theta^1 \cong (\eta^m \oplus \theta^{k-1-m}) \oplus \theta^1 \cong \eta^m \oplus \theta^{k-m}.$$

The inequality $n \leq c(m+1)-1$ also yields $[(n+1)/c] - 1 \leq m$, confirming that $m$ as defined is the minimum dimension achievable by this process.

Special cases:
- $c=1$ (real): $m = \langle n+1-1 \rangle = n$, so $\xi^k \cong \eta^n \oplus \theta^{k-n}$.
- $c=2$ (complex): $m \approx n/2$.
- $c=4$ (quaternionic): $m \approx n/4$.
