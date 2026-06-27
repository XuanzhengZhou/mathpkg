---
role: proof
locale: en
of_concept: kernel-differential-is-closed
source_book: gtm035
source_chapter: "Chapter 13"
source_section: "13.6"
---
# Proof of Lemma 13.6 (Differential of Cauchy-Fantappie Kernel is Closed)

**Lemma 13.6.** Fix $z \in D$. Then $dK_w(\zeta, z) = 0$ for $\zeta \in D \setminus \{z\}$.

**Proof.** Recall the Cauchy-Fantappie form

$$K_w(\zeta, z) = \sum_{j=1}^{n} (-1)^{j-1} w_j \; dw_1 \wedge \cdots \wedge \widehat{dw_j} \wedge \cdots \wedge dw_n \wedge d\zeta_1 \wedge \cdots \wedge d\zeta_n,$$

where the functions $w_j = w_j(\zeta, z)$ satisfy

$$\sum_{j=1}^{n} w_j(\zeta, z) (\zeta_j - z_j) = 1. \tag{13}$$

Note that (13) yields, by applying the exterior derivative $d$ (with respect to $\zeta$),

$$d\left(\sum_{j=1}^{n} w_j (\zeta_j - z_j)\right) = \sum_{j=1}^{n} \left[ (\zeta_j - z_j) dw_j + w_j d\zeta_j \right] = 0,$$

or equivalently

$$\sum_{j=1}^{n} (\zeta_j - z_j) dw_j = - \sum_{j=1}^{n} w_j d\zeta_j. \tag{20}$$

Now consider the differential of $K_w$. Viewed as a form in $\zeta$ alone (with $z$ fixed), $K_w$ has the structure

$$K_w = \sum_{j=1}^{n} (-1)^{j-1} w_j \; dw_1 \wedge \cdots \wedge \widehat{dw_j} \wedge \cdots \wedge dw_n \wedge d\zeta,$$

where $d\zeta = d\zeta_1 \wedge \cdots \wedge d\zeta_n$. The exterior derivative is

$$dK_w = \sum_{j=1}^{n} (-1)^{j-1} dw_j \wedge dw_1 \wedge \cdots \wedge \widehat{dw_j} \wedge \cdots \wedge dw_n \wedge d\zeta$$

$$+ \sum_{j=1}^{n} (-1)^{j-1} w_j \; d(dw_1 \wedge \cdots \wedge \widehat{dw_j} \wedge \cdots \wedge dw_n) \wedge d\zeta.$$

The second sum vanishes because $d^2 = 0$. In the first sum, the term $dw_j \wedge dw_1 \wedge \cdots \wedge \widehat{dw_j} \wedge \cdots \wedge dw_n$ is (up to sign) simply $dw_1 \wedge \cdots \wedge dw_n$, which is a form of top degree in the $dw_j$ variables. Since each $dw_j$ is a $1$-form on $D$, the full wedge product $dw_1 \wedge \cdots \wedge dw_n$ is an $n$-form in the $w$-variables. Thus

$$dK_w = \left( \sum_{j=1}^{n} dw_j \right) \wedge (\text{the } n-1 \text{-form in } w) \wedge d\zeta.$$

More systematically, we note that $K_w$ can be written as

$$K_w = \left( \sum_{j=1}^{n} (-1)^{j-1} w_j \; \widehat{dw_j} \right) \wedge d\zeta,$$

and its differential, using $d^2 = 0$, is

$$dK_w = \left( \sum_{j=1}^{n} dw_j \right) \wedge \left( \bigwedge_{k \neq j} dw_k \right)?$$

Actually, a cleaner computation goes as follows. For each $j$, let

$$\beta_j = dw_1 \wedge \cdots \wedge \widehat{dw_j} \wedge \cdots \wedge dw_n.$$

Then $dK_w = \sum_{j=1}^{n} (-1)^{j-1} dw_j \wedge \beta_j \wedge d\zeta$. Note that $dw_j \wedge \beta_j = (-1)^{j-1} dw_1 \wedge \cdots \wedge dw_n$. So

$$dK_w = \sum_{j=1}^{n} (-1)^{j-1} (-1)^{j-1} dw_1 \wedge \cdots \wedge dw_n \wedge d\zeta = n \; dw_1 \wedge \cdots \wedge dw_n \wedge d\zeta.$$

Now we use relation (20). Wedge (20) with $(\bigwedge_{k \neq \ell} \bar{\partial} w_k) \wedge d\zeta$. On the left we obtain $(\zeta_\ell - z_\ell)(\bigwedge_{k=1}^n \bar{\partial} w_k) \wedge d\zeta$, and on the right we get $0$ (because of repetitions: each $dw_k$ appears twice). Hence

$$(\zeta_\ell - z_\ell) \bigwedge_{k=1}^{n} \bar{\partial} w_k \wedge d\zeta = 0 \quad \text{for each } \ell.$$

Since the functions $w_j$ are smooth on $D \setminus \{z\}$, and at any $\zeta \neq z$ at least one coordinate satisfies $\zeta_\ell - z_\ell \neq 0$, we deduce that

$$\bigwedge_{k=1}^{n} \bar{\partial} w_k \wedge d\zeta = 0.$$

But $dw_k = \partial w_k + \bar{\partial} w_k$, and expanding $dw_1 \wedge \cdots \wedge dw_n$ reveals that the only term that survives when wedged with $d\zeta$ (which already contains all $d\zeta_j$) is the one involving all $\bar{\partial} w_k$. Specifically, since $d\zeta$ contains $d\zeta_1 \wedge \cdots \wedge d\zeta_n$, any $\partial w_k$ term containing $d\zeta_j$ forms a repetition and vanishes. Hence

$$dw_1 \wedge \cdots \wedge dw_n \wedge d\zeta = \bar{\partial} w_1 \wedge \cdots \wedge \bar{\partial} w_n \wedge d\zeta = 0.$$

Consequently, $dK_w = 0$ on $D \setminus \{z\}$. $\square$
