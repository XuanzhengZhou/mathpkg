---
role: proof
locale: en
of_concept: cantor-schroder-bernstein-zermelo-theorem
source_book: gtm053
source_chapter: "III"
source_section: "1"
---

**Proof of (a), first part (Schroder-Bernstein).** Suppose $M$ has the same cardinality as $M' \subset N$ and $N$ has the same cardinality as $N_1 \subset M \cong M'$. Identify $M$ with $M'$. We then have $N_1 \subset M \subset N$ and a one-to-one correspondence $f: N \to N_1$. Set $M_0 = M \setminus N_1$, $M_{k+1} = f(M_k)$, and $M_\infty = \bigcup_{k=0}^\infty M_k$. Define $g: N \to M$ by $g(x) = x$ if $x \notin M_\infty$, and $g(x) = f(x)$ if $x \in M_\infty$. Then $g$ is a one-to-one correspondence between $N$ and $M$.

**Proof of (a), second part (Zermelo).** To prove comparability, it suffices to show any set can be well-ordered. Let $M$ be any set. For every nonempty $N \subset M$ choose $c(N) \in N$. Call a well-ordering $<$ of $M' \subset M$ admissible if $c(M \setminus \hat{X}) = X$ for all $X \in M'$, where $\hat{X} = \{Y \mid Y \in M', Y < X\}$. If $M' \neq M''$ are two subsets with admissible well-orderings, one is an initial segment of the other. The union of all such $M'$ has an admissible ordering and must equal $M$. Hence $M$ can be well-ordered.

**Proof of (b).** $\mathcal{P}(M)$ contains all singletons $\{x\}$ for $x \in M$, so $\operatorname{card} \mathcal{P}(M) \geqslant \operatorname{card} M$. If there were a bijection $f: M \to \mathcal{P}(M)$, consider $N = \{x \in M \mid x \notin f(x)\}$. Then $N \in \mathcal{P}(M)$ but $N \neq f(x)$ for any $x \in M$, contradiction (Cantor's diagonal argument).

**Proof of (c).** Any set of cardinalities corresponds to a set of ordinals (since every set has the cardinality of some ordinal by (a)), and any set of ordinals has a least element. Therefore cardinalities are well-ordered.
