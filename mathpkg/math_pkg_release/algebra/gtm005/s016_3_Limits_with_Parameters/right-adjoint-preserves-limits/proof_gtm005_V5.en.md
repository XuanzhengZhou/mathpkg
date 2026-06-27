---
role: proof
locale: en
of_concept: right-adjoint-preserves-limits
source_book: gtm005
source_chapter: "V"
source_section: "5. Adjoints on Limits"
---

Let $T : J \rightarrow A$ be a functor with limiting cone $\sigma : a \rightarrow T$ in $A$. Applying $G$ yields a cone $G\sigma : Ga \rightarrow GT$ in $X$. We must show it is limiting.

Consider any other cone $\tau : x \rightarrow GT$ in $X$. By the adjunction $\langle F, G, \eta, \varepsilon \rangle$, the transpose of $\tau$ under the adjunction yields a cone $\bar{\tau} : Fx \rightarrow T$ in $A$. Since $\sigma : a \rightarrow T$ is limiting, there exists a unique arrow $h : Fx \rightarrow a$ such that $\sigma \circ h = \bar{\tau}$. Taking the transpose back yields a unique arrow $\tilde{h} : x \rightarrow Ga$ with $G\sigma \circ \tilde{h} = \tau$. Hence $G\sigma$ is a limiting cone.

More conceptually, $\operatorname{Lim} : A^J \rightarrow A$ is right adjoint to the diagonal functor $\Delta : A \rightarrow A^J$. Given the adjunction $\langle F, G, \eta, \varepsilon \rangle : X \rightarrow A$, pass to the functor categories to obtain $\langle F^J, G^J \rangle : X^J \rightarrow A^J$. Now observe:
$$F^J \circ \Delta = \Delta \circ F$$
(since both send objects to the constant diagram). The composite functor $A^J \stackrel{G^J}{\longrightarrow} X^J \stackrel{\operatorname{Lim}}{\longrightarrow} X$ is right adjoint to $X \stackrel{\Delta}{\longrightarrow} X^J \stackrel{F^J}{\longrightarrow} A^J$ (composition of adjoints). But $\operatorname{Lim} \circ G^J$ is also right adjoint to $\Delta \circ F$, and so is $G \circ \operatorname{Lim}$. Since right adjoints are unique up to isomorphism,
$$\operatorname{Lim} \circ G^J \cong G \circ \operatorname{Lim},$$
which is precisely the statement that $G$ preserves limits.
