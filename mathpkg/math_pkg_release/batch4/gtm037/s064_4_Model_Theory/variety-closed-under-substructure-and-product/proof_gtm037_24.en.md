---
role: proof
locale: en
of_concept: variety-closed-under-substructure-and-product
source_book: gtm037
source_chapter: "24"
source_section: ""
---
Say $\mathbf{K}$ is the class of all models of the set $\Gamma$ of identities. Obviously $\mathbf{K} \subseteq \mathbf{SK}$ and $\mathbf{K} \subseteq \mathbf{PK}$.

First, assume that $f: \mathfrak{A} \to \mathfrak{B} \in \mathbf{K}$ is an embedding and $[\sigma = \tau] \in \Gamma$. For any $x \in {}^{\omega}A$, using the fact that identities are universal closures of equations, we have $\sigma^{\mathfrak{B}}(f \circ x) = \tau^{\mathfrak{B}}(f \circ x)$ since $\mathfrak{B} \models [\sigma = \tau]$. Since $f$ is an embedding, this implies $\sigma^{\mathfrak{A}}x = \tau^{\mathfrak{A}}x$. Thus $[\sigma = \tau]$ holds in $\mathfrak{A}$, and it is an arbitrary member of $\Gamma$, so $\mathfrak{A} \in \mathbf{K}$.

Next, assume that $f: \mathfrak{A} \to \prod_{i \in I} \mathfrak{B}_i = \mathfrak{C}$ with $\mathfrak{B} \in {}^I\mathbf{K}$, and $[\sigma = \tau] \in \Gamma$. For any $x \in {}^{\omega}A$ and any $i \in I$ we have using 18.14:

$$[\sigma^{\mathfrak{C}}(f \circ x)]_i = \sigma^{\mathfrak{B}_i}(\mathrm{pr}_i \circ f \circ x) = \tau^{\mathfrak{B}_i}(\mathrm{pr}_i \circ f \circ x) = [\tau^{\mathfrak{C}}(f \circ x)]_i.$$

Since $i$ is arbitrary, $\sigma^{\mathfrak{C}}(f \circ x) = \tau^{\mathfrak{C}}(f \circ x)$. Then by 18.22 we have $\sigma^{\mathfrak{A}}x = \tau^{\mathfrak{A}}x$. Thus $[\sigma = \tau]$ holds in $\mathfrak{A}$. Hence $\mathfrak{A} \in \mathbf{K}$.
