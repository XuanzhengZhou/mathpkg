---
role: proof
locale: en
of_concept: dolbeault-lemma
source_book: gtm038
source_chapter: "VII"
source_section: "4"
---

Write $\varphi$ in the form $\varphi = d\bar{z}_1 \wedge \varphi_1 + \varphi_2$, where $\varphi_1, \varphi_2$ no longer contain $d\bar{z}_1$. Then

$$0 = d''\varphi = d\bar{z}_1 \wedge \left(-d''_*\varphi_1 + \frac{\partial \varphi_2}{\partial \bar{z}_1}\right) + d''_*\varphi_2.$$

Since $d''_*\varphi_2$ contains no $d\bar{z}_1$, it follows that $d''_*\varphi_2 = 0$.

Now regard $z_1$ as an additional parameter and apply the induction hypothesis.

Let

$$K_* := K_2 \times \cdots \times K_n, \quad U_* := U_2 \times \cdots \times U_n.$$

There exist an open set $U'_*$ with $K_* \subset U'_* \subset U_*$ and a $\psi = \psi^{(0,q-1)}$ in which $z_1$ appears as a parameter, such that

$$d''_*\psi | U_1 \times U'_* = \varphi_2 | U_1 \times U'_*.$$

On $U' := U_1 \times U'_*$ we have

$$\varphi - d''\psi = \varphi - d''_*\psi - d\bar{z}_1 \wedge \frac{\partial \psi}{\partial \bar{z}_1} = d\bar{z}_1 \wedge \left(\varphi_1 - \frac{\partial \psi}{\partial \bar{z}_1}\right),$$

where $\varphi_1 - (\partial \psi / \partial \bar{z}_1)$ contains no $d\bar{z}_1$. On the other hand

$$0 = d''(\varphi - d''\psi) = d\bar{z}_1 \wedge d''_*\left(\varphi_1 - \frac{\partial \psi}{\partial \bar{z}_1}\right);$$

therefore

$$d''_*\left[\varphi_1 - \frac{\partial \psi}{\partial \bar{z}_1}\right] = 0.$$

The coefficients of the form $\varphi_1 - (\partial \psi / \partial \bar{z}_1)$ are holomorphic with respect to $z_1$ on the sets $\{x_1\} \times U_*$ for $x_1 \in U_1$. By the one-dimensional Dolbeault lemma (the case $n=1$, which follows from the solution of the inhomogeneous Cauchy-Riemann equation via the Cauchy integral), there exists a form $\chi$ of type $(0, q-2)$ on a neighborhood of $K_1 \times K_*$ such that

$$\varphi_1 - \frac{\partial \psi}{\partial \bar{z}_1} = d''_*\chi.$$

One then constructs the desired form $\tilde{\psi}$ by combining $\psi$ and $\chi$ with a suitable partition of unity argument to obtain $d''\tilde{\psi} = \varphi$ on a product of open neighborhoods of the $K_v$.
