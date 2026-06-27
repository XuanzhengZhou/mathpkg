---
role: proof
locale: en
of_concept: projectivity-domain-properties
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

(1) Suppose $g: M \to M''$ is an epimorphism and $k: M' \to M$ is a monomorphism. To see $U$ is $M''$-projective, let $h: M'' \to N$ be an epimorphism. Then $hg: M \to N$ is an epimorphism, so $(hg)_* = h_* g_*$ is epic. Since $g_*$ is epic (as $U$ is $M$-projective), $h_*$ must be epic, so $U$ is $M''$-projective. To see $U$ is $M'$-projective, assume $M' \leq M$. For $K' \leq M'$, consider the commutative diagram with exact rows and columns:

$$\begin{array}{cccccc}
0 & & \downarrow \\
0 \to M' & \to & M & \to & M/M' & \to 0 \\
n_{K'} & \downarrow & & \downarrow & & \downarrow \\
0 \to M'/K' & \to & M/K' & \to & M/M' & \to 0 \\
\downarrow & & \downarrow & & \downarrow \\
0 & & 0 & & 0
\end{array}$$

Applying $Hom_R(U, -)$ and using that the rows and columns remain exact, it follows from (3.14.4) that $(n_{K'})_*$ is epic, so $U$ is $M'$-projective.

(2) It suffices to show that if $U$ is projective relative to $M_1$ and $M_2$, then $U$ is $M_1 \oplus M_2$-projective. Let $K \leq M_1 \oplus M_2$ and consider the natural maps. For a finite subset $F \subseteq A$, $U$ is $\bigoplus_F M_\alpha$-projective by finite induction. For an arbitrary direct sum, if $\gamma: U \to Im(\gamma) \subseteq \bigoplus_A M_\alpha$, then $Im(\gamma)$ is finitely generated, so it is contained in a finite direct sum $\bigoplus_F M_\alpha$. By the finite case, there exists a lifting $\bar{\gamma}$ making the diagram commute.
