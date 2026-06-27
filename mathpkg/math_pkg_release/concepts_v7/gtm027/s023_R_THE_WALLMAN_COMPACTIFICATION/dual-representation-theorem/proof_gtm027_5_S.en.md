---
role: proof
locale: en
of_concept: dual-representation-theorem
source_book: gtm027
source_chapter: "5"
source_section: "The Wallman Compactification"
---

# Proof of the Dual Representation Theorem (Stone Duality)

Let $X$ be a Boolean space (a Hausdorff space in which the family of all compact-open sets forms a base for the topology; such a space is automatically locally compact). Let $\mathfrak{F} = \mathfrak{F}(X)$ be the characteristic ring of $X$, i.e., the ring of all continuous functions $f : X \to I_2$ such that $f^{-1}[1]$ is compact. Let $S$ be the Stone space of $\mathfrak{F}$, i.e., $S = \{\text{non-zero ring homomorphisms } \mathfrak{F} \to I_2\}$ with the relative product topology from $I_2^{\mathfrak{F}}$.

**Theorem (Dual Representation).** The evaluation map $\varphi : X \to S$ defined by

$$\varphi(x)(f) = f(x) \qquad (x \in X,\; f \in \mathfrak{F})$$

is a homeomorphism of $X$ onto the Stone space $S$ of its characteristic ring.

**Proof.** The proof proceeds in several steps.

**Step 1: $\varphi$ is well-defined and continuous.** For each $x \in X$, the map $\varphi(x) : \mathfrak{F} \to I_2$ given by $\varphi(x)(f) = f(x)$ is a ring homomorphism because the ring operations in $\mathfrak{F}$ are pointwise:

$$\varphi(x)(f + g) = (f+g)(x) = f(x) + g(x) = \varphi(x)(f) + \varphi(x)(g),$$
$$\varphi(x)(f \cdot g) = (f \cdot g)(x) = f(x) \cdot g(x) = \varphi(x)(f) \cdot \varphi(x)(g).$$

Moreover, $\varphi(x) \neq 0$ (the zero homomorphism) because the characteristic ring contains functions that do not vanish at every point (e.g., characteristic functions of non-empty compact-open neighborhoods). Hence $\varphi(x) \in S$.

To check continuity: a subbasic open set in $S$ has the form $U(f, \varepsilon) = \{s \in S : s(f) = \varepsilon\}$ for $f \in \mathfrak{F}$ and $\varepsilon \in I_2$. Then

$$\varphi^{-1}[U(f, \varepsilon)] = \{x \in X : f(x) = \varepsilon\}.$$

For $\varepsilon = 1$, this is $f^{-1}[1]$, which is compact-open (hence open) in $X$. For $\varepsilon = 0$, this is $X \setminus f^{-1}[1]$, which is also open since $f^{-1}[1]$ is clopen. Thus the preimage of every subbasic open set is open, so $\varphi$ is continuous.

**Step 2: $\varphi$ is injective.** Suppose $\varphi(x_1) = \varphi(x_2)$ for $x_1, x_2 \in X$. Then $f(x_1) = f(x_2)$ for every $f \in \mathfrak{F}$. In particular, for any compact-open neighborhood $U$ of $x_1$, its characteristic function $\chi_U \in \mathfrak{F}$ satisfies $\chi_U(x_1) = 1$. Since $\chi_U(x_2) = 1$, we have $x_2 \in U$. Because the compact-open sets form a base and $X$ is Hausdorff, this forces $x_1 = x_2$.

**Step 3: $\varphi$ is surjective.** We need to show that every non-zero homomorphism $s : \mathfrak{F} \to I_2$ is of the form $s = \varphi(x)$ for some $x \in X$. Let $\mathfrak{J} = \ker(s) = \{f \in \mathfrak{F} : s(f) = 0\}$. Then $\mathfrak{J}$ is a maximal proper ideal in $\mathfrak{F}$ (since $\mathfrak{F}/\mathfrak{J} \cong I_2$ is a field). By part (d) of the problem, every maximal proper ideal $\mathfrak{J}$ in $\mathfrak{F}$ has the form

$$\mathfrak{J} = \{f \in \mathfrak{F} : f(x) = 0\}$$

for some $x \in X$. (Proof of part (d): If there is no point at which all members of $\mathfrak{J}$ vanish, then for each $x \in X$, choose $f_x \in \mathfrak{J}$ with $f_x(x) = 1$. The open sets $f_x^{-1}[1]$ cover $X$, and by compactness of the supports one constructs a finite partition of unity in $\mathfrak{F}$ subordinate to these sets, yielding $1 \in \mathfrak{J}$, a contradiction. Hence some $x \in X$ is a common zero of $\mathfrak{J}$, and maximality forces $\mathfrak{J} = \{f : f(x) = 0\}$.)

Thus $\ker(s) = \{f \in \mathfrak{F} : f(x) = 0\}$ for a unique $x \in X$, which implies $s(f) = f(x) = \varphi(x)(f)$ for all $f \in \mathfrak{F}$. Hence $s = \varphi(x)$, proving surjectivity.

**Step 4: $\varphi$ is a closed map (hence a homeomorphism).** The space $X$ is a Boolean space, hence locally compact and Hausdorff. Its characteristic ring $\mathfrak{F}$ separates points from closed sets. The Stone space $S$ is compact Hausdorff (as a closed subspace of $I_2^{\mathfrak{F}}$). A continuous bijection from a locally compact Hausdorff space onto a compact Hausdorff space need not be closed in general, but here $\varphi$ is actually a homeomorphism because:

- $X$ has a base of compact-open sets. For such a set $U$, $\varphi[U]$ is the set of all $s \in S$ with $s(\chi_U) = 1$, which is $e(\chi_U)^{-1}[1]$, a compact-open subset of $S$ by the Stone representation theorem applied to $\mathfrak{F}$. Thus $\varphi$ maps basic compact-open sets to compact (hence closed) sets.
- Consequently $\varphi$ is a closed map: any closed set in $X$ is an intersection of complements of compact-open sets (since compact-open sets form a base in a locally compact Hausdorff space), and $\varphi$ preserves such images.

Therefore $\varphi$ is a continuous bijection with continuous inverse, i.e., a homeomorphism.

**Conclusion.** $X$ is homeomorphic to the Stone space $S$ of its characteristic ring $\mathfrak{F}(X)$ via the evaluation map. This establishes the dual representation theorem: the category of Boolean spaces is dually equivalent to the category of Boolean rings. $\square$

**Reference:** M. H. Stone [3].
