---
role: proof
locale: en
of_concept: lie-algebra-of-closed-subgroup-via-ideal
source_book: gtm021
source_chapter: "9"
source_section: "Lie Algebras and Tangent Spaces"
---
Let $x \in \mathfrak{g}$ satisfy $I * x \subset I$. If $f \in I$, then evaluating at the identity:
$$(f * x)(e) = x(\lambda_{e^{-1}} f) = x(f).$$
Since $f * x \in I$ and vanishes on $H$, in particular at $e \in H$, we have $(f * x)(e) = 0$. Thus $x(f) = 0$ for all $f \in I$, which means $x \in \mathfrak{h}$ (since $\mathfrak{h}$ consists of tangent vectors annihilating $I$).

Conversely, if $x \in \mathfrak{h}$, then for any $f \in I$, we must show $f * x \in I$, i.e., $(f * x)(h) = 0$ for all $h \in H$. For $h \in H$,
$$(f * x)(h) = x(\lambda_{h^{-1}} f).$$
Since $\lambda_{h^{-1}} f \in I$ (because $I$ is stable under left translations by elements of $H$, as $H = \{x \in G \mid \rho_x I = I\}$ from Lemma 8.5), and $x$ annihilates $I$ (being in $\mathfrak{h}$), we have $x(\lambda_{h^{-1}} f) = 0$. Hence $f * x \in I$.
