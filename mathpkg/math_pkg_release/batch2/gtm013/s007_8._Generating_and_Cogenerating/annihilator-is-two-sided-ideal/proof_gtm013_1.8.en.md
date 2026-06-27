---
role: proof
locale: en
of_concept: annihilator-is-two-sided-ideal
source_book: gtm013
source_chapter: "1"
source_section: "8"
---

By definition, $l_R(\mathcal{U}) = \mathrm{Rej}_R(\mathcal{U})$ is the intersection of all left ideals $I$ of $R$ such that $R/I$ embeds in some $U \in \mathcal{U}$. Since each kernel $\mathrm{Ker}(h)$ for $h: R \to U$ is a left ideal, $\mathrm{Rej}_R(\mathcal{U})$ is a left ideal. It remains to show it is also a right ideal. Let $r \in R$ and $a \in \mathrm{Rej}_R(\mathcal{U})$. For any $h: R \to U$ with $U \in \mathcal{U}$, consider $h \circ \rho_a: R \to U$, where $\rho_a$ is right multiplication by $a$. Then $h(ar) = (h \circ \rho_a)(r)$. Since $\mathrm{Rej}_R(\mathcal{U})$ is stable under endomorphisms of $_R R$ by Proposition 8.16, and right multiplication by $r$ is an endomorphism of $_R R$, we have $ar \in \mathrm{Rej}_R(\mathcal{U})$. Thus $\mathrm{Rej}_R(\mathcal{U})$ is a two-sided ideal.
