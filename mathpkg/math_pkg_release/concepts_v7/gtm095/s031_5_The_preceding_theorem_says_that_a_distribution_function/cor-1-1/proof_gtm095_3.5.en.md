---
role: proof
locale: en
of_concept: cor-1-1
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Corollary 1 (Formulas connecting moments and semi-invariants)

**Corollary 1.** The following formulas connect moments and semi-invariants:

$$m_{\xi}^{(\nu)} = \sum_{\{r_1 \lambda^{(1)} + \cdots + r_x \lambda^{(x)} = \nu\}} \frac{1}{r_1! \cdots r_x!} \frac{\nu!}{(\lambda^{(1)}!)^{r_1} \cdots (\lambda^{(x)}!)^{r_x}} \prod_{j=1}^{x} [s_{\xi}^{(\lambda^{(j)})}]^{r_j}, \tag{44}$$

$$s_{\xi}^{(\nu)} = \sum_{\{r_1 \lambda^{(1)} + \cdots + r_x \lambda^{(x)} = \nu\}} \frac{(-1)^{q-1}(q-1)!}{r_1! \cdots r_x!} \frac{\nu!}{(\lambda^{(1)}!)^{r_1} \cdots (\lambda^{(x)}!)^{r_x}} \prod_{j=1}^{x} [m_{\xi}^{(\lambda^{(j)})}]^{r_j}, \tag{45}$$

where the summation $\sum_{\{r_1 \lambda^{(1)} + \cdots + r_x \lambda^{(x)} = \nu\}}$ is taken over all unordered collections of distinct vectors $\lambda^{(1)}, \ldots, \lambda^{(x)}$ and positive integers $r_1, \ldots, r_x$ with $q = r_1 + \cdots + r_x$.

## Proof

Formulas (44) and (45) are obtained from (40) and (41) of Theorem 6 by grouping together terms with the same $\lambda^{(j)}$ in the sums. In (40), the sum runs over all ordered $q$-tuples $(\lambda^{(1)}, \ldots, \lambda^{(q)})$ whose sum is $\nu$. If among these $q$ vectors there are $x$ distinct ones $\lambda^{(1)}, \ldots, \lambda^{(x)}$, occurring with multiplicities $r_1, \ldots, r_x$ (so $q = r_1 + \cdots + r_x$), then the number of ordered $q$-tuples giving rise to the same unordered collection is ${q \choose r_1, \ldots, r_x} / r_1! \cdots r_x!$. Accounting for this combinatorial factor transforms the ordered sum over $(\lambda^{(1)}, \ldots, \lambda^{(q)})$ into the unordered sum over distinct $\lambda^{(j)}$ with multiplicities $r_j$, yielding:

$$\frac{1}{q!} \times \frac{q!}{r_1! \cdots r_x!} = \frac{1}{r_1! \cdots r_x!}.$$

Applying this grouping to (40) gives (44). Similarly, applying the same grouping to (41), with the factor $(-1)^{q-1}/q$ replaced by $(-1)^{q-1}(q-1)!/q!$, yields (45).
