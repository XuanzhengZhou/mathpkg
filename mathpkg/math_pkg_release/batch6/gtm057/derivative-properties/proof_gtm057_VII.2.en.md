---
role: proof
locale: en
of_concept: derivative-properties
source_book: gtm057
source_chapter: "VII"
source_section: "2"
---

From the axioms for a derivative $D$ in a group ring $JG$:
- (2.1) $D(v_1+v_2) = Dv_1 + Dv_2$ (additivity).
- (2.2) $D(v_1 v_2) = (Dv_1)t(v_2) + v_1 Dv_2$ (product rule).

**Property (2.5):** $D(\sum n_i g_i) = \sum n_i D g_i$ follows from (2.1) and the fact that $D(ng) = n Dg$ for any integer $n$ (by induction from additivity).

**Property (2.6):** $Dn = 0$ for any integer $n$. Since $D1 = D(1 \cdot 1) = D1 + D1$, we have $D1 = 0$. By additivity, $Dn = n D1 = 0$.

**Property (2.7):** $D g^{-1} = -g^{-1} Dg$. From $0 = D(g^{-1}g) = Dg^{-1} + g^{-1} Dg$ (since $t(g) = 1$).

**Property (2.8):** $D g^n = \frac{g^n-1}{g-1} Dg$, proved by induction on $|n|$ using the product rule and the definition of $(g^n-1)/(g-1)$.
