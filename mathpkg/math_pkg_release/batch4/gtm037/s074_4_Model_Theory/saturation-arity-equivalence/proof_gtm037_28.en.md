---
role: proof
locale: en
of_concept: saturation-arity-equivalence
source_book: gtm037
source_chapter: "28"
source_section: "Saturated Structures"
---

**Proof of Proposition 28.2.**

Obviously $(ii) \Rightarrow (i)$, since condition (ii) applies to all formulas while (i) restricts to formulas with a single free variable.

Now assume $(i)$ and the hypothesis of $(ii)$. We may assume that $\Delta$ is closed under conjunction. For each $\varphi \in \Delta$ choose $m_\varphi$ such that $\mathrm{Fv}\,\varphi \subseteq \{v_0, \ldots, v_{m_\varphi}\}$.

We define $a \in {}^\omega A$ by recursion. Suppose that $a \upharpoonright i$ has been defined in such a way that each formula
$$\exists v_i \cdots \exists v_{m_\varphi}\, \varphi(c_{a_0}, \ldots, c_{a_{i-1}}, v_i, \ldots, v_{m_\varphi}), \quad \varphi \in \Delta,$$
holds in $(\mathfrak{A}, x, a_j)_{x \in X,\, j < i}$. This is clearly true for $i = 0$ (with the existential quantifiers ranging over all of $v_0, \ldots, v_{m_\varphi}$, the formulas hold by the consistency hypothesis of $(ii)$).

Now let $\Theta$ be the set of all formulas
$$\exists v_{i+1} \cdots \exists v_{m_\varphi}\, \varphi(c_{a_0}, \ldots, c_{a_{i-1}}, v_i, \ldots, v_{m_\varphi})$$
with $\varphi \in \Delta$. Thus
$$|X \cup \{a_j : j < i\}| < \mathfrak{m},$$
and $\Theta$ is a set of formulas $\psi$ with $\mathrm{Fv}\,\psi \subseteq \{v_i\}$.

If $\Theta'$ is a finite subset of $\Theta$, we may write
$$\Theta' = \{\exists v_{i+1} \cdots \exists v_{m_\varphi}\, \varphi(c_{a_0}, \ldots, c_{a_{i-1}}, v_i, \ldots, v_{m_\varphi}) : \varphi \in \Delta'\},$$
where $\Delta'$ is a finite subset of $\Delta$. Now $\bigwedge \Delta' \in \Delta$ (since $\Delta$ is closed under conjunction), so by the induction hypothesis, the formula
$$\exists v_i \cdots \exists v_{m_{\bigwedge\Delta'}}\, \bigwedge\Delta'(c_{a_0}, \ldots, c_{a_{i-1}}, v_i, \ldots)$$
holds in the expanded structure. This means there exists some $a_i \in A$ satisfying all formulas in $\Theta'$ simultaneously. Since this holds for every finite $\Theta' \subseteq \Theta$, the set $\Theta$ is finitely satisfiable.

By condition $(i)$ (applied with the parameter set $X \cup \{a_j : j < i\}$, whose cardinality is less than $\mathfrak{m}$), there exists $a_i \in A$ such that every formula in $\Theta$ holds at $a_i$. This extends the recursion by defining $a_i$.

Proceeding by induction, we obtain $a \in {}^\omega A$ such that for each $\varphi \in \Delta$ and each $i \leq m_\varphi$, the relevant existentially quantified formula holds. In particular, when $i = m_\varphi$, the formula reduces to $\varphi(c_{a_0}, \ldots, c_{a_{m_\varphi-1}})$, which therefore holds in the expanded structure. Hence $(\mathfrak{A}, x)_{x \in X} \models \varphi[a]$ for all $\varphi \in \Delta$, establishing $(ii)$.
