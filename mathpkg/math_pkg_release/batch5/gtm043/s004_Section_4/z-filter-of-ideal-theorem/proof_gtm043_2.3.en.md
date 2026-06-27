---
role: proof
locale: en
of_concept: z-filter-of-ideal-theorem
source_book: gtm043
source_chapter: "2"
source_section: "2.3"
---

(a) (i) Since $I$ contains no unit, $\emptyset \notin Z[I]$. (ii) Let $Z_1 = Z(f_1)$, $Z_2 = Z(f_2)$ with $f_1, f_2 \in I$. Then $Z_1 \cap Z_2 = Z(f_1^2 + f_2^2)$, and $f_1^2 + f_2^2 \in I$ because $I$ is an ideal. (iii) If $Z \in Z[I]$, say $Z = Z(f)$, and $Z' \supset Z$ with $Z' = Z(g)$, then $Z(f) \subset Z(g)$ implies $Z(fg) = Z(f)$, so $fg \in I$ and $Z' \supset Z(fg)$. Hence $Z' = Z(fg) \cup Z' \in Z[I]$ because $Z[I]$ is closed under supersets and finite intersections.

(b) (i) $Z(1) = \emptyset \notin \mathcal{F}$, so $1 \notin Z^{\leftarrow}[\mathcal{F}]$, hence it is proper. (ii) If $f, g \in Z^{\leftarrow}[\mathcal{F}]$, then $Z(f), Z(g) \in \mathcal{F}$. Since $Z(f - g) \supset Z(f) \cap Z(g) \in \mathcal{F}$, we have $Z(f - g) \in \mathcal{F}$, so $f - g \in Z^{\leftarrow}[\mathcal{F}]$. (iii) If $f \in Z^{\leftarrow}[\mathcal{F}]$ and $h \in C(X)$, then $Z(fh) \supset Z(f) \in \mathcal{F}$, so $Z(fh) \in \mathcal{F}$, hence $fh \in Z^{\leftarrow}[\mathcal{F}]$.
