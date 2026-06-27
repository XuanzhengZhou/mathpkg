---
role: proof
locale: en
of_concept: abelian-semigroup-amenable
source_book: gtm015
source_chapter: "3"
source_section: "29"
---

# Proof of Every abelian semigroup is amenable

Let $T$ be an abelian semigroup and let $p$ be the functional on $\mathcal{B} = \mathcal{B}_{\mathbb{R}}(T)$ constructed in Lemma (29.4). By the Hahn-Banach theorem (28.6), applied to the functional $p$ and the zero subspace of $\mathcal{B}$, there exists a linear form $f$ on $\mathcal{B}$ such that $f(x) \le p(x)$ for all $x \in \mathcal{B}$.

Then $f(x) \le p(x) \le \sup x$ for all $x \in \mathcal{B}$. Replacing $x$ by $-x$, we have $-f(x) \le p(-x) \le \sup(-x)$, therefore

$$\inf x = -\sup(-x) \le f(x) \le p(x) \le \sup x.$$

In particular, condition (ii) in the definition of an invariant mean (29.3) is verified.

If $x \in \mathcal{B}$ and $s \in T$, then by property (4) of $p$:

$$0 = -p(x_s - x) \le f(x - x_s) \le p(x - x_s) = 0,$$

therefore $f(x - x_s) = 0$, so $f(x_s) = f(x)$, which is condition (i) of (29.3). Thus $f$ is a right-invariant mean on $T$, proving that $T$ is amenable.
