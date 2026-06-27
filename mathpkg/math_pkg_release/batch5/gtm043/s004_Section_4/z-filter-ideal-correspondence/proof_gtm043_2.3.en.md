---
role: proof
locale: en
of_concept: z-filter-ideal-correspondence
source_book: gtm043
source_chapter: "2"
source_section: "2.3"
---

\textbf{(a).} (i) Since $I$ contains no unit, $\emptyset \notin Z[I]$.

(ii) Let $Z_1, Z_2 \in Z[I]$, say $Z_1 = Z(f_1)$, $Z_2 = Z(f_2)$, with $f_1, f_2 \in I$. Then $f_1^2 + f_2^2 \in I$, and $Z(f_1^2 + f_2^2) = Z_1 \cap Z_2$. Hence $Z_1 \cap Z_2 \in Z[I]$.

(iii) Let $Z_1 \in Z[I]$, say $Z_1 = Z(f)$, with $f \in I$, and let $Z_2 \in Z(X)$ satisfy $Z_2 \supset Z_1$. Write $Z_2 = Z(g)$. Then $Z(fg) = Z(f) \cup Z(g) = Z_2$. Since $fg \in I$, we have $Z_2 \in Z[I]$.

\textbf{(b).} We verify the ideal axioms. Since $\mathcal{F} \neq \emptyset$ and $\emptyset \notin \mathcal{F}$, the zero function $0$ (with $Z(0) = X \in \mathcal{F}$) belongs to $Z^{\leftarrow}[\mathcal{F}]$, and the constant function $1$ (with $Z(1) = \emptyset \notin \mathcal{F}$) does not. Thus $Z^{\leftarrow}[\mathcal{F}]$ is a proper subset of $C(X)$.

If $f, g \in Z^{\leftarrow}[\mathcal{F}]$, then $Z(f), Z(g) \in \mathcal{F}$. Since $Z(f - g) \supset Z(f) \cap Z(g)$, we have $Z(f - g) \in \mathcal{F}$ by properties (ii) and (iii) of $z$-filters, so $f - g \in Z^{\leftarrow}[\mathcal{F}]$.

If $f \in Z^{\leftarrow}[\mathcal{F}]$ and $h \in C(X)$, then $Z(fh) \supset Z(f)$, whence $Z(fh) \in \mathcal{F}$ and $fh \in Z^{\leftarrow}[\mathcal{F}]$. Thus $Z^{\leftarrow}[\mathcal{F}]$ is an ideal.
