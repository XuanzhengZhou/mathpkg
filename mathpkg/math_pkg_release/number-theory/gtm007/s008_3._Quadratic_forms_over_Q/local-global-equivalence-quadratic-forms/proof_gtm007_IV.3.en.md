---
role: proof
locale: en
of_concept: local-global-equivalence-quadratic-forms
source_book: gtm007
source_chapter: "IV"
source_section: "3"
---

The necessity is trivial. To prove the sufficiency, we use induction on the rank $n$ of $f$ and $f'$.

If $n = 0$, there is nothing to prove. Otherwise, by Corollary 1 to Theorem 8 (Hasse–Minkowski), there exists $a \in \mathbf{Q}^*$ represented by $f$, and therefore also represented by $f'$. Thus we can write
$$f \sim aZ^2 \oplus g, \qquad f' \sim aZ^2 \oplus g'.$$
By Theorem 4 of §1.6 (Witt cancellation over $\mathbf{Q}_v$), the equivalence of $f$ and $f'$ over $\mathbf{Q}_v$ implies $g \sim g'$ over $\mathbf{Q}_v$ for all $v \in V$. The induction hypothesis then shows that $g \sim g'$ over $\mathbf{Q}$, hence $f \sim f'$ over $\mathbf{Q}$.
