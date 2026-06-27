---
role: proof
locale: en
of_concept: corollary
source_book: gtm026
source_chapter: "1"
source_section: "1.50"
---

If $f$ is a coequalizer and $f$ is mono, $f.id = f.id.f$ are two coequalizer-mono factorizations of $f$, giving rise to $f^{-1}$ as above.

Examples such as 1.38 and 1.40 show that a morphism which is epi and mono need not be an isomorphism.

$\mathcal{K}$ has coequalizer-mono factorizations if every morphism in $\mathcal{K}$ has a coequalizer-mono factorization. For example

which case $i$ is continuous and $(p, i)$ is a coequalizer-mono factorization of $f$, or we can provide $\text{Im}(f)$ with the subspace topology induced by $i$, in which case $p$ is continuous and $(p, i)$ is an epi-equalizer factorization. The details are left as exercises.

A well-known way to construct the image factorization of a function $f: A \longrightarrow B$ is to divide out by the equivalence relation, $E$, of $f$ (where $E$ is the equivalence relation on $A$ given by $E = \{(x, y): xf = yf\}$). Let $p$ be the canonical projection as shown. Since $xEy$ if and only if $xf = yf$, $(xE)i = xf$ is a well-defined injection. Thus $f = p.i$ is a coequalizer-mono factorization of $f$. We now explore the possibility that this construction can be imitated in $\mathcal{H}$.

Consider a diagram scheme $\Delta$ with three nodes $i, j, k$ and just two edges, $\alpha \in \Delta (i, k)$ and $\beta \in \Delta (j, k)$. A diagram $(\Delta, D)$ in $\mathcal{H}$ looks like

(i.e., $D_\alpha = f$ and $D_\beta = g$). Since $\{i, j\}$ is final, $\lim D$ is an object $P$ of $\mathcal{H}$ equipped with two morphisms $a: P \longrightarrow A$ and $b: P \longrightarrow B$ such that $a.f = b.g$, and universal with this property as shown below:

The square $a.f = b.g$ is called a pullback square, $(P, a, b)$ is the pullback of $(f, g, C)$ and $b$ is the pullback of $f$ along $g$. (The dual concept is called a pushout.) In Set, $P$ is constructed as the subset $\{(a, b): af = bg\}$ of $A \times B$ with $a$ and $b$ the restrictions of the coordinate projections. In particular, if $f = g$, $P$ is the equivalence relation of $f$. In this case, a glance at 1.30 shows that the canonical projection $C \longrightarrow C/P$ is the coequalizer of $(a, b)$.

Consider a morphism $f: A \longrightarrow B$ in $\mathcal{H}$. The kernel pair of $f$ is the pullback $(E, a, b)$ of $(f, f, B)$. Let us assume that this kernel pair exists and that $p: A \longrightarrow C = \text{coeq}(a, b)$ also exists. Define $i: C \longrightarrow B$ as shown below by the universal property of a coequalizer

$$\begin{array}{c c c c}
E & a & f & B \\
b & p & i & C
\end{array}$$

(since $a.f = b.f$). As we see shortly, the factorization $f = p.i$ is a very good candidate for the coequalizer-mono factorization of $f$.
