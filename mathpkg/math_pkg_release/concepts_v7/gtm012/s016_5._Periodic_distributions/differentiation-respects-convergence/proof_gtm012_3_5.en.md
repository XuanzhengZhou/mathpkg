---
role: proof
locale: en
of_concept: differentiation-respects-convergence
source_book: gtm012
source_chapter: "3"
source_section: "5"
---

# Proof of Differentiation Respects Convergence in $\mathcal{P}'$

**Proposition.** If $F_n \to F$ in $\mathcal{P}'$, then $DF_n \to DF$ in $\mathcal{P}'$. More generally, if $F_n \to F$ in $\mathcal{P}'$, then $D^k F_n \to D^k F$ in $\mathcal{P}'$ for any $k \ge 0$.

*Proof.* These assertions follow directly from the definitions. Suppose $u \in \mathcal{P}$. By the definition of the derivative of a distribution (formula (6)),

$$(DF_n)(u) = -F_n(Du).$$

Since $F_n \to F$ in $\mathcal{P}'$, we have $F_n(v) \to F(v)$ for every $v \in \mathcal{P}$. In particular, taking $v = Du$, we obtain

$$(DF_n)(u) = -F_n(Du) \to -F(Du) = DF(u).$$

Thus $DF_n(u) \to DF(u)$ for every $u \in \mathcal{P}$, which means $DF_n \to DF$ in $\mathcal{P}'$.

The general statement for higher derivatives follows by induction: by formula (7),

$$(D^k F_n)(u) = (-1)^k F_n(D^k u) \to (-1)^k F(D^k u) = (D^k F)(u).$$

Hence $D^k F_n \to D^k F$ in $\mathcal{P}'$ for every $k \ge 0$. $\square$
