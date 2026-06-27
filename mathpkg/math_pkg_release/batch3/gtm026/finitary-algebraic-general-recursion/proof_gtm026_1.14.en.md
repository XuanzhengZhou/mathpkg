---
role: proof
locale: en
of_concept: finitary-algebraic-general-recursion
source_book: gtm026
source_chapter: "1"
source_section: "1.14"
---

The principle follows from the Uncoupling Lemma (1.11) and the inductive construction of $\Omega$-terms (1.8 and 1.9).

Given specifications (1.15) and (1.16), define $\psi(p)$ for $p \in A\Omega$ by induction on the length of $p$:

- If $p$ has length $1$, then $p \in A$ (by the construction rules, the only length-1 $\Omega$-terms are the variables). Set $\psi(p) = a\psi$ as specified by (1.15).

- If $p$ has length $> 1$, then by the Uncoupling Lemma there exists a unique integer $n > 0$, unique $\omega \in \Omega_n$, and unique $n$-tuple $(p_1, \ldots, p_n) \in (A\Omega)^n$ such that $p = p_1 \cdots p_n \omega$. Since each $p_i$ is a proper subterm of $p$, each $p_i$ has strictly smaller length, so by the induction hypothesis $\psi(p_i)$ is already defined. Then set $\psi(p) = (p_1 \cdots p_n \omega)\psi$ according to the rule specified in (1.16) in terms of the already-computed $\psi(p_i)$ and $\omega$.

The uniqueness of the decomposition guaranteed by the Uncoupling Lemma ensures that this recursive definition is well-defined: there is exactly one way to decompose $p$, so no ambiguity arises. The induction is well-founded because term length strictly decreases at each recursive step.
