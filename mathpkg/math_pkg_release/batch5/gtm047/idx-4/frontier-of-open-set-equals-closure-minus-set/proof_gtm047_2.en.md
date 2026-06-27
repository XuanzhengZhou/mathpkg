---
role: proof
locale: en
of_concept: frontier-of-open-set-equals-closure-minus-set
source_book: gtm047
source_chapter: "2"
source_section: "Separation Properties of Polygons in R^2"
---

By definition, $\operatorname{Fr} U = \overline{U} \cap \overline{X - U}$. Therefore $\operatorname{Fr} U \subset \overline{U}$. Since $U$ is open, we have $U \cap \overline{X - U} = \emptyset$. Since $\operatorname{Fr} U \subset \overline{X - U}$, it follows that $\operatorname{Fr} U \subset \overline{U} - U$.

Next observe that if $P \in \overline{U} - U$, then $P \in \overline{U}$ and $P \in X - U \subset \overline{X - U}$. Therefore $\overline{U} - U \subset \operatorname{Fr} U$.

The theorem follows. $\square$
