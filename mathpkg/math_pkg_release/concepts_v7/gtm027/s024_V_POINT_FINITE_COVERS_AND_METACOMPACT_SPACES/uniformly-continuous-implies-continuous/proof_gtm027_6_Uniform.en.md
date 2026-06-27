---
role: proof
locale: en
of_concept: uniformly-continuous-implies-continuous
source_book: gtm027
source_chapter: "6"
source_section: "Uniform Spaces"
---

# Proof that Uniformly Continuous Implies Continuous (Theorem 6.9)

**Theorem 6.9.** Each uniformly continuous function is continuous relative to the uniform topology, and hence each uniform isomorphism is a homeomorphism.

**Proof.** Let $f$ be a uniformly continuous function on $(X, \mathcal{U})$ to $(Y, \mathcal{V})$ and let $W$ be a neighborhood of $f(x)$ in $Y$. Then there is $V$ in $\mathcal{V}$ such that $V[f(x)] \subset W$.

Now,

$$f^{-1}[V[f(x)]] = \{y \in X : f(y) \in V[f(x)]\} = \{y \in X : (f(x), f(y)) \in V\} = f_2^{-1}[V][x],$$

where $f_2(x,y) = (f(x), f(y))$. Since $f$ is uniformly continuous, $f_2^{-1}[V] \in \mathcal{U}$, and therefore $f_2^{-1}[V][x]$ is a neighborhood of $x$ in the uniform topology of $X$.

Thus $f^{-1}[W]$ contains a neighborhood of $x$, which means $f$ is continuous at $x$. Since $x$ was arbitrary, $f$ is continuous.

If $f$ is a uniform isomorphism, then both $f$ and $f^{-1}$ are uniformly continuous, hence both are continuous, so $f$ is a homeomorphism.
