---
role: proof
locale: en
of_concept: invariant-factor-multiplicative-group
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

View the multiplicative group $F^*$ of the finite field $F$ as a $\mathbb{Z}$-module. Since $F^*$ is a finite abelian group, by the structure theorem for finitely generated modules over a principal ideal domain (here $\mathbb{Z}$), $F^*$ decomposes as a direct sum of cyclic submodules:
$$F^* \cong \mathbb{Z}/m_1\mathbb{Z} \oplus \mathbb{Z}/m_2\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/m_t\mathbb{Z},$$
where $m_1 \mid m_2 \mid \cdots \mid m_t$ are the invariant factors.

Let $m = m_t$ be the positive generator of the largest (or equivalently, the smallest in terms of the divisibility chain) invariant factor. For any $x \in F^*$, its annihilator ideal contains $m\mathbb{Z}$ because the order of every element divides $m_t$. Hence $x^m = 1$ for all $x \in F^*$.

Moreover, the element corresponding to a generator of the cyclic summand $\mathbb{Z}/m_t\mathbb{Z}$ has annihilator precisely $\mathbb{Z}m_t = \mathbb{Z}m$. Thus there exists $x_0 \in F^*$ such that $\operatorname{Ann}_{\mathbb{Z}}(x_0) = m\mathbb{Z}$, meaning $x_0$ has exact order $m$.
