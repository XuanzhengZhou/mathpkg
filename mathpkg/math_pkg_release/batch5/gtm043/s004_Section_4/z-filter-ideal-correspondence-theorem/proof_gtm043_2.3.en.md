---
role: proof
locale: en
of_concept: z-filter-ideal-correspondence-theorem
source_book: gtm043
source_chapter: "2"
source_section: "2.3"
---
(a). (i). Since $I$ contains no unit, $\emptyset \notin Z[I]$.

(ii). Let $Z(f), Z(g) \in Z[I]$, with $f, g \in I$. Then $f^2 + g^2 \in I$, and $Z(f^2 + g^2) = Z(f) \cap Z(g)$. Hence $Z(f) \cap Z(g) \in Z[I]$.

(iii). Let $Z \in Z[I]$, so that $Z = Z(f)$ for some $f \in I$. If $Z' \in Z(X)$ and $Z' \supset Z$, then there exists $g \in C(X)$ such that $Z' = Z(g)$. Then $fg \in I$ and $Z(fg) = Z(f) \cup Z(g) = Z \cup Z' = Z'$. Hence $Z' \in Z[I]$.

Thus $Z[I]$ is a $z$-filter on $X$.

(b). (i) If $f \in Z^{\leftarrow}[\mathcal{F}]$ and $g \in C(X)$, then $Z(fg) \supset Z(f) \in \mathcal{F}$, so $Z(fg) \in \mathcal{F}$ by (iii) of the definition of $z$-filter. Hence $fg \in Z^{\leftarrow}[\mathcal{F}]$.

(ii) Let $f, g \in Z^{\leftarrow}[\mathcal{F}]$. Then $Z(f + g) \supset Z(f) \cap Z(g) \in \mathcal{F}$, so $Z(f+g) \in \mathcal{F}$. Hence $f+g \in Z^{\leftarrow}[\mathcal{F}]$.

(iii) $Z^{\leftarrow}[\mathcal{F}]$ contains no unit, because $\emptyset \notin \mathcal{F}$.

Thus $Z^{\leftarrow}[\mathcal{F}]$ is a proper ideal in $C(X)$.
