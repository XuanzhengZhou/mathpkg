---
role: proof
locale: en
of_concept: generalized-quotient-ring-existence
source_book: gtm028
source_chapter: "I"
source_section: "9. Quotient rings"
---

Let $\mathfrak{n} = \{ x \in R \mid \exists m \in M,\; xm = 0 \}$. One verifies that $\mathfrak{n}$ is an ideal of $R$. Let $\varphi: R \to R/\mathfrak{n}$ be the canonical homomorphism. The image $\overline{M} = \varphi(M)$ is a multiplicative system in $R/\mathfrak{n}$, and since every element of $\mathfrak{n}$ annihilated by some element of $M$ has been factored out, $\overline{M}$ consists entirely of regular elements of $R/\mathfrak{n}$. Thus $\overline{M}$ is a regular multiplicative system in $R/\mathfrak{n}$, and we may form the quotient ring $(R/\mathfrak{n})_{\overline{M}}$ in the classical (regular) sense. Let $\psi: R/\mathfrak{n} \to (R/\mathfrak{n})_{\overline{M}}$ be the canonical isomorphism (embedding $R/\mathfrak{n}$ into its quotient ring).

Define $R_M = (R/\mathfrak{n})_{\overline{M}}$ and $h = \varphi \circ \psi$, i.e., $h(x) = \psi(\varphi(x))$ for $x \in R$. We verify the three required properties:

\textbf{1)} $\ker h = \mathfrak{n}$. If $x \in \mathfrak{n}$, then $\varphi(x) = 0$, so $h(x) = \psi(0) = 0$. Conversely, if $h(x) = 0$, then $\psi(\varphi(x)) = 0$, and since $\psi$ is injective, $\varphi(x) = 0$, so $x \in \mathfrak{n}$.

\textbf{2)} For $m \in M$, $h(m) = \psi(\varphi(m))$. Since $\varphi(m) \in \overline{M}$ and $\overline{M}$ is regular, $\psi(\varphi(m))$ is a unit in $(R/\mathfrak{n})_{\overline{M}}$, i.e., $h(m)$ is a unit in $R_M$.

\textbf{3)} Every element of $(R/\mathfrak{n})_{\overline{M}}$ is of the form $\psi(a)/\psi(\overline{m})$ for some $a \in R/\mathfrak{n}$ and $\overline{m} \in \overline{M}$. Writing $a = \varphi(x)$ and $\overline{m} = \varphi(m)$ with $x \in R$, $m \in M$, we have $\psi(a)/\psi(\overline{m}) = \psi(\varphi(x))/\psi(\varphi(m)) = h(x)/h(m)$. Thus every element of $R_M$ is of the form $h(x)/h(m)$.
