---
role: proof
locale: en
of_concept: complex-poincare-lemma
source_book: gtm035
source_chapter: "6"
source_section: "6.1"
---
# Proof of Complex Poincaré Lemma

**Theorem 6.1 (Complex Poincaré Lemma).** Let $\Omega$ be a neighborhood of the closed unit polydisk $\Delta^n = \{z \in \mathbb{C}^n \mid |z_j| \leq 1,\ j = 1, \ldots, n\}$. Fix $\omega \in \wedge^{p,q}(\Omega)$ with $q > 0$ such that $\bar{\partial}\omega = 0$ in $\Omega$. Then there exists a neighborhood $\tilde{\Omega}$ of $\Delta^n$ and a form $\tau \in \wedge^{p,q-1}(\tilde{\Omega})$ such that $\bar{\partial}\tau = \omega$ in $\tilde{\Omega}$.

*Proof.* We call a form

$$\sum_{I, J} C_{IJ} dz_I \wedge d\bar{z}_J$$

of *level* $v$, if for some $I$ and $J$ with $J = (j_1, j_2, \ldots, v)$, where $j_1 < j_2 < \cdots < v$, we have $C_{IJ} \neq 0$; while for each $I$ and $J$ with $J = (j_1, \ldots, j_s)$ where $j_1 < \cdots < j_s$ and $j_s > v$, we have $C_{IJ} = 0$.

We prove the theorem by induction on the level $v$ of $\omega$.

**Base case: level 1.** Consider a form $\omega$ of level $1$ such that $\bar{\partial}\omega = 0$. Then $\omega \in \wedge^{p,1}(\Omega)$ for some $p$ and we have

$$\omega = \sum_I a_I d\bar{z}_1 \wedge dz_I, \quad a_I \in C^\infty(\Omega) \quad \text{for each } I.$$

Applying $\bar{\partial}$:

$$0 = \bar{\partial}\omega = \sum_{I,k} \frac{\partial a_I}{\partial \bar{z}_k} d\bar{z}_k \wedge d\bar{z}_1 \wedge dz_I.$$

From linear independence of the basis wedges, the coefficients of independent terms must vanish. Since $d\bar{z}_k \wedge d\bar{z}_1$ is non-zero only when $k \neq 1$, we obtain

$$\frac{\partial a_I}{\partial \bar{z}_k} = 0 \quad \text{for all } k \geq 2.$$

By Lemma 6.3, there exists a neighborhood $\Omega_1$ of $\Delta^n$ and, for each $I$, a function $A_I \in C^\infty(\Omega_1)$ with

$$\frac{\partial A_I}{\partial \bar{z}_1} = a_I, \quad \frac{\partial A_I}{\partial \bar{z}_k} = 0 \text{ for } k \geq 2.$$

Put $\omega_1 = \sum_I A_I dz_I$. Then $\bar{\partial}\omega_1 = \sum_I \frac{\partial A_I}{\partial \bar{z}_1} d\bar{z}_1 \wedge dz_I = \sum_I a_I d\bar{z}_1 \wedge dz_I = \omega$. Thus $\tau = \omega_1$ solves $\bar{\partial}\tau = \omega$ for level $1$ forms.

**Induction step.** Assume we can solve $\bar{\partial}\tau = \omega$ for any $\bar{\partial}$-closed form $\omega$ of level $< v$. Let $\omega$ be a $\bar{\partial}$-closed form of level $v$. Write

$$\omega = d\bar{z}_v \wedge \alpha + \beta,$$

where $\alpha$ and $\beta$ are forms of level $\leq v-1$. Then

$$0 = \bar{\partial}\omega = \bar{\partial}(d\bar{z}_v \wedge \alpha) + \bar{\partial}\beta = -d\bar{z}_v \wedge \bar{\partial}\alpha + \bar{\partial}\beta,$$

where we have used Lemma 5.5. So

$$0 = d\bar{z}_v \wedge \bar{\partial}\alpha - \bar{\partial}\beta. \tag{6}$$

Let us write

$$\alpha = \sum_{I,J} a_{IJ} dz_I \wedge d\bar{z}_J, \qquad \beta = \sum_{I,J} b_{IJ} dz_I \wedge d\bar{z}_J.$$

Expanding equation (6) gives

$$0 = d\bar{z}_v \wedge \sum_{I,J,k} \frac{\partial a_{IJ}}{\partial \bar{z}_k} d\bar{z}_k \wedge dz_I \wedge d\bar{z}_J - \sum_{I,J,k} \frac{\partial b_{IJ}}{\partial \bar{z}_k} d\bar{z}_k \wedge dz_I \wedge d\bar{z}_J. \tag{7}$$

Fix $k > v$, and examine the terms on the right side of (7) containing $d\bar{z}_v \wedge d\bar{z}_k$. Because $\alpha$ and $\beta$ are of level $\leq v-1$, the only contributions to terms of the form $d\bar{z}_v \wedge d\bar{z}_k \wedge \cdots$ come from the first sum, specifically:

$$d\bar{z}_v \wedge \frac{\partial a_{IJ}}{\partial \bar{z}_k} d\bar{z}_k \wedge dz_I \wedge d\bar{z}_J.$$

Since these must cancel to zero and there are no other sources of such terms, it follows that for each $I$ and $J$,

$$\frac{\partial a_{IJ}}{\partial \bar{z}_k} = 0, \qquad k > v.$$

By Lemma 6.3, there exists a neighborhood $\Omega_1$ of $\Delta^n$ and, for each $I$ and $J$, functions $A_{IJ} \in C^\infty(\Omega_1)$ with

$$\frac{\partial A_{IJ}}{\partial \bar{z}_v} = a_{IJ}, \qquad \frac{\partial A_{IJ}}{\partial \bar{z}_k} = 0 \text{ for } k > v.$$

Put $\omega_1 = \sum_{I,J} A_{IJ} dz_I \wedge d\bar{z}_J$. Then

$$\bar{\partial}\omega_1 = d\bar{z}_v \wedge \alpha + \gamma = \omega - \beta + \gamma,$$

where $\gamma$ is a form of level $\leq v-1$. Set $\tilde{\gamma} = \gamma - \beta$, which also has level $\leq v-1$. From $\bar{\partial}\omega = 0$ and $\bar{\partial}\omega_1 = \omega + \tilde{\gamma}$, we obtain $\bar{\partial}\tilde{\gamma} = \bar{\partial}(\bar{\partial}\omega_1 - \omega) = 0$, so $\tilde{\gamma}$ is $\bar{\partial}$-closed.

By the induction hypothesis, we can choose a neighborhood $\Omega_2$ of $\Delta^n$ and a form $\tau \in \wedge^{p,q-1}(\Omega_2)$ with $\bar{\partial}\tau = \gamma - \beta = \tilde{\gamma}$. Then

$$\bar{\partial}(\omega_1 - \tau) = \bar{\partial}\omega_1 - \bar{\partial}\tau = \omega + (\gamma - \beta) - (\gamma - \beta) = \omega.$$

Taking $\tilde{\Omega}$ as a sufficiently small neighborhood contained in $\Omega_1 \cap \Omega_2$, the form $\omega^* = \omega_1 - \tau$ is the desired solution. $\square$

**Notes.** Theorem 6.1 appears in P. Dolbeault, *Formes différentielles et cohomologie sur une variété analytique complexe*, I, Ann. Math. 64 (1956), 83-130; II, Ann. Math. 65 (1957), 282-330. For an alternative proof see [Hö2, Chap. 2].
