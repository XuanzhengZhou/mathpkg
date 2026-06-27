---
role: proof
locale: en
of_concept: operator-norm-is-norm-function
source_book: gtm023
source_chapter: "VII"
source_section: "5 (7.21)"
---

$N_1$: Clearly $\|\varphi\| \geq 0$. If $\varphi = 0$ then $\|\varphi\| = 0$. Conversely, if $\|\varphi\| = 0$ then $\|\varphi x\| \leq \|\varphi\| \cdot \|x\| = 0$ for all $x$, so $\varphi x = 0$ for all $x$, hence $\varphi = 0$.

$N_3$: $\|\lambda \varphi\| = \sup_{\|x\|=1} \|\lambda \varphi x\| = |\lambda| \sup_{\|x\|=1} \|\varphi x\| = |\lambda| \cdot \|\varphi\|$.

$N_2$: For any $x$ with $\|x\| = 1$,
$$\|(\varphi + \psi)x\| = \|\varphi x + \psi x\| \leq \|\varphi x\| + \|\psi x\| \leq \|\varphi\| + \|\psi\|.$$
Taking the supremum over all such $x$ yields $\|\varphi + \psi\| \leq \|\varphi\| + \|\psi\|$.
