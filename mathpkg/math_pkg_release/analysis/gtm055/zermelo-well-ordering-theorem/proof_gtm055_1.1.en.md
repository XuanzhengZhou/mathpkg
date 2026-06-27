---
role: proof
locale: en
of_concept: zermelo-well-ordering-theorem
source_book: gtm055
source_chapter: "1"
source_section: "1"
---
The proof of Zermelo's Well-Ordering Theorem relies on the Axiom of Choice. One standard proof:

Let $X$ be any set. By the Axiom of Choice, there exists a choice function $f : \mathcal{P}(X) \setminus \{\varnothing\} \to X$ such that $f(A) \in A$ for every nonempty $A \subset X$. Using transfinite recursion, define a sequence $\{x_\alpha\}$ indexed by ordinal numbers:

For each ordinal $\alpha$, if $\{x_\beta : \beta < \alpha\} \neq X$, set
$$x_\alpha = f(X \setminus \{x_\beta : \beta < \alpha\}).$$

This construction continues until the set $\{x_\beta : \beta < \alpha\} = X$. By Hartogs' theorem (which does not require Choice), there exists an ordinal that cannot be injected into $X$, so the process must terminate at some ordinal $\alpha_0$. The resulting enumeration gives a well-ordering of $X$.

The equivalence to the statement about cardinal numbers follows: given a cardinal $c$, take a set $X$ with $\operatorname{card} X = c$, well-order it by the theorem to obtain an ordinal $\alpha$, then $\operatorname{card} \alpha = c$.
