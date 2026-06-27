---
role: proof
locale: en
of_concept: morse-dual-nk-cell
source_book: gtm033
source_chapter: "6"
source_section: "6.3"
---

# Proof of Morse Dual Cell Attachment for a Single Critical Point

Consider the map $-f: M \to [-b, -a]$ instead of $f$. Since $f$ is an admissible Morse function with a unique critical point $z$ of index $k$, the function $-f$ is also an admissible Morse function (with the interval $[-b, -a]$), and at $z$ the Morse index of $-f$ is $n - k$.

Applying Theorem 3.1 to $-f$, we obtain an $(n - k)$-cell $e_*^{n-k} \subset M - (-f)^{-1}(-a) = M - f^{-1}(a)$ such that

$$e_*^{n-k} \cap (-f)^{-1}(-b) = \partial e_*^{n-k},$$

i.e.,

$$e_*^{n-k} \cap f^{-1}(b) = \partial e_*^{n-k},$$

and there is a deformation retraction of $M$ onto

$$(-f)^{-1}(-b) \cup e_*^{n-k} = f^{-1}(b) \cup e_*^{n-k}.$$

Moreover, $e_*^{n-k}$ can be chosen so that $e^k$ (of Theorem 3.1) meets $e_*^{n-k}$ only at $z$, and transversely. This follows from the construction: in Morse coordinates, the $k$-cell $e^k$ corresponds to $D^k(\sqrt{2\varepsilon}) \times \{0\}$, while the $(n-k)$-cell for $-f$ corresponds to $\{0\} \times D^{n-k}(\sqrt{2\varepsilon})$. These intersect transversely at the origin $z = (0,0) \in \mathbb{R}^k \times \mathbb{R}^{n-k}$.
