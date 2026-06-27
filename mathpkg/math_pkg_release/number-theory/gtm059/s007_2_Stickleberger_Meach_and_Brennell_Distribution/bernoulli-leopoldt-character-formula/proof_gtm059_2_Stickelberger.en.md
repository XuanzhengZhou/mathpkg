---
role: proof
locale: en
of_concept: bernoulli-leopoldt-character-formula
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

Write $dE_n = dE_{n,c} + c^n dE_n \circ c^{-1}$, where $E_{n,c} = E_n - c^n E_n \circ c^{-1}$. Then

$$\int_{\mathbf{Z}_p^*} \psi \, dE_n = \int_{\mathbf{Z}_p^*} \psi \, dE_{n,c} + c^n \int_{\mathbf{Z}_p^*} \psi \, d(E_n \circ c^{-1}).$$

For the second integral, use the change of variables $a \mapsto c^{-1}a$:

$$c^n \int_{\mathbf{Z}_p^*} \psi(c^{-1}a) \, dE_n(a) = c^n \psi(c^{-1}) \int_{\mathbf{Z}_p^*} \psi(a) \, dE_n(a).$$

Thus

$$\int_{\mathbf{Z}_p^*} \psi \, dE_n = \frac{1}{1 - \psi(c)c^n} \int_{\mathbf{Z}_p^*} \psi \, dE_{n,c}.$$

By Theorem 2.2, $E_{n,c}(x) = x^{n-1}E_{1,c}(x)$, so substituting this yields

$$\frac{1}{n}B_{n,\psi} = \int_{\mathbf{Z}_p^*} \psi \, dE_n
= \frac{1}{1 - \psi(c)c^n} \int_{\mathbf{Z}_p^*} \psi(a) a^{n-1} \, dE_{1,c}(a).$$

Recall that by definition $B_{n,\psi} = N^{n-1} \sum_{a \in G} \psi(a) B_n(\langle a/N \rangle)$ and in terms of distribution notation,
$\frac{1}{n}B_{n,\psi} = \int_{\mathbf{Z}_p^*} \psi \, dE_n$, which completes the proof.
