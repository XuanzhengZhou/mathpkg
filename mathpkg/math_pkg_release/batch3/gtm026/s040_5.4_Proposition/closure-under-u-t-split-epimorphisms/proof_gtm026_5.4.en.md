---
role: proof
locale: en
of_concept: closure-under-u-t-split-epimorphisms
source_book: gtm026
source_chapter: "5"
source_section: "5.4"
---

Let $(X, s, \xi) \in \mathcal{C}$ and let $f: (X, s, \xi) \longrightarrow (Y, t, \theta) \in \mathcal{A}^{\bar{T}}$ and $d: (Y, t) \longrightarrow (X, s) \in \mathcal{A}$ satisfy $d \circ f = \mathrm{id}_Y$. Consider the diagram induced by the semantic operation $\alpha: (U^{\bar{T}})^n \longrightarrow U^{\bar{T}}$:

$$
\begin{array}{ccc}
Y^n & \xrightarrow{d^n} & X^n & \xrightarrow{f^n} & Y^n \\[4pt]
{\scriptstyle (Y,\theta)\alpha}\ \downarrow & & {\scriptstyle (X,\xi)\alpha}\ \downarrow & & \downarrow\ {\scriptstyle (Y,\theta)\alpha} \\[4pt]
Y & \xrightarrow{d} & X & \xrightarrow{f} & Y
\end{array}
$$

Then $(Y, \theta)\alpha = d^n \circ (X, \xi)\alpha \circ f: (Y^n, t^n) \longrightarrow (Y, t)$ is admissible, since $d^n$ is admissible (admissibility lifts to powers), $(X, \xi)\alpha$ is admissible (since $(X, s, \xi) \in \mathcal{C}$), and $f$ is admissible (it is a $T$-homomorphism). Being a composite of admissible maps, $(Y, \theta)\alpha$ is admissible. Hence $(Y, t, \theta) \in \mathcal{C}$. $\square$
