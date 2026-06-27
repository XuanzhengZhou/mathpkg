---
role: proof
locale: en
of_concept: extension-of-uniformly-continuous-function
source_book: gtm027
source_chapter: "6"
source_section: "Completeness"
---

# Proof of Extension of Uniformly Continuous Functions to the Closure (Theorem 6.26)

**Theorem 6.26.** Let $f$ be a function whose domain is a subset $A$ of a uniform space $(X, \mathcal{U})$ and whose values lie in a complete Hausdorff uniform space $(Y, \mathcal{V})$. If $f$ is uniformly continuous on $A$, then there is a unique uniformly continuous extension $f^-$ of $f$ whose domain is the closure of $A$.

**Proof.** The function $f$ is viewed as a subset of $X \times Y$ (its graph). The desired extension $f^-$ is the closure of $f$ in $X \times Y$. That is, $(x,y) \in f^-$ if and only if there is a net in $A$ converging to $x$ such that the image net converges to $y$. The domain of $f^-$ is evidently the closure of $A$.

We first show that $f^-$ is a function (single-valued). Choose a closed symmetric $W \in \mathcal{V}$ with $W \circ W \subset V$ (for arbitrary $V \in \mathcal{V}$). By uniform continuity of $f$ on $A$, there exists an open symmetric $U \in \mathcal{U}$ such that $f[U[x] \cap A] \subset W[f(x)]$ for each $x \in A$.

Now suppose $(x,y)$ and $(x,z)$ belong to $f^-$. Then there are nets in $A$ converging to $x$ whose images converge to $y$ and $z$ respectively. For any open $U \in \mathcal{U}$ with $x \in U[x]$, there exists $a \in A$ such that $a \in U[x]$ and both image nets eventually land in $W[y]$ and $W[z]$. This implies $(y,z) \in W \circ W \subset V$ for every $V \in \mathcal{V}$. Since $Y$ is Hausdorff ($\bigcap \mathcal{V} = \Delta$), we have $y = z$. Thus $f^-$ is a function.

To show uniform continuity: let $W \in \mathcal{V}$ be given. Choose a closed symmetric $V \in \mathcal{V}$ with $V \circ V \subset W$, and choose an open symmetric $U \in \mathcal{U}$ such that $f[U[x] \cap A] \subset V[f(x)]$ for all $x \in A$. Take $(x,y), (u,v) \in f^-$ with $(x,u) \in U$. Since the intersection $U[x] \cap U[u]$ is open and non-empty, there exists $z \in A$ with $z \in U[x] \cap U[u]$. Then both $y$ and $v$ belong to the closure of $f[U[z] \cap A]$ in $Y$, which is contained in $\overline{V}[f(z)]$. Hence $(y,v) \in V \circ V \subset W$. This proves $f^-$ is uniformly continuous.

Uniqueness follows from the Hausdorff property of $Y$: any two continuous extensions agreeing on the dense subset $A$ must agree everywhere on the closure.
