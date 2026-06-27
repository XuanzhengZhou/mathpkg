---
role: proof
locale: en
of_concept: schwarz-reflection-principle
source_book: gtm011
source_chapter: "9"
source_section: "9.1"
---

Define $g: G \to \mathbb{C}$ by
$$g(z) = \begin{cases} f(z), & z \in G_+ \cup G_0, \\ \overline{f(\bar{z})}, & z \in G_-. \end{cases}$$
It is clear that $g$ extends $f$ and that $g$ is continuous on $G$. To prove analyticity, one checks that $\int_T g = 0$ for every triangular path $T$ in $G$ (Morera's Theorem). For triangles entirely contained in $G_+$ or $G_-$, this follows from the analyticity of $f$ and the fact that $z \mapsto \overline{f(\bar{z})}$ is analytic when $f$ is. For triangles that cross $G_0$, one approximates the triangle by unions of triangles in $G_+$ and $G_-$ and uses the continuity of $g$ and the real-valuedness of $f$ on $G_0$ to show the integral over the approximating triangles converges to zero. By Morera's Theorem, $g$ is analytic on $G$.

Note: The source OCR contains garbled text in the proof section. The proof presented here is reconstructed from mathematical reasoning based on the standard proof of the Schwarz Reflection Principle.
