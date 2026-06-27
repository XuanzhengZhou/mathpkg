---
role: proof
locale: en
of_concept: theorem-5-1-galois-quasi-isomorphism
source_book: gtm059
source_chapter: "5"
source_section: "5"
---

*Proof.* By class field theory, the Artin reciprocity map gives an isomorphism

$$G_M(K) \cong J_K \;/\; \overline{K^* U_p^\perp},$$

where $J_K$ is the idele group. The subgroup $U_p$ (units at primes dividing $p$) decomposes the idele group. Using the lemma on the intersection $\overline{U_p E} \cap \overline{U_p^\perp K^*}$, one obtains the exact sequence that relates $G_M(K)$ to $U_p E$.

Specifically, consider the exact sequence

$$1 \to \overline{U_p^\perp K^*} \to \overline{U_p^\perp K^*} \cdot \overline{U_p E} \to (\overline{U_p^\perp K^*} \cdot \overline{U_p E}) / \overline{U_p^\perp K^*} \to 1.$$

The quotient on the right is isomorphic to $\overline{U_p E} / (\overline{U_p E} \cap \overline{U_p^\perp K^*})$, which by the lemma is $\overline{U_p E} / \overline{E}$. This yields the quasi-isomorphism.

The statement about $\mathbb{Z}_p^{r_2+1}$ follows from the fact that $U_p$ is isomorphic to a product of $\mathbb{Z}_p$'s (one for each prime dividing $p$), and the global unit group $E$ has rank $r_1 + r_2 - 1$. The quotient by the closure of global units leaves a $\mathbb{Z}_p$-module of rank $(r_1 + 2r_2) - (r_1 + r_2 - 1) = r_2 + 1$, assuming the Leopoldt conjecture.
