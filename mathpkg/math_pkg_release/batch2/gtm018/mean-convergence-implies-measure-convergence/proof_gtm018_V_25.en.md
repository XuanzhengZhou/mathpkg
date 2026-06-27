---
role: proof
locale: en
of_concept: mean-convergence-implies-measure-convergence
source_book: gtm018
source_chapter: "V"
source_section: "25"
---
**Proof.** For any $\epsilon > 0$, let $E_n = \{x : |f_n(x) - f(x)| \geq \epsilon\}$. Then
$$\int |f_n - f| d\mu \geq \int_{E_n} |f_n - f| d\mu \geq \epsilon \mu(E_n),$$
so $\mu(E_n) \to 0$ as $n \to \infty$.
