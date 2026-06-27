---
role: proof
locale: en
of_concept: geometric-significance-of-rotation-vector
source_book: gtm023
source_chapter: "8"
source_section: "8.23"
---

For a proper rotation $\varphi$ of 3-space, let $F$ be the plane orthogonal to the axis $E_1$. Then $\varphi_1 = \varphi|_F$ is a proper rotation with angle $\theta$. Using formula (8.43): $\cos \theta = \frac{1}{2} \operatorname{tr} \varphi_1$. Since $\operatorname{tr} \varphi = \operatorname{tr} \varphi_1 + 1$ (adding the eigenvalue 1 from the axis), we obtain $\cos \theta = \frac{1}{2}(\operatorname{tr} \varphi - 1)$.

For $\sin \theta$, consider the rotation vector $u$ from $\psi = \frac{1}{2}(\varphi - \tilde{\varphi})$ with $\psi y = u \times y$. Let $y$ be a unit vector in $F$ orthogonal to $u$. Then $|u| = |u \times y|$ and equations (8.47)-(8.50) yield $\sin \theta = |u|$.

Thus: 1. $u$ lies on the axis; 2. $|u| = \sin \theta$; 3. With the orientation induced by $u$ on $F$, we have $0 < \theta < \pi$.
