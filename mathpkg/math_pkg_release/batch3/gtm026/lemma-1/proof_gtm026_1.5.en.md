---
role: proof
locale: en
of_concept: lemma-1
source_book: gtm026
source_chapter: "1"
source_section: "5.33"
---

This is where we really use the algebra axioms. First of all, if $i:B \longrightarrow X$ is the inclusion map then clearly $B^*$ is just the image of $i\beta:B\beta \longrightarrow X\beta$, so that $B^*\xi$ is just $\langle B \rangle$ as in 4.31. In particular, $B \subset B^*\xi$ and $(B^*\xi)^*\xi = B^*\xi$. To show $B^*\xi$ is $\mathcal{T}$-closed, we must show, given

of 1.19 can be recaptured by setting $\Omega_n = \varnothing$ when $n$ is infinite and using only $\aleph_0$-ary equations. The category of $(\Omega, E)$-algebras is called an equationally-definable class.

5.35 The Lawvere Theory. Let $T$ be an algebraic theory in Set. If $T$ is bounded, the regular rank of $T$ is the smallest infinite regular cardinal greater than or equal to the rank of $T$. The Lawvere theory of $T$ is the category Law($T$) whose objects are $\{all$ cardinal numbers\} $\{all$ cardinal numbers less than the regular rank of $T\}$ accordingly as $T$ is unbounded or bounded. Thus, $\sup(m_i \in n) \in \text{Law}(T)$ whenever all $m_i$ and $n$ are. A morphism $\alpha: m \longrightarrow n$ in Law($T$) is a morphism $\alpha:n \longrightarrow m$ in $\text{Set}_T$ (see 3.2), that is a function $\alpha:n \longrightarrow mT$ (Notice how we use different types of arrows to identify which category we mean). Composition and identities are defined just as in $\text{Set}_T$, specifically

$$\begin{align*}
(m \xrightarrow{\alpha} n) * (n \xrightarrow{\beta} p) &= (p \xrightarrow{\beta} n) \circ (n \xrightarrow{\alpha} m) \\
&= p \xrightarrow{\beta} nT \xrightarrow{\alpha T} mTT \xrightarrow{m\mu} mT
\end{align*}$$

(where $*$ denotes the composition operation in Law($T$)), and $n\eta:n \longrightarrow n$ provides the identities. Since $\text{Set}_T$ is a category, so is Law($T$).

Our definition of a $T$-algebra has so far stressed the monoid form $(T, \eta, \mu)$ of $T$. We now show how to express 4.9 and 4.10 referring only to the clone form $(T, \eta

To prove this, 5.7 tells us we have only to check equality of the values assigned by the $m$th components to $id_m$. Indeed, $\langle id_m, (m\hat{\alpha}_i : i \in n).mT\hat{\beta}.m\mu \rangle = \langle \alpha : n \longrightarrow mT, mT\hat{\beta}.m\mu \rangle = \langle \beta, \alpha T.m\mu \rangle = \beta \circ \alpha = \langle id_m, m(\beta \circ \alpha)^* \rangle$.

5.38 Remark. For any function $\xi : XT \longrightarrow X$, 4.10 is commutative restricted to the elements in the image of $(\emptyset \longrightarrow XT)T$ (that is, restricted to the interpretation in $(XTT, XT\mu)$ of the true constants). To prove this, one need only observe that $(\emptyset \longrightarrow XT)T.X\mu$ and $(\emptyset \longrightarrow XT).\xi T$ are already equal, both being the unique $T$-homomorphism $(\emptyset T, \emptyset\mu) \longrightarrow (XT, X\mu)$.

Now consider the following diagram induced by $\alpha : m \longrightarrow n$ and $\beta : n \longrightarrow p$:

$$
\begin{array}{c}
X^m \\
(X\hat{\alpha}_i) \\
XT^n \\
(XT\hat{\beta}_j) \\
XT^p \\
(X\mu)^p \\
XT^p \\
(X^p)
\end{array}
$$

The two boundary paths from $X^m$ to $X^p$ are equal precisely when $M_\xi$ preserves composition whereas III is equivalent to 4.10 (as $p$ can equal 1). I and II always commute (by 5.37 and the naturality of $\beta_j$). It is now clear that if 4.10 holds then $M_\xi$ preserves composition. Using 5.38, to prove the converse it is sufficient to show that given $\bar{x} \in X

We are now ready to prove the extension of 4.25 to infinitary algebraic theories. Rather than relying on a Birkhoff variety argument, we will present the operations and equations explicitly and prove that they work. In particular, this provides a different (and more informative) proof of 4.25.
