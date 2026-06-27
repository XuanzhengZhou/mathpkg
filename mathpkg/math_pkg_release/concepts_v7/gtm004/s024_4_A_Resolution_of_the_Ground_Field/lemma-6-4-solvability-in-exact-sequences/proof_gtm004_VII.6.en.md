---
role: proof
locale: en
of_concept: lemma-6-4-solvability-in-exact-sequences
source_book: gtm004
source_chapter: "VII"
source_section: "6"
---

# Proof of Lemma 6.4: Solvability in Exact Sequences

**Lemma 6.4.** In the exact sequence $\mathfrak{h} \to \mathfrak{g} \to \mathfrak{g}/\mathfrak{h}$ of Lie algebras, $\mathfrak{g}$ is solvable if and only if $\mathfrak{h}$ and $\mathfrak{g}/\mathfrak{h}$ are solvable.

Recall that the derived series of a Lie algebra $\mathfrak{g}$ is defined by $\mathfrak{g}^{(0)} = \mathfrak{g}$, $\mathfrak{g}^{(n)} = [\mathfrak{g}^{(n-1)}, \mathfrak{g}^{(n-1)}]$, and $\mathfrak{g}$ is solvable if $\mathfrak{g}^{(n)} = \{0\}$ for some $n$.

**Proof.** $(\Rightarrow)$ If $\mathfrak{g}$ is solvable, then there exists $n$ such that $\mathfrak{g}^{(n)} = 0$. Since $\mathfrak{h} \subset \mathfrak{g}$, we have $\mathfrak{h}^{(n)} \subset \mathfrak{g}^{(n)} = 0$, so $\mathfrak{h}$ is solvable. The quotient map $\mathfrak{g} \to \mathfrak{g}/\mathfrak{h}$ sends $\mathfrak{g}^{(n)}$ to $(\mathfrak{g}/\mathfrak{h})^{(n)}$, so $(\mathfrak{g}/\mathfrak{h})^{(n)} = 0$ and $\mathfrak{g}/\mathfrak{h}$ is solvable.

$(\Leftarrow)$ Suppose $\mathfrak{h}$ and $\mathfrak{g}/\mathfrak{h}$ are solvable. Let $\mathfrak{h}^{(m)} = 0$ and $(\mathfrak{g}/\mathfrak{h})^{(n)} = 0$. The latter means $\mathfrak{g}^{(n)} \subset \mathfrak{h}$. Then

$$\mathfrak{g}^{(m+n)} = (\mathfrak{g}^{(n)})^{(m)} \subset \mathfrak{h}^{(m)} = 0.$$

Hence $\mathfrak{g}$ is solvable. $\square$
