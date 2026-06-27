---
role: proof
locale: en
of_concept: curvature-invariance-under-isometries
source_book: gtm051
source_chapter: "3"
source_section: "5"
---

**(i) Invariance under isometries of $\mathbb{R}^3$.** Let $B: \mathbb{R}^3 \to \mathbb{R}^3$ be an isometry. Then $B(x) = Ax + b$ with $A \in O(3)$ and $b \in \mathbb{R}^3$. Set $\tilde{f} = B \circ f$. The differential is $d\tilde{f} = A \circ df$, and the unit normal transforms as $\tilde{n} = (\det A) A n$. Consequently the Weingarten map transforms by $d\tilde{n} \circ d\tilde{f}^{-1} = (\det A) A \circ (dn \circ df^{-1}) \circ A^{-1}$. Since $A$ is orthogonal, $\tilde{L}_u$ is similar to $\pm L_u$ (the sign being $\det A$). The principal curvatures, being eigenvalues, satisfy $\tilde{\kappa}_i = (\det A) \kappa_i$, and hence $\tilde{K} = \tilde{\kappa}_1 \tilde{\kappa}_2 = (\det A)^2 \kappa_1 \kappa_2 = K$ and $\tilde{H} = \frac{1}{2}(\tilde{\kappa}_1 + \tilde{\kappa}_2) = (\det A) H$. A congruence has $\det A = +1$, a symmetry has $\det A = -1$.

**(ii) Invariance under change of variables.** Let $\phi: V \to U$ be a diffeomorphism and $\tilde{f} = f \circ \phi$. By the chain rule, $d\tilde{f} = df \circ d\phi$. The unit normal satisfies $\tilde{n} = \pm n \circ \phi$ (with the sign depending on whether $\phi$ preserves orientation). The fundamental forms pull back: $\tilde{I} = \phi^* I$, $\tilde{II} = \phi^* II$. Since the principal curvatures are the eigenvalues of $II$ with respect to $I$, and these transform covariantly under $\phi$, we obtain $\tilde{\kappa} = \kappa \circ \phi$, $\tilde{K} = K \circ \phi$, and $\tilde{H} = H \circ \phi$.
