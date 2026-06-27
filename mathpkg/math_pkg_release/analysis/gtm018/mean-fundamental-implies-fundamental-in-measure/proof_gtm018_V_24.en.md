---
role: proof
locale: en
of_concept: mean-fundamental-implies-fundamental-in-measure
source_book: gtm018
source_chapter: "V"
source_section: "24"
---
**Proof.** For any $\epsilon > 0$, let $E_{nm} = \{x : |f_n(x) - f_m(x)| \geq \epsilon\}$. Then
$$\rho(f_n, f_m) = \int |f_n - f_m| d\mu \geq \int_{E_{nm}} |f_n - f_m| d\mu \geq \epsilon \mu(E_{nm}),$$
so $\mu(E_{nm}) \to 0$ as $n, m \to \infty$."
