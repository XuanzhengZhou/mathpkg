---
role: proof
locale: en
of_concept: irreducible-ideal-is-primary-in-acc-ring
source_book: gtm028
source_chapter: "IV"
source_section: "§4. The Lasker-Noether decomposition theorem"
---

Let $\mathfrak{a}$ be an ideal of $R$ and suppose it is not primary. Then there exist elements $b, c \in R$, not in $\mathfrak{a}$, such that $bc \in \mathfrak{a}$ and no power of $b$ lies in $\mathfrak{a}$.

The ideals $\{\mathfrak{a} : (b^s)\}$ form an increasing sequence. By the a.c.c., there exists $n$ such that $\mathfrak{a} : (b^n) = \mathfrak{a} : (b^{n+1})$. We claim that
$$\mathfrak{a} = (\mathfrak{a} + Rb^n) \cap (\mathfrak{a} + Rc).$$

The right-hand side clearly contains $\mathfrak{a}$. Conversely, if $x$ belongs to the right-hand side, then
$$x = u + yb^n = v + zc + mc \quad (u, v \in \mathfrak{a}, y, z \in R, m \in \mathbb{Z}).$$

Since $bc \in \mathfrak{a}$, we have $bx \in \mathfrak{a}$, so $yb^{n+1} \in \mathfrak{a}$. From $\mathfrak{a} : (b^n) = \mathfrak{a} : (b^{n+1})$ we deduce $yb^n \in \mathfrak{a}$, hence $x \in \mathfrak{a}$.

Now $\mathfrak{a} + Rc > \mathfrak{a}$ since $c \notin \mathfrak{a}$, and $\mathfrak{a} + Rb^n > \mathfrak{a}$ since $b^{n+1} \in Rb^n$ but $b^{n+1} \notin \mathfrak{a}$. Thus $\mathfrak{a}$ is not irreducible.
