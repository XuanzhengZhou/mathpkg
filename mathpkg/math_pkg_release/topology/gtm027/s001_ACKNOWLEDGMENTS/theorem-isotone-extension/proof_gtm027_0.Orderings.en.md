---
role: proof
locale: en
of_concept: theorem-isotone-extension
source_book: gtm027
source_chapter: "0"
source_section: "Orderings"
---

# Proof of Theorem 10: Isotone Extension of Functions on Chains

**Necessity.** If $f$ has an isotone extension $f^-$ whose domain is $X$, and if $A$ is a subset of $X_0$ which is order-bounded in $X$ (say $a \leq x \leq b$ for all $x \in A$, with $a,b \in X$), then by isotonicity of $f^-$ we have $f^-(a) \leq f^-(x) \leq f^-(b)$ for all $x \in A$. Since $f^-$ agrees with $f$ on $X_0$, it follows that $f[A]$ is order-bounded in $Y$ (by $f^-(a)$ and $f^-(b)$). Hence the condition is necessary.

**Sufficiency.** Assume that $f$ carries order-bounded subsets of $X_0$ (order-bounded in $X$) into order-bounded subsets of $Y$. We must construct an isotone extension $f^-$ of $f$ with domain $X$.

First we note that if $A$ is a subset of $X_0$ which has a lower bound in $X$, then $f[A]$ has a lower bound. For, choosing a point $x$ in $A$, the set $\{y : y \in A \text{ and } y \leq x\}$ is order-bounded (it is bounded below by the lower bound of $A$ and above by $x$), hence its image under $f$ is order-bounded, and a lower bound for this image is also a lower bound for $f[A]$. A similar statement applies to upper bounds.

Now, for each $x$ in $X$ let $L_x$ be the set of all members of $X_0$ which are less than or equal to $x$; that is, $L_x = \{y : y \leq x \text{ and } y \in X_0\}$. There are two cases:

- If $L_x$ is void, then $x$ is a lower bound for $X_0$. By the observation above, $f[X_0]$ has an infimum $v$, and we define $f^-(x) = v$.

- If $L_x$ is not void, then $x$ is an upper bound for $L_x$, so by the observation above the set $f[L_x]$ has an upper bound and hence (since $Y$ is order-complete) a supremum. We define $f^-(x) = \sup f[L_x]$.

The function $f^-$ so defined is an isotone extension of $f$:
- If $x \in X_0$, then $x \in L_x$ and $x$ is an upper bound of $L_x$, so $f(x) = \sup f[L_x] = f^-(x)$. Hence $f^-$ extends $f$.
- If $x \leq z$ in $X$, then $L_x \subset L_z$, so $\sup f[L_x] \leq \sup f[L_z]$, i.e., $f^-(x) \leq f^-(z)$. Hence $f^-$ is isotone.

Thus $f$ has an isotone extension if and only if it carries order-bounded sets into order-bounded sets.
