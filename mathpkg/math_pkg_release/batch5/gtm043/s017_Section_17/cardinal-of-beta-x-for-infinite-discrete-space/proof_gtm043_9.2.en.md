---
role: proof
locale: en
of_concept: cardinal-of-beta-x-for-infinite-discrete-space
source_book: gtm043
source_chapter: "9"
source_section: "9.2"
---

For simplicity of notation, put $m = 2^{2|X|}$. The problem is to show that there are at least $m$ ultrafilters on $X$. We reduce the complexity of the notation by considering the following auxiliary sets: the set $F$ of all finite subsets $F$ of $X$, and the set $\Phi$ of all finite subsets $\varphi$ of $F$. We shall construct $m$ ultrafilters on $F \times \Phi$; since $F \times \Phi$ is equipotent with $X$ ($X$ being infinite), the results are equivalent.

With each (arbitrary) subset $S$ of $X$, associate a subset $b_S$ of $F \times \Phi$, as follows:
$$b_S = \{(F, \varphi) \in F \times \Phi : S \cap F \in \varphi\}.$$
For simplicity of notation, we shall denote the complement of $b_S$ in $F \times \Phi$ by $-b_S$.

Next, for each of the $m$ subsets $\mathcal{S}$ of the set of all subsets of $X$, define the family
$$\mathfrak{B}_{\mathcal{S}} = \{\mathfrak{b}_S : S \in \mathcal{S}\} \cup \{-\mathfrak{b}_S : S \notin \mathcal{S}\}.$$

Let $\mathfrak{b}_{S_1}, \cdots, \mathfrak{b}_{S_k}, -\mathfrak{b}_{S_{k+1}}, \cdots, -\mathfrak{b}_{S_n}$ be distinct members of $\mathfrak{B}_{\mathcal{S}}$. The indices $S_1, \cdots, S_n$ are distinct subsets of $X$. For $i < j$, choose a single element $x_{ij}$ that belongs to exactly one of $S_i, S_j$. The selected elements $x_{ij}$, for $1 \leq i < j \leq n$, form a finite subset $F$ of $X$. For $i < j$, the sets $S_i \cap F$ and $S_j \cap F$ are distinct, since exactly one of them contains $x_{ij}$. Now consider the finite set
$$\varphi = \{S_1 \cap F, \cdots, S_k \cap F\},$$
which is a member of $\Phi$. Trivially, $S_i \cap F \in \varphi$ for $i \leq k$, and $S_j \cap F \notin \varphi$ for $j > k$. Therefore $(F, \varphi) \in \mathfrak{b}_{S_i}$ for $i \leq k$, and $(F, \varphi) \in -\mathfrak{b}_{S_j}$ for $j > k$. This shows that $\mathfrak{B}_{\mathcal{S}}$ has the finite intersection property.

Each family $\mathfrak{B}_{\mathcal{S}}$ is embeddable, therefore, in at least one ultrafilter $\mathfrak{U}_{\mathcal{S}}$. Furthermore, distinct families cannot be contained in the same ultrafilter; for, if $S \in \mathcal{S} - \mathcal{S}'$, then $\mathfrak{B}_{\mathcal{S}}$ contains $\mathfrak{b}_S$, while $\mathfrak{B}_{\mathcal{S}'}$ contains its complement. Since there are $m$ sets $\mathcal{S}$, there are $m$ ultrafilters $\mathfrak{U}_{\mathcal{S}}$.
