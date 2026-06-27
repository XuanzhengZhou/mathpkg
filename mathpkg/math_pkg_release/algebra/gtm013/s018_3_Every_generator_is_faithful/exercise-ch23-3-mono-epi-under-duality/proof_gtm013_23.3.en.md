---
role: proof
locale: en
of_concept: exercise-ch23-3-mono-epi-under-duality
source_book: gtm013
source_chapter: "6"
source_section: "23. Exercises"
---
Recall that $f: A \to B$ is a monomorphism iff it is left-cancellable: for any $u, v: X \to A$, $fu = fv$ implies $u = v$. An epimorphism is right-cancellable.

Suppose $f$ is monic in $\mathcal{C}$ and let $u, v: H'(A) \to Y$ in $\mathcal{D}$ satisfy $u \circ H'(f) = v \circ H'(f)$. Since $(H', H'')$ is a duality, we have natural isomorphisms $\eta: H''H' \cong 1_{\mathcal{C}}$ and $\zeta: H'H'' \cong 1_{\mathcal{D}}$. Applying $H''$ and using naturality, $H''(u) \circ H''H'(f) = H''(v) \circ H''H'(f)$. But $H''H'(f) \cong f$ via $\eta$, and since $f$ is monic, $H''(u) \cong H''(v)$ after composing with $\eta$. Applying $H'$ again gives $u = v$, so $H'(f)$ is epic.

Conversely, if $H'(f)$ is epic in $\mathcal{D}$, the dual argument (using that $H''$ is also part of a duality) shows $f$ is monic in $\mathcal{C}$. The statement about epimorphisms follows by symmetry, exchanging the roles of $\mathcal{C}$ and $\mathcal{D}$.
