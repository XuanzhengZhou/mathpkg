---
role: proof
locale: en
of_concept: reciprocity-law-independence
source_book: gtm059
source_chapter: "Local Class Field Theory"
source_section: "54. The Reciprocity Law"
---

Let $K$ be the completion as in the preceding section. Let $\pi$ and $\pi'$ be two uniformizers, and consider the associated Lubin-Tate extensions $K_{\pi}$ and $K_{\pi'}$. Let $K^{\mathrm{ur}}$ be the maximal unramified extension of $K$. Set
$$K'_{\pi} = K_{\pi} K^{\mathrm{ur}}, \qquad K'_{\pi'} = K_{\pi'} K^{\mathrm{ur}}.$$

We must show $K'_{\pi} = K'_{\pi'}$. Since $K^{\mathrm{ur}}$ is algebraically closed in the sense that it contains all unramified extensions, the two totally ramified extensions $K_{\pi}$ and $K_{\pi'}$ become equal after composition with a sufficiently large unramified extension. More precisely, there exists a finite unramified extension $L/K$ such that
$$L K_{\pi} = L K_{\pi'}.$$

By elementary field theory, this forces $K_{\pi} K^{\mathrm{ur}} = K_{\pi'} K^{\mathrm{ur}}$, which proves the first assertion of the theorem.

For the second assertion, we must show the independence of the association $a \mapsto r_a$. Let $r_a^{(\pi)}$ and $r_a^{(\pi')}$ denote the automorphisms of $K' = K'_{\pi} = K'_{\pi'}$ defined using $\pi$ and $\pi'$ respectively. These automorphisms coincide on $K^{\mathrm{ur}}$ since they both give the Frobenius automorphism $\varphi^{k}$ where $k = \mathrm{ord}(a)$. It remains to show they coincide on $K_{\pi}$ and $K_{\pi'}$.

Write $\pi' = \pi \cdot u$ with $u$ a unit. Let $F$ be the Frobenius power series associated with the Lubin-Tate formal group for $\pi$. For any finite subextension of $K_{\pi}$ (resp. $K_{\pi'}$), the action of $r_a^{(\pi)}$ (resp. $r_a^{(\pi')}$) on the torsion points of the formal group is given by the endomorphism $[a^{-1}]_f$. Since the Lubin-Tate formal groups for $\pi$ and $\pi'$ are isomorphic over $K^{\mathrm{ur}}$ (by a theorem in the preceding section), the two reciprocity automorphisms coincide on all torsion points, hence on the compositum $K_{\pi} K_{\pi'}$.

Therefore $r_a^{(\pi)} = r_a^{(\pi')}$ on $K'$, establishing that the reciprocity map is independent of the choice of uniformizer.
