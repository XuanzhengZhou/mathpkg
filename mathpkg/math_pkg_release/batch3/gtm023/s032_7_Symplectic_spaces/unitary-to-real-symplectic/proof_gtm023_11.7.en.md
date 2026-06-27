---
role: proof
locale: en
of_concept: unitary-to-real-symplectic
source_book: gtm023
source_chapter: "11"
source_section: "7"
---

The proof is left as an exercise in the source text. The argument proceeds as follows:

Let $(\cdot, \cdot)$ denote the Hermitian inner product on the unitary space $E$. For $x, y \in E_{\mathbb{R}}$ (the underlying real vector space), define
$$(x, y)_{\mathbb{R}} = \operatorname{Re}(x, y), \quad \langle x, y \rangle = \operatorname{Im}(x, y).$$

**Symmetry and positive definiteness:** Since the Hermitian inner product satisfies $(x, y) = \overline{(y, x)}$, taking real parts gives $(x, y)_{\mathbb{R}} = (y, x)_{\mathbb{R}}$, so the real part is symmetric. Positive definiteness follows from $(x, x)_{\mathbb{R}} = \operatorname{Re}(x, x) = (x, x) > 0$ for $x \neq 0$.

**Skew-symmetry:** $\langle x, y \rangle = \operatorname{Im}(x, y) = \operatorname{Im}(\overline{(y, x)}) = -\operatorname{Im}(y, x) = -\langle y, x \rangle$.

**Non-degeneracy:** If $\langle x, y \rangle = 0$ for all $y$, then $\operatorname{Im}(x, y) = 0$ for all $y$. Since the Hermitian form is non-degenerate and $\operatorname{Re}(x, y) = \operatorname{Im}(-ix, y)$, setting $y = -ix$ yields $(x, -ix) = i(x, x)$, whose imaginary part is $(x, x) \neq 0$ for $x \neq 0$, contradiction.

**Relations:** For the first relation,
$$\langle x, y \rangle = \operatorname{Im}(x, y) = \operatorname{Re}(-i(x, y)) = \operatorname{Re}((-ix, y)) = -(-ix, y)_{\mathbb{R}} = -(ix, y)_{\mathbb{R}}.$$

For the second,
$$\langle ix, y \rangle = \operatorname{Im}(ix, y) = \operatorname{Re}(-i(ix, y)) = \operatorname{Re}((x, y)) = (x, y)_{\mathbb{R}}.$$

**Conclusion:** From $\langle ix, y \rangle = (x, y)_{\mathbb{R}}$, we obtain $\langle ix, iy \rangle = (x, iy)_{\mathbb{R}} = \operatorname{Re}(x, iy)$. Using $(x, iy) = -i(x, y)$ and taking real parts: $\langle ix, iy \rangle = \operatorname{Im}(x, y) = \langle x, y \rangle$, so $x \mapsto ix$ is symplectic. The relation $\langle ix, y \rangle = (x, y)_{\mathbb{R}}$ together with $(x, y)_{\mathbb{R}} = \langle x, -iy \rangle$ shows that the transformation is also skew-symplectic.
