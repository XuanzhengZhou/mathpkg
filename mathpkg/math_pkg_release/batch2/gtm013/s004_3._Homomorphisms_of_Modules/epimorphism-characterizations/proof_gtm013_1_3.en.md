---
role: proof
locale: en
of_concept: epimorphism-characterizations
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof.** The implication (d) $\Rightarrow$ (b) is the only one that offers any challenge. Let $K = \text{Ker}\, f$. Then the inclusion $i_K: K \to M$ is an $R$-homomorphism and $f i_K = 0$. So assuming (d) we have $i_K = 0$. But then $K = \text{Im}\, i_K = 0$, whence $\text{Im}\, f = N$ (since $f$ is epic iff $\text{Ker}\, f = 0$...). The remaining equivalences are straightforward:
- (a) $\Leftrightarrow$ (b) is the definition.
- (b) $\Rightarrow$ (c): If $gf = hf$, then for any $y \in N = \text{Im}\, f$, write $y = f(x)$ and get $g(y) = h(y)$, so $g = h$.
- (c) $\Rightarrow$ (d): Take $h = 0$; then $gf = 0 = 0 \cdot f$ implies $g = 0$.
- (b) $\Rightarrow$ (d): If $gf = 0$, then $g$ vanishes on $\text{Im}\, f = N$, so $g = 0$. $\square$
