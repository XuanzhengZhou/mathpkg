---
role: proof
locale: en
of_concept: normability-theorem
source_book: gtm036
source_chapter: "2"
source_section: "6 (Normability, Metrizability, and Embedding; Local Convexity)"
---

If there is a bounded convex neighborhood of $0$ in a linear topological space $E$, then there is a bounded circled convex neighborhood $U$ of $0$, because each convex neighborhood of $0$ contains a convex circled neighborhood of $0$. Let $p$ be the Minkowski functional of $U$; explicitly,

$$p(x) = \inf \{ t : t > 0 \text{ and } x \in tU \}.$$

Then $p$ is a pseudo-norm. To see this: subadditivity follows from the convexity of $U$ (if $x \in tU$ and $y \in sU$, then $x + y \in (t+s)U$), absolute homogeneity follows from $U$ being circled, and non-negativity is immediate from the definition. Moreover, the open unit $p$-sphere about $0$ contains $\frac{1}{2}U$ and is contained in $U$. Since $U$ is a neighborhood of $0$, the $p$-topology is precisely the given topology of $E$, establishing pseudo-normability.

Conversely, if the space is pseudo-normable with pseudo-norm $p$, then the open unit sphere $V = \{ x : p(x) < 1 \}$ is a convex circled neighborhood of $0$, and because multiples $aV$ (for $a > 0$) form a base for the neighborhood system of $0$, $V$ is bounded: for any neighborhood $W$ of $0$, there exists $a > 0$ with $aV \subset W$, so $V \subset a^{-1}W$.

If the space is Hausdorff in addition to being pseudo-normable, then $p(x) = 0$ implies that $x$ belongs to every neighborhood of $0$, so by the Hausdorff property $x = 0$. Thus $p$ is a norm and the space is normable.
