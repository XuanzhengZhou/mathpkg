---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Kleisli category $X_T$ is a construction that, given a monad $\langle T, \eta, \mu \rangle$ on a category $X$, produces a new category whose objects are the same as those of $X$ but whose morphisms $x \to y$ correspond to morphisms $f : x \to T y$ in the original category. The composition in $X_T$ is defined using the multiplication $\mu$ of the monad, and the identity on $x_T$ is given by the unit $\eta_x$. The Kleisli construction yields an adjunction $F_T \dashv G_T$ whose associated monad is precisely the original monad $T$, and it provides the initial resolution of $T$ among all adjunctions defining the same monad.
