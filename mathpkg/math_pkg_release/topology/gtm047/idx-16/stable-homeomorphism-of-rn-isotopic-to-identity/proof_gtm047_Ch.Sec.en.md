---
role: proof
locale: en
of_concept: stable-homeomorphism-of-rn-isotopic-to-identity
source_book: gtm047
source_chapter: ""
source_section: ""
---

We may suppose that $f_1$ is the identity on $\mathbf{B}^n$, since $f_1$ is isotopic to a homeomorphism which has this property. Let $\operatorname{inv}$ be the inversion
$$\mathbf{R}^n - \{0\} \leftrightarrow \mathbf{R}^n - \{0\}, \quad P \mapsto P / \|P\|^2,$$
where $0$ is the origin. Let $g_1: \mathbf{B}^n \leftrightarrow \mathbf{B}^n$ be defined by the conditions
$$g_1(0) = 0,$$
$$g_1(P) = \operatorname{inv} \circ f_1 \circ \operatorname{inv}(P) \quad (0 < \|P\| \leq 1).$$

Then $g_1$ is a homeomorphism $\mathbf{B}^n \leftrightarrow \mathbf{B}^n$, and $g_1|_{\mathbf{S}^{n-1}}$ is the identity. Therefore $g_1$ is isotopic to the identity (by Alexander's theorem). Let $\psi: \mathbf{B}^n \times [0, 1] \to \mathbf{B}^n$ be the isotopy given in the proof of the preceding theorem. Under the definition of $\psi$, we have $\psi(0, t) = 0$ for every $t$, and $\psi(P, t) \neq 0$ for every $P \neq 0$ and every $t$. Therefore $\psi' = \psi|_{(\mathbf{B}^n - \{0\}) \times [0, 1]}$ has analogous properties. Conjugating by $\operatorname{inv}$ once more yields an isotopy between $f_1$ and the identity on $\mathbf{R}^n$.
