---
role: proof
locale: en
of_concept: comma-category-creates-limits
source_book: gtm005
source_chapter: "V"
source_section: "6. Freyd's Adjoint Functor Theorem"
---

We show $Q$ creates products and equalizers; since limits are built from these, $Q$ creates all small limits.

**Products.** Let $J$ be a set (discrete category) and $f_j : x \rightarrow G a_j$ a $J$-indexed family of objects of $(x \downarrow G)$. Since $A$ is small-complete, the product $\prod a_j$ with projections $p_j : \prod a_j \rightarrow a_j$ exists in $A$. Because $G$ preserves products, $G p_j : G\prod a_j \rightarrow G a_j$ is a product diagram in $X$. Hence there is a unique arrow $f : x \rightarrow G\prod a_j$ such that $G p_j \circ f = f_j$ for all $j$. Then $p_j : f \rightarrow f_j$ is a cone in $(x \downarrow G)$, and it is the unique cone projecting under $Q$ to the given product cone $p_j$. One verifies it is a product diagram in $(x \downarrow G)$, so $Q$ creates products.

**Equalizers.** Let $s, t : f \rightarrow g$ be arrows in $(x \downarrow G)$, where $f : x \rightarrow G a$ and $g : x \rightarrow G b$. Their images under $Q$ are arrows $s, t : a \rightarrow b$ in $A$. Let $e : c \rightarrow a$ be the equalizer of $s$ and $t$ in $A$. Since $G$ preserves equalizers, $G e : G c \rightarrow G a$ is the equalizer of $G s$ and $G t$. Now $G s \circ f = G t \circ f = g$ (since $s, t$ are arrows in $(x \downarrow G)$), so there is a unique arrow $h : x \rightarrow G c$ with $G e \circ h = f$. This defines $e : h \rightarrow f$ as the unique arrow in $(x \downarrow G)$ with $Q$-projection $e$. To verify $e$ is an equalizer: given any $k : x \rightarrow G d$ and $r : k \rightarrow f$ in $(x \downarrow G)$ with $s \circ r = t \circ r$, applying $Q$ yields $s \circ r = t \circ r$ in $A$, so $r$ factors uniquely through $e$ via some $r' : d \rightarrow c$. Lifting back gives the unique factorization in $(x \downarrow G)$.

Thus $Q$ creates all small limits, and $(x \downarrow G)$ is small-complete when $A$ is.
