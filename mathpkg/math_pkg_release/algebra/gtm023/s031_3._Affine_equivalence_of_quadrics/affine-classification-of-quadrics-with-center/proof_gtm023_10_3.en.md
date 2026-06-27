---
role: proof
locale: en
of_concept: affine-classification-of-quadrics-with-center
source_book: gtm023
source_chapter: "X. Quadrics"
source_section: "§3. Affine equivalence of quadrics"
---

Assume that $x \to x'$ is an affine mapping carrying $Q_1$ into $Q_2$. Since centers are transformed into centers, we may assume the mapping sends $c_1$ into $c_2$ and hence has the form
$$x' = \tau(x - c_1) + c_2.$$
By hypothesis, $Q_1$ is mapped onto $Q_2$, so the equation
$$\Phi_2(\tau(x - c_1)) = 1$$
must represent the quadric $Q_1$. Comparing this with the defining equation $Q_1: \Phi_1(x - c_1) = 1$ and applying the uniqueness theorem (sec. 10.9), we find that
$$\Phi_1(x) = \Phi_2(\tau x).$$
This relation implies that $\Phi_1$ and $\Phi_2$ have the same rank and the same index:
$$r_1 = r_2 \quad \text{and} \quad s_1 = s_2.$$

Conversely, if $r_1 = r_2$ and $s_1 = s_2$, then there exists a linear automorphism $\tau$ of $E$ such that $\Phi_1(x) = \Phi_2(\tau x)$. Then the affine mapping
$$x' = \tau(x - c_1) + c_2$$
transforms $Q_1$ into $Q_2$, proving affine equivalence.
