---
role: proof
locale: en
of_concept: quotient-space-of-topological-group-is-homogeneous
source_book: gtm027
source_chapter: "3"
source_section: "U"
---

# Proof of Quotient space of a topological group by a subgroup is a homogeneous space

Let $G$ be a topological group and $H$ a subgroup. Let $G/H = \{xH : x \in G\}$ be the family of left cosets, endowed with the quotient topology induced by the natural projection $\pi: G \to G/H$, $\pi(x) = xH$.

We must show that $G/H$ is homogeneous: for any two cosets $A, B \in G/H$, there exists a homeomorphism $\varphi: G/H \to G/H$ with $\varphi(A) = B$.

---

**Step 1: Left translation is well-defined.** Fix $a \in G$ and define $L_a: G/H \to G/H$ by

$$L_a(xH) = (ax)H.$$

If $xH = yH$, then $y^{-1}x \in H$. Applying $L_a$,

$$(ay)^{-1}(ax) = y^{-1}a^{-1}ax = y^{-1}x \in H,$$

hence $(ax)H = (ay)H$. Thus $L_a$ is well-defined.

---

**Step 2: Left translation is a homeomorphism.** Consider the diagram

$$\begin{CD}
G @>{a\cdot(-)}>> G \\
@V{\pi}VV @VV{\pi}V \\
G/H @>>{L_a}> G/H
\end{CD}$$

The top map $x \mapsto ax$ is left multiplication by $a$, which is a homeomorphism of $G$ (since $G$ is a topological group). The composed map $\pi \circ (a \cdot (-)): G \to G/H$ is continuous. Since $\pi$ is a quotient map, the induced map $L_a$ on $G/H$ is continuous.

The inverse of $L_a$ is $L_{a^{-1}}$, because for any $xH \in G/H$,

$$L_{a^{-1}}(L_a(xH)) = L_{a^{-1}}((ax)H) = (a^{-1}ax)H = xH.$$

By the same argument, $L_{a^{-1}}$ is continuous. Therefore $L_a$ is a homeomorphism of $G/H$ onto itself.

---

**Step 3: Transitivity.** Let $A = xH$ and $B = yH$ be arbitrary cosets. Set $a = yx^{-1}$. Then

$$L_a(A) = L_a(xH) = (yx^{-1}x)H = yH = B.$$

Thus $G$ acts transitively on $G/H$ by homeomorphisms, and $G/H$ is a homogeneous space. $\square$
