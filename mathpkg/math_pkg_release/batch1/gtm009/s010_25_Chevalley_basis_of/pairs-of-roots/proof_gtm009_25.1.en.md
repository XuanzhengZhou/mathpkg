---
role: proof
locale: en
of_concept: pairs-of-roots
source_book: gtm009
source_chapter: "VII"
source_section: "25.1"
---

**Proof.** (a) This was proved in (9.4) (as well as in Proposition 8.4(e), via the representation theory of $\mathfrak{sl}(2, F)$).

(b) $\Phi' = (\mathbb{Z}\alpha + \mathbb{Z}\beta) \cap \Phi$ is a root system of rank 2 (in the subspace of $E$ spanned by $\alpha, \beta$); cf. Exercise 9.7. If reducible, it must be of type $A_1 \times A_1$, where all roots have the same length. Otherwise, $\Phi'$ is irreducible of type $A_2$, $B_2$, or $G_2$, where the string in question involves at most two root lengths.

(c) From (a), compute:

$$(r+1) - \frac{q(\alpha + \beta, \alpha + \beta)}{(\beta, \beta)} = q + \frac{2(\beta, \alpha)}{(\alpha, \alpha)} + 1 - \frac{q(\alpha + \beta, \alpha + \beta)}{(\beta, \beta)}$$

$$= \frac{2(\beta, \alpha)}{(\alpha, \alpha)} + 1 - \frac{q(\alpha, \alpha)}{(\beta, \beta)} - \frac{2q(\alpha, \beta)}{(\beta, \beta)}$$

$$= (\langle \beta, \alpha \rangle + 1) \left( 1 - \frac{q(\alpha, \alpha)}{(\beta, \beta)} \right).$$

Call the respective factors of this last product $A, B$. We have to show that one or the other is 0. The situation here is not symmetric in $\alpha, \beta$, so two cases must be distinguished:

**Case 1:** $(\alpha, \alpha) \geq (\beta, \beta)$. Then $|\langle \beta, \alpha \rangle| \leq |\langle \alpha, \beta \rangle|$. Since $\alpha, \beta$ are independent, we know (9.4) that $\langle \beta, \alpha \rangle \langle \alpha, \beta \rangle = 0, 1, 2,$ or $3$. The inequality forces $\langle \beta, \alpha \rangle = -1, 0,$ or $1$. In the first case, $A = 0$ and we are done. Otherwise $(\beta, \alpha) \geq 0$, so $(\beta + \alpha, \beta + \alpha)$ is strictly larger than both $(\beta, \beta)$ and $(\alpha, \alpha)$. Since $\alpha + \beta \in \Phi$, (b) implies that $(\alpha, \alpha) = (\beta, \beta)$. Similarly, $(\beta + 2\alpha, \beta + 2\alpha) > (\beta + \alpha, \beta + \alpha)$, so (b) implies that $\beta + 2\alpha \notin \Phi$, whence $q = 1$. Then $B = 1 - \frac{1 \cdot (\alpha, \alpha)}{(\beta, \beta)} = 0$.

**Case 2:** $(\beta, \beta) \geq (\alpha, \alpha)$. The argument is analogous, interchanging the roles of $\alpha$ and $\beta$ and using the $\beta$-string through $\alpha$.
