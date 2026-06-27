---
role: proof
locale: en
of_concept: transitivity-of-free-extensions
source_book: gtm006
source_chapter: "11"
source_section: "3. Generation"
---

That (b) and (c) imply (a) is trivial: if $\mathcal{C}$ is a free extension of $\mathcal{B}$ and $\mathcal{B}$ is a free extension of $\mathcal{A}$, then composing the free extension steps yields that $\mathcal{C}$ is a free extension of $\mathcal{A}$.

Now suppose (a) and (c) are true: $\mathcal{C}$ is a free extension of $\mathcal{A}$ and $\mathcal{B}$ is a free extension of $\mathcal{A}$. We must show $\mathcal{C}$ is a free extension of $\mathcal{B}$.

Let $\mathcal{D}$ be a maximal free extension of $\mathcal{B}$ such that $\mathcal{D} < \mathcal{C}$. We claim $\mathcal{D} = \mathcal{C}$. Suppose not, so $\mathcal{D} 
eq \mathcal{C}$. Then the addition of any element of $\mathcal{C}$ not in $\mathcal{D}$ must result in a configuration that is not a free extension of $\mathcal{B}$, hence not of $\mathcal{D}$.

Choose an element $X$ in $\mathcal{C}$ but not in $\mathcal{D}$ of minimal $\mathcal{A}$-stage. Let $\mathcal{D}_1$ be the configuration obtained by adding $X$ to $\mathcal{D}$ with its incidences in $\mathcal{C}$. Since $X$ has minimal $\mathcal{A}$-stage among elements not in $\mathcal{D}$, all elements incident with $X$ in $\mathcal{C}$ must already be in $\mathcal{D}$ (they have strictly smaller $\mathcal{A}$-stage). Since $\mathcal{C}$ is a free extension of $\mathcal{A}$, $X$ has exactly two incidences in $\mathcal{C}$, and these two elements are in $\mathcal{D}$. Thus $\mathcal{D}_1$ would be a free one-step extension of $\mathcal{D}$, hence a free extension of $\mathcal{B}$, contradicting the maximality of $\mathcal{D}$. Therefore $\mathcal{D} = \mathcal{C}$, establishing (b).

The case where (a) and (b) imply (c) is handled similarly by symmetry, considering maximal free extensions of $\mathcal{A}$ contained in $\mathcal{B}$.
