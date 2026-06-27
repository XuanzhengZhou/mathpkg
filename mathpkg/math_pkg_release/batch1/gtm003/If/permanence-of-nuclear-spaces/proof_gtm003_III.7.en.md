---
role: proof
locale: en
of_concept: permanence-of-nuclear-spaces
source_book: gtm003
source_chapter: "III"
source_section: "7"
---

**Products.** Let $\{E_\alpha\}$ be a family of nuclear spaces, $E = \prod_\alpha E_\alpha$. Let $u$ be a continuous linear map of $E$ into a Banach space $F$. There exists a $0$-neighborhood $V$ such that $u(V)$ is bounded in $F$. By definition of the product topology, $V$ contains $V_{\alpha_1} \times \cdots \times V_{\alpha_n} \times \prod_{\beta \neq \alpha_i} E_\beta$. It follows that $u$ vanishes on $G = \prod_{\beta \neq \alpha_i} E_\beta$. Since $E = \prod_{i=1}^n E_{\alpha_i} \oplus G$, the restriction of $u$ to the finite product is nuclear (as a sum of nuclear maps). Hence $u$ is nuclear and $E$ is nuclear.

**Subspaces.** Let $M$ be a subspace of a nuclear space $E$. For each convex, circled $0$-neighborhood $U$ in $E$, the canonical map $E \to \tilde{E}_U$ factors through $M_V \to \tilde{E}_U$. By property (c) of (7.2), one can find $V \subset U$ such that the linking map is nuclear, and the same holds for the induced map on quotient spaces.

**Quotients.** For a separated quotient $E/M$, one uses the orthogonal decomposition $\tilde{E}_U = \overline{M} \oplus \overline{M}^\perp$ in the Hilbert space associated to $U$, and the induced map on the quotient of the completions is nuclear by the series decomposition of the nuclear linking map.

**Direct sums.** For a countable direct sum, each summand is nuclear by the above, and a continuous linear map into a Banach space restricts to each summand. The equicontinuity argument from the product case, together with the nuclearity of finite direct sums, yields the result.
