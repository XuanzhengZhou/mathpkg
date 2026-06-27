---
role: proof
locale: en
of_concept: models-with-many-automorphisms
source_book: gtm037
source_chapter: "27"
source_section: "Indiscernibles and the Ehrenfeucht-Mostowski Theorem"
---

**Proof of Corollary 27.19.**

By the Ehrenfeucht--Mostowski theorem (Theorem 27.17), it suffices to construct a simple ordering structure $\mathfrak{A} = \langle A, \leq \rangle$ of power $\mathfrak{m}$ with $2^{\mathfrak{m}}$ automorphisms. Take $A = \mathfrak{m} \times [0,1)_{\mathbb{Q}}$, ordered lexicographically: $(\alpha, r) < (\beta, s)$ iff $\alpha < \beta$, or $\alpha = \beta$ and $r < s$. In the notation of the theory of ordered sets, this linear order has type $(1 + \eta) \cdot \mathfrak{m}$; one replaces each ordinal $\alpha < \mathfrak{m}$ by a copy of the rationals in $[0, 1)$.

Let $F = \{ f \in {}^\mathfrak{m}2 : f\alpha = 0 \text{ for every limit ordinal } \alpha < \mathfrak{m} \}$. Clearly $|F| = 2^\mathfrak{m}$. With every $f \in F$ we associate an automorphism $g_f$ of $\mathfrak{A} = \langle A, \leq \rangle$, as follows. Take any $(\alpha, r) \in A$. Write $\alpha = \beta + m$, where $\beta$ is a limit ordinal and $m \in \omega$. Define $g_f(\alpha, r)$ according to the values of $f$ on $\alpha$ and $\alpha+1$:

*Case 1.* $f\alpha = 0$, $f(\alpha+1) = 0$:
$$g_f(\alpha,r) = (\beta + 2m, \; 2r) \quad\text{if } 0 \leq r < 1/2,$$
$$g_f(\alpha,r) = (\beta + 2m + 1, \; 2(r - 1/2)) \quad\text{if } 1/2 \leq r < 1.$$

*Case 2.* $f\alpha = 0$, $f(\alpha+1) = 1$:
$$g_f(\alpha,r) = (\beta + 2m, \; 3r) \quad\text{if } 0 \leq r < 1/3,$$
$$g_f(\alpha,r) = (\beta + 2m + 1, \; 3(r - 1/3)) \quad\text{if } 1/3 \leq r < 2/3,$$
$$g_f(\alpha,r) = (\beta + 2m + 2, \; 3(r - 2/3)) \quad\text{if } 2/3 \leq r < 1.$$

*Case 3.* $f\alpha = 1$, $f(\alpha+1) = 0$: an analogous piecewise linear map splitting the interval $[0,1)$ into three parts, mapping to ordinals $\beta+2m$, $\beta+2m+1$, $\beta+2m+2$.

*Case 4.* $f\alpha = 1$, $f(\alpha+1) = 1$: an analogous piecewise linear map splitting into four parts.

One verifies that each $g_f$ is order-preserving and bijective, hence an automorphism of $\mathfrak{A}$. Moreover, if $f \neq f'$, then for the least $\alpha$ where they differ, say $f\alpha = 0$ and $f'\alpha = 1$, the images of $(\alpha, 0)$ under $g_f$ and $g_{f'}$ have distinct first coordinates (differing by 1), so $g_f \neq g_{f'}$. Thus $|\mathrm{Aut}(\mathfrak{A})| \geq |F| = 2^\mathfrak{m}$. Since there are at most $|A|^{|A|} = \mathfrak{m}^\mathfrak{m} = 2^\mathfrak{m}$ functions from $A$ to $A$, we have $|\mathrm{Aut}(\mathfrak{A})| = 2^\mathfrak{m}$.

Now apply Theorem 27.17 with this $\mathfrak{A}$. We obtain a model $\mathfrak{B}$ of $\Gamma$ such that $\mathfrak{A}$ is homogeneous for $\mathfrak{B}$ and every automorphism of $\mathfrak{A}$ extends to an automorphism of $\mathfrak{B}$. Hence $|\mathrm{Aut}(\mathfrak{B})| \geq |\mathrm{Aut}(\mathfrak{A})| = 2^\mathfrak{m}$, and condition (iii) of the theorem gives $|B| \leq |\mathrm{Fmla}_{\mathfrak{B}}| + \mathfrak{m} = \mathfrak{m}$. By the downward L\"owenheim--Skolem theorem we may assume $|B| = \mathfrak{m}$. Thus $\mathfrak{B}$ is the desired model.
