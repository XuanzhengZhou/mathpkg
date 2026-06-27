---
role: proof
locale: en
of_concept: restricted-commutativity-of-4-10
source_book: gtm026
source_chapter: "5"
source_section: "5.38"
---

To prove this, one need only observe that $(\emptyset \longrightarrow XT)T \cdot X\mu$ and $(\emptyset \longrightarrow XT) \cdot \xi T$ are already equal, both being the unique $T$-homomorphism $(\emptyset T, \emptyset\mu) \longrightarrow (XT, X\mu)$.

Now consider the diagram induced by $\alpha: m \longrightarrow n$ and $\beta: n \longrightarrow p$:

$$
\begin{array}{c}
X^m \\
\downarrow (X\hat{\alpha}_i) \\
XT^n \\
\downarrow (XT\hat{\beta}_j) \\
XT^p \\
\downarrow (X\mu)^p \\
XT^p \\
\downarrow \\
X^p
\end{array}
$$

The two boundary paths from $X^m$ to $X^p$ are equal precisely when $M_\xi$ preserves composition, whereas III is equivalent to 4.10 (as $p$ can equal 1). I and II always commute (by 5.37 and the naturality of $\hat{\beta}_j$). It is now clear that if 4.10 holds then $M_\xi$ preserves composition. Using 5.38, to prove the converse it is sufficient to show that given $\bar{x} \in X^m$, the two boundary paths agree when restricted to the true constants.
