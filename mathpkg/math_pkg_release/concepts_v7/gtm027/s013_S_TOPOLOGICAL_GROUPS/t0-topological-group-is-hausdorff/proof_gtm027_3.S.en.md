---
role: proof
locale: en
of_concept: t0-topological-group-is-hausdorff
source_book: gtm027
source_chapter: "3"
source_section: "S"
---

# Proof that a $T_0$ Topological Group is Hausdorff

**Statement.** A topological group is a Hausdorff space (i.e., $T_2$) whenever it is a $T_0$-space.

**Proof.** Recall that a space is $T_0$ if for any two distinct points $x \neq y$, there exists a neighborhood of one that does not contain the other. A space is Hausdorff ($T_2$) if for any two distinct points $x \neq y$, there exist disjoint neighborhoods separating them.

Let $G$ be a topological group and assume $G$ is $T_0$. Let $x, y \in G$ with $x \neq y$.

**Step 1: Translating to the identity.** Since $G$ is $T_0$, there exists (without loss of generality) a neighborhood $N$ of $x$ such that $y \notin N$. The left translation $L_{x^{-1}}: G \to G$, defined by $L_{x^{-1}}(z) = x^{-1} \cdot z$, is a homeomorphism (its inverse is $L_x$). Applying $L_{x^{-1}}$ to the neighborhood relation: $N$ is a neighborhood of $x$, so $x^{-1} \cdot N$ is a neighborhood of $x^{-1} \cdot x = e$, and $y \notin N$ implies $x^{-1} \cdot y \notin x^{-1} \cdot N$.

Set $a = x^{-1} \cdot y \neq e$ (since $x \neq y$), and let $U_0 = x^{-1} \cdot N$. Then $U_0$ is a neighborhood of $e$ with $a \notin U_0$.

**Step 2: Using continuity at the identity.** By the continuity of the map $\varphi(p, q) = p \cdot q^{-1}$ at $(e, e)$ (or equivalently, by applying proposition (b) at the identity), there exists a neighborhood $V$ of $e$ such that $V \cdot V^{-1} \subset U_0$. Since $V^{-1}$ is also a neighborhood of $e$ (inversion is a homeomorphism), we may replace $V$ by $V \cap V^{-1}$ to assume $V = V^{-1}$ and $V \cdot V \subset U_0$ (by possibly shrinking further).

**Step 3: Producing disjoint neighborhoods of $x$ and $y$.** Consider the neighborhoods $V \cdot x$ (of $x$) and $V \cdot y$ (of $y$). We claim they are disjoint.

Suppose, for contradiction, that there exists $z \in (V \cdot x) \cap (V \cdot y)$. Then $z = v_1 \cdot x = v_2 \cdot y$ for some $v_1, v_2 \in V$. This implies

$$
x^{-1} \cdot v_1^{-1} \cdot v_2 \cdot y = e \quad \Longrightarrow \quad x^{-1} \cdot y = v_1 \cdot v_2^{-1} \in V \cdot V^{-1} = V \cdot V \subset U_0.
$$

But $a = x^{-1} \cdot y \notin U_0$, contradiction. Hence $V \cdot x \cap V \cdot y = \varnothing$.

Therefore $G$ is Hausdorff.

**Alternative argument (as sketched in the text):** If $x \neq y$ and $G$ is $T_0$, then (without loss) there is a neighborhood of $x$ not containing $y$; i.e., $y \notin U \cdot x$ for some neighborhood $U$ of $e$. Then $y \cdot x^{-1} \notin U$ (equivalently, $x^{-1} \cdot y \notin U$). Choose a symmetric neighborhood $V$ of $e$ (so $V^{-1} = V$) with $V \cdot V \subset U$. Then $V \cdot x \cap V \cdot y = \varnothing$. Indeed, if $v_1 \cdot x = v_2 \cdot y$ with $v_1, v_2 \in V$, then $x^{-1} \cdot y = v_1^{-1} \cdot v_2 \in V^{-1} \cdot V = V \cdot V \subset U$, contradicting $x^{-1} \cdot y \notin U$. Thus $V \cdot x$ and $V \cdot y$ are disjoint neighborhoods of $x$ and $y$.

**Remark.** In fact, the proof shows that in a topological group, $T_0$ implies $T_1$ (since singleton sets are translates of $\{e\}$, and the above shows $\{e\}$ is closed when $G$ is $T_0$), and $T_0$ actually implies $T_{3\frac{1}{2}}$ (complete regularity). So separation axioms collapse in topological groups: $T_0 \iff T_1 \iff T_2 \iff T_{3\frac{1}{2}}$. ∎
