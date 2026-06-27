---
role: proof
locale: en
of_concept: classification-of-irreducible-sl2-modules
source_book: gtm009
source_chapter: "II"
source_section: "7"
---

From Lemma 7.2(c) with $i = m+1$, if $v_m$ exists then $x.v_m$ would be a nonzero multiple of $v_{m+1}$, forcing more weight spaces. But $\dim V < \infty$, so the chain must terminate: there exists $m$ such that $v_m \neq 0$ but $v_{m+1} = 0$. Then $y.v_m = (m+1)v_{m+1} = 0$ by Lemma 7.2(b), and $x.v_{m+1} = 0$ gives $(\lambda - m)v_m = 0$ by Lemma 7.2(c) with $i = m+1$. Hence $\lambda = m$.

Thus the weight $\lambda$ must be a nonnegative integer, and the vectors $v_0, v_1, \ldots, v_m$ are nonzero. They are linearly independent since they lie in distinct weight spaces (eigenvalues $\lambda, \lambda-2, \ldots, \lambda-2m = -m$). The subspace spanned by $\{v_0, \ldots, v_m\}$ is stable under $x, y, h$ by Lemma 7.2, hence is an $L$-submodule. By irreducibility, this subspace equals $V$, so $\dim V = m+1$.

The uniqueness of the highest weight vector (up to scalar) follows since only the weight $m$ occurs with multiplicity 1 and every other weight $m-2i$ has $v_i$ as a basis vector, determined uniquely up to scaling by $v_0$.

For uniqueness of the module: any two irreducible modules of dimension $m+1$ have highest weight $m$, and the action formulas force an isomorphism sending the maximal vector of one to that of the other.
