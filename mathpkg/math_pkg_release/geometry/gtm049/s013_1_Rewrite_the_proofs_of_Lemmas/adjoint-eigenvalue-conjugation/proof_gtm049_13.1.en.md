---
role: proof
locale: en
of_concept: adjoint-eigenvalue-conjugation
source_book: gtm049
source_chapter: "13"
source_section: "13.1"
---

Since $w$ is an eigenvector of $f$ with eigenvalue $x$, we have $w f = x w$. For any $v \in W$,

$$
\sigma(w f^*, v) = \sigma(w, v f) = \overline{\sigma(v f, w)}.
$$

Now compute $\sigma(w, v f)$ using the adjoint property:

$$
\sigma(w f^*, v) = \overline{\sigma(v, w f^*)}.
$$

Alternatively, using the eigenvalue equation directly: for all $v \in W$,

$$
\sigma(w f^*, v) = \sigma(w, v f).
$$

Taking $v = w$, we have:

$$
\sigma(w f^*, w) = \sigma(w, w f) = \sigma(w, x w) = \bar{x}\,\sigma(w, w).
$$

On the other hand, if we set $v = w$ in $\sigma(w f^* - \bar{x} w, v) = 0$ for all $v$, we deduce $w f^* = \bar{x} w$ by the nondegeneracy of $\sigma$. More directly, for all $v \in W$:

$$
\sigma(w f^* - \bar{x} w, v) = \sigma(w f^*, v) - \bar{x} \sigma(w, v) = \sigma(w, v f) - \sigma(w, v(\bar{x})) = \sigma(w, v f - \bar{x} v).
$$

Since this argument requires more care, a cleaner approach uses the fact that the matrix of $f^*$ in a cartesian basis is the conjugate transpose of the matrix of $f$. If $w$ corresponds to a coordinate vector $\mathbf{w}$ with $A\mathbf{w} = x\mathbf{w}$, then $A^*\mathbf{w} = \bar{x}\mathbf{w}$, where $A^* = \bar{A}^T$. Hence $w f^* = \bar{x} w$. (This is left as Exercise 4(ii) in the source text.)
