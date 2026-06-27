---
role: proof
locale: en
of_concept: pbw-basis-of-universal-enveloping-algebra
source_book: gtm004
source_chapter: "VII"
source_section: "1. Lie Algebras and their Universal Enveloping Algebra"
---

# Proof of PBW Basis of the Universal Enveloping Algebra

**Corollary 1.4.** Let $\mathfrak{h}$ be a Lie subalgebra of $\mathfrak{g}$ and let $J'$ be an ordered basis of $\mathfrak{h}$. Choose an ordered basis $J$ of $\mathfrak{g}$ such that the elements of $J'$ precede the elements of $J \setminus J'$ and such that the ordering on $J'$ coincides with the ordering induced from $J$. Then the elements

$$e_{i_1} e_{i_2} \cdots e_{i_k}$$

for all finite increasing sequences $i_1 \leq i_2 \leq \cdots \leq i_k$ in $J$ form a basis of $U\mathfrak{g}$ as an $\mathfrak{h}$-module (where $\mathfrak{h}$ acts by left multiplication on $U\mathfrak{g}$ via the embedding $U\mathfrak{h} \hookrightarrow U\mathfrak{g}$).

**Proof.** By Theorem 1.2 (the Birkhoff--Witt Theorem), the monomials

$$e_{i_1} e_{i_2} \cdots e_{i_k}$$

with $i_1 \leq i_2 \leq \cdots \leq i_k$ ranging over all finite increasing sequences in $J$ form a $K$-basis of $U\mathfrak{g}$.

Now let us analyze the action of $\mathfrak{h}$. We impose the ordering on $J$ as described: elements of $J'$ (the basis of $\mathfrak{h}$) come first, followed by the remaining basis elements. That is, for $i \in J'$ and $j \in J \setminus J'$, we set $i < j$. On $J'$, the ordering is inherited from $J$.

Under this ordering, any monomial $e_{i_1} \cdots e_{i_k}$ with $i_1 \leq \cdots \leq i_k$ can be written as a product of the form

$$h \cdot e_{j_1} \cdots e_{j_\ell}$$

where $h = e_{i_1} \cdots e_{i_r}$ is a PBW monomial in the basis elements of $\mathfrak{h}$ (i.e., indices from $J'$) and $j_1, \ldots, j_\ell$ are indices from $J \setminus J'$ in increasing order. The element $h$ lies in $U\mathfrak{h}$, which acts on $U\mathfrak{g}$ by left multiplication via the natural inclusion $U\mathfrak{h} \hookrightarrow U\mathfrak{g}$.

Since the PBW monomials form a $K$-basis of $U\mathfrak{g}$, and the $K$-basis of $U\mathfrak{h}$ is given by the PBW monomials in $J'$, it follows that the monomials $e_{j_1} \cdots e_{j_\ell}$ (for $j_1 \leq \cdots \leq j_\ell$ in $J \setminus J'$) form a basis of $U\mathfrak{g}$ as a left $U\mathfrak{h}$-module, i.e., as an $\mathfrak{h}$-module. More precisely, the set

$$\{ e_{i_1} \cdots e_{i_k} \mid i_1 \leq \cdots \leq i_k \text{ in } J \}$$

is $K$-linearly independent and spans $U\mathfrak{g}$. Restricting the leading factor to $\mathfrak{h}$ and the remaining factors to $J \setminus J'$ gives the desired $\mathfrak{h}$-module basis. $\square$
