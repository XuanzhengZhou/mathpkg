---
role: proof
locale: en
of_concept: nontrivial-theory-equivalences
source_book: gtm026
source_chapter: "5"
source_section: "5"
---

**Proof of Proposition 5.2.**

**(1 $\Rightarrow$ 2):** Suppose $T$ is nontrivial, so some $T$-algebra has at least two elements. By forming a suitably large cartesian power (as in 4.27), for each set $X$ we can construct a $T$-algebra $(Y, \theta)$ and an injective function $f: X \longrightarrow Y$. From the naturality square (3.11) we have:

$$X\eta \cdot (fT \cdot \theta) = f \cdot Y\eta \cdot \theta = f \cdot \mathrm{id}_Y = f$$

Since $f$ is injective and equals $X\eta$ followed by some function, $X\eta$ must itself be injective.

**(2 $\Rightarrow$ 3):** If $f \neq g$ and $Y\eta$ is injective, then $f \cdot Y\eta \neq g \cdot Y\eta$. Naturality of $\eta$ gives $X\eta \cdot fT = f \cdot Y\eta$ and $X\eta \cdot gT = g \cdot Y\eta$, so $X\eta \cdot fT \neq X\eta \cdot gT$, which implies $fT \neq gT$. Thus $T$ is faithful.

**(3 $\Rightarrow$ 1):** This is clear, since neither of the two functors involved in the trivial theories are faithful. $\square$
