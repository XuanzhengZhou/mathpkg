---
role: proof
locale: en
of_concept: open-continuous-image-locally-compact
source_book: gtm027
source_chapter: "5"
source_section: "Locally Compact Spaces"
---

# Proof that the Open Continuous Image of a Locally Compact Space is Locally Compact

Let $X$ be a locally compact space and let $f: X \to Y$ be a continuous open surjection. Let $y \in Y$ and pick $x \in f^{-1}(y)$. Since $X$ is locally compact, $x$ has a compact neighborhood $C$ in $X$. Because $f$ is continuous, $f(C)$ is compact in $Y$ (the continuous image of a compact set is compact). Because $f$ is open, the image under $f$ of the interior $C^0$ is an open set in $Y$, and $y = f(x) \in f(C^0) \subset f(C)$. Thus $f(C)$ is a compact subset of $Y$ containing an open neighborhood of $y$, so $f(C)$ is a compact neighborhood of $y$. Therefore $Y$ is locally compact. $\square$

*Remark.* The hypothesis that $f$ is open is essential: the continuous image of a locally compact space need not be locally compact. For example, every discrete space is locally compact, and every topological space is the continuous one-to-one image of a discrete space (take the same set with the discrete topology and the identity function).
