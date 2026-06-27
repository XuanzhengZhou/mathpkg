---
role: proof
locale: en
of_concept: finite-order-criterion-for-infinitesimal-stability
source_book: gtm014
source_chapter: "V"
source_section: "§1"
---

**Proof of Theorem 1.2.** We shall use the Generalized Malgrange Preparation Theorem.
First note that
\[
C^\infty(f^*TY)_p = \bigoplus_{i=1}^{m} C_p^\infty(X)
\]
since locally $\tau(x) = \sum_{i=1}^{m} \tau_i(x) \frac{\partial}{\partial y_i}$.
Thus $C^\infty(f^*TY)_p$ is a finitely generated $C_p^\infty(X)$-module.

Let
\[
A = \{(df)(\zeta) \mid \zeta \in C^\infty(TX)_p\}.
\]
$A$ is a submodule of $C^\infty(f^*TY)_p$, so the quotient
\[
M_f^p = C^\infty(f^*TY)_p / A
\]
is a finitely generated $C_p^\infty(X)$-module.
Via the pullback homomorphism $f^*: C_q^\infty(Y) \to C_p^\infty(X)$, the module $M_f^p$ becomes a $C_q^\infty(Y)$-module.

Now suppose $[f]_p$ is infinitesimally stable. By definition, every $\tau \in C^\infty(f^*TY)_p$ can be written as $\tau = (df)(\zeta) + f^*\eta$ for some $\zeta \in C^\infty(TX)_p$ and $\eta \in C^\infty(TY)_q$. This means that the map $f^*: C^\infty(TY)_q \to M_f^p$ induced by $\eta \mapsto [f^*\eta]$ is surjective. Equivalently, $M_f^p$ is a finitely generated $C_q^\infty(Y)$-module.

Applying the Generalized Malgrange Preparation Theorem to the $C_p^\infty(X)$-module $M_f^p$ viewed as a $C_q^\infty(Y)$-module, the finiteness of $M_f^p$ over $C_q^\infty(Y)$ is equivalent to the condition that the equations $(**)$ can be solved to order $m = \dim Y$ (since $C_q^\infty(Y) \cong C_0^\infty(\mathbf{R}^m)$ locally).

Conversely, if the equations $(**)$ can be solved to order $m$, then the Malgrange Preparation Theorem implies that $M_f^p$ is finitely generated over $C_q^\infty(Y)$. The surjectivity of $f^*: C^\infty(TY)_q \to M_f^p$ then yields that every $\tau$ decomposes as $\tau = (df)(\zeta) + f^*\eta$, i.e., $[f]_p$ is infinitesimally stable. $\square$
