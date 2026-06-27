---
role: proof
locale: en
of_concept: properties-of-canonical-embedding
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The proof proceeds by $\in$-induction on the well-founded relation.

**Part 1.** By definition, $[\![\check{x} \in \check{y}]\!] = \sum_{z \in \mathcal{D}(\check{y})} \check{y}(z) \cdot [\![z = \check{x}]\!]$. Since $\mathcal{D}(\check{y}) = \{\check{w} \mid w \in y\}$ and $\check{y}(\check{w}) = 1$ for all $w \in y$, we have:
$$[\![\check{x} \in \check{y}]\!] = \sum_{w \in y} [\![\check{w} = \check{x}]\!].$$

If $x \in y$, then one term in this sum is $[\![\check{x} = \check{x}]\!] = 1$ (by the induction hypothesis), so the sum equals $1$. If $x \notin y$, then for each $w \in y$, by the induction hypothesis $[\![\check{w} = \check{x}]\!] = 0$ (since $w \neq x$), so the sum equals $0$.

**Part 2.** By definition,
$$[\![\check{x} = \check{y}]\!] = \prod_{u \in \mathcal{D}(\check{x})} (\check{x}(u) \Rightarrow [\![u \in \check{y}]\!]) \cdot \prod_{v \in \mathcal{D}(\check{y})} (\check{y}(v) \Rightarrow [\![v \in \check{x}]\!])$$
$$= \prod_{u \in x} [\![\check{u} \in \check{y}]\!] \cdot \prod_{v \in y} [\![\check{v} \in \check{x}]\!].$$

If $x = y$, then by Part 1, $[\![\check{u} \in \check{y}]\!] = 1$ for all $u \in x$, and $[\![\check{v} \in \check{x}]\!] = 1$ for all $v \in y$, so the product equals $1$. If $x \neq y$, then (without loss of generality) there exists $u \in x$ with $u \notin y$, so $[\![\check{u} \in \check{y}]\!] = 0$ by Part 1, making the product $0$.

**Part 3.** For $u \in V^{(2)}$, since $B = 2 = \{0, 1\}$, the condition $u: \mathcal{D}(u) \to \{0, 1\}$ means $u$ is essentially the characteristic function of a set of $B$-valued sets. By induction on rank, each $x \in \mathcal{D}(u)$ with $u(x) = 1$ corresponds to a unique $\check{v}_x$ with $v_x \in V$. Defining $v = \{v_x \mid x \in \mathcal{D}(u), u(x) = 1\}$, we obtain $[\![u = \check{v}]\!] = 1$.
