---
role: proof
locale: en
of_concept: kernel-identity-lemma
source_book: gtm035
source_chapter: "Chapter 19"
source_section: "19.8"
---

# Proof of Kernel Identity for Martinelli-Bochner Kernel

**Lemma 19.8.** $-\bar{\partial}_{\zeta} K_1(\zeta, z) = \bar{\partial}_z K(\zeta, z)$.

**Proof of Lemma 19.8.** We define functions

$$F(w) = \frac{\bar{w}_2}{|w|^4} \quad \text{and} \quad G(w) = \frac{\bar{w}_1}{|w|^4},$$

for $w \in \mathbb{C}^2$. Then, suppressing for now the factor $d\zeta_1 \wedge d\zeta_2$,

$$K_1 = F(\zeta - z) d\bar{z}_1 - G(\zeta - z) d\bar{z}_2$$

and

$$K = F(z - \zeta) d\bar{\zeta}_1 - G(z - \zeta) d\bar{\zeta}_2.$$

Since $F$ and $G$ are odd functions of $w$, it follows that each of the functions $\partial F / \partial \bar{w}_1$, $\partial F / \partial \bar{w}_2$, $\partial G / \partial \bar{w}_1$, $\partial G / \partial \bar{w}_2$ is an even function of $w$.

We have

$$\bar{\partial}_{\zeta} K_1 = \left( \frac{\partial}{\partial \bar{\zeta}_1} F(\zeta - z) d\bar{\zeta}_1 + \frac{\partial}{\partial \bar{\zeta}_2} F(\zeta - z) d\bar{\zeta}_2 \right) \wedge d\bar{z}_1$$

$$- \left( \frac{\partial}{\partial \bar{\zeta}_1} G(\zeta - z) d\bar{\zeta}_1 + \frac{\partial}{\partial \bar{\zeta}_2} G(\zeta - z) d\bar{\zeta}_2 \right) \wedge d\bar{z}_2.$$

Hence

$$\bar{\partial}_{\zeta} K_1 = \left( \frac{\partial F}{\partial \bar{w}_1}(\zeta - z) d\bar{\zeta}_1 + \frac{\partial F}{\partial \bar{w}_2}(\zeta - z) d\bar{\zeta}_2 \right) \wedge d\bar{z}_1 - \left( \frac{\partial G}{\partial \bar{w}_1}(\zeta - z) d\bar{\zeta}_1 + \frac{\partial G}{\partial \bar{w}_2}(\zeta - z) d\bar{\zeta}_2 \right) \wedge d\bar{z}_2.$$

For the $d\bar{\zeta}_j \wedge d\bar{z}_j$, $j = 1, 2$, terms, the identity follows from the fact noted above, that the first partial derivatives of $F$ and $G$ are even functions.

Consider now the $d\bar{\zeta}_2 \wedge d\bar{z}_1$ coefficients. We need to verify that

$$\frac{\partial F}{\partial \bar{w}_2} (\zeta - z) = -\frac{\partial G}{\partial \bar{w}_1} (z - \zeta). \tag{A.4}$$

We note that the sum of the right-hand sides of (A.3b) and (A.3c) is identically zero, for all $w$. Then (A.4) follows by taking $w = \zeta - z$ in this identity. Finally, the $d\bar{\zeta}_1 \wedge d\bar{z}_2$ term is treated in the same way. This completes the proof of Lemma 19.8. $\square$
