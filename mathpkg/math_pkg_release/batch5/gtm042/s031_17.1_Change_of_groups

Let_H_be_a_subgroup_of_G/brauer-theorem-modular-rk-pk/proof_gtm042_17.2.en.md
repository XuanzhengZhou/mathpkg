---
role: proof
locale: en
of_concept: brauer-theorem-modular-rk-pk
source_book: gtm042
source_chapter: "17"
source_section: "17.2"
---

Let $l_K$ (resp. $l_k$) denote the identity element of the ring $R_K(G)$ (resp. $R_k(G)$). We have $d(l_K) = l_k$. By Theorem 27 (Brauer's theorem in the ordinary case), we can write $l_K$ in the form

$$l_K = \sum_{H \in X} \text{Ind}_H^G(x_H) \quad \text{with} \quad x_H \in R_K(H).$$

Applying the homomorphism $d$, and using the fact that $d$ commutes with $\text{Ind}_H^G$, we obtain an analogous formula for $l_k$:

$$l_k = \sum_{H \in X} \text{Ind}_H^G(x_H') \quad \text{with} \quad x_H' = d(x_H) \in R_k(H).$$

Now for any $y \in R_k(G)$ (resp. $y \in P_k(G)$), we multiply by $y$:

$$y = l_k \cdot y = \sum_{H \in X} \text{Ind}_H^G(x_H') \cdot y.$$

Using the induction-restriction formula $(*)$ from Section 17.1 in case (b) (resp. case (c)), we have

$$\text{Ind}_H^G(x_H') \cdot y = \text{Ind}_H^G(x_H' \cdot \text{Res}_H^G y).$$

Since $x_H' \cdot \text{Res}_H^G y \in R_k(H)$ (resp. $P_k(H)$), this shows that $y$ belongs to the image of the induction map from $\bigoplus_{H \in X} R_k(H)$ (resp. $\bigoplus_{H \in X} P_k(H)$). Hence the induction homomorphisms are surjective.
