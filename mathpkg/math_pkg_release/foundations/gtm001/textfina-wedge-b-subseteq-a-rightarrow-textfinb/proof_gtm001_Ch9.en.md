---
role: proof
locale: en
of_concept: textfina-wedge-b-subseteq-a-rightarrow-textfinb
source_book: gtm001
source_chapter: "9"
source_section: ""
---

If $a$ is finite then by Definition 10.29, $(\exists n)[a \simeq n]$. If $b \subseteq a$ it then follows from Proposition 10.12 that $(\exists \beta \leq n)[b \simeq \beta]$. Since such a $\beta$ must be in $\omega$ it follows that $b$ is finite.

EXERCISES

Prove the following.

(1) $\text{Fin}(n)$.

(2) $\text{Fin}(a) \rightarrow \text{Fin}(a \cup \{b\})$.

(3) $\text{Fin}(a) \rightarrow \text{Fin}(a - \{b\})$.

(4) $\text{Fin}(a) \rightarrow \text{Fin}(\{b\} \times a)$.

(5) $\text{Inf}(a) \rightarrow \bar{a} = \overline{a \cup \{b\}}$.

(6) $\text{Inf}(a) \wedge a \simeq b \rightarrow \text{Inf}(b)$.

(7) $\text{Inf}(a) \rightarrow (\exists x)[x \subset a \wedge x \simeq a]$ (Hint: Use AC).

(8) $\text{Inf}(a) \rightarrow

$(a - \{x\}) \cup b$ is finite and $(a - \{x\}) \times b$ is finite. But $a \cup b = [(a - \{x\}) \cup b] \cup \{x\}$ which is finite by Exercise 2 above, and $a \times b = [(a - \{x\}) \times b] \cup \{x\} \times b$, which is finite because it is the union of two finite sets.
