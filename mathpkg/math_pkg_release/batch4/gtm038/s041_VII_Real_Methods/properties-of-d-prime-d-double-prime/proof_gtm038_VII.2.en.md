---
role: proof
locale: en
of_concept: properties-of-d-prime-d-double-prime
source_book: gtm038
source_chapter: "VII"
source_section: "2"
---

It suffices to prove the statements for pure forms.

(1) $\mathbb{C}$-linearity and $d' + d'' = d$ are immediate from the definitions.

(2) From $dd = 0$ we have:
$$0 = dd\varphi = (d' + d'') \circ (d' + d'')\varphi = d'd'\varphi + d'd''\varphi + d''d'\varphi + d''d''\varphi.$$

If $\varphi$ has type $(p, q)$, then:
- $d'd'\varphi$ has type $(p + 2, q)$,
- $d'd''\varphi + d''d'\varphi$ has type $(p + 1, q + 1)$,
- $d''d''\varphi$ has type $(p, q + 2)$.

Since forms of different types are linearly independent (by Theorem 1.5), each component must vanish separately. Hence $d'd' = 0$, $d''d'' = 0$, and $d'd'' + d''d' = 0$.

(3) The operators are not real because conjugation interchanges the roles of $d'$ and $d''$. Explicitly, for a pure form $\varphi$ of type $(p,q)$,
$$\overline{d'\varphi} = d''\overline{\varphi}, \quad \overline{d''\varphi} = d'\overline{\varphi}.$$

(4) For the Leibniz rule, if $\varphi$ is an $\ell$-form (pure of type $(p,q)$ with $p+q=\ell$) and $\psi$ arbitrary, then using the decomposition $d = d' + d''$ and the known Leibniz rule for $d$:
$$d(\varphi \wedge \psi) = d\varphi \wedge \psi + (-1)^{\ell} \varphi \wedge d\psi.$$
Expanding both sides into type components and comparing the $(p+p'+1, q+q')$ part yields the formula for $d'$, while comparing the $(p+p', q+q'+1)$ part yields the formula for $d''$.
