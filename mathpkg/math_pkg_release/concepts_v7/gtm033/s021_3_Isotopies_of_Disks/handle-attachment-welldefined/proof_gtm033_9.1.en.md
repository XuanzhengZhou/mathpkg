---
role: proof
locale: en
of_concept: handle-attachment-welldefined
source_book: gtm033
source_chapter: "9"
source_section: "1"
---

# Proof of Theorem 1.1 (Handle Attachment is Well-Defined up to Diffeomorphism)

Let $M$ be a surface. Given an embedding $f: S^0 \times D^2 \hookrightarrow M - \partial M$, define the surface obtained by attaching a handle:

$$M[f] = [M - \operatorname{Int} f(S^0 \times D^2)] \bigcup_f D^1 \times S^1.$$

Then the diffeomorphism type of $M[f]$ depends only on the isotopy class of $f|S^0 \times S^1$.

**Proof.** Let $f_0, f_1: S^0 \times D^2 \hookrightarrow M - \partial M$ be embeddings such that $f_0|S^0 \times S^1$ and $f_1|S^0 \times S^1$ are isotopic. Set $Q_i = D^1 \times S^1$ (the handle) and let $g_i = f_i|S^0 \times S^1: \partial Q_i \to \partial(M - \operatorname{Int} f_i(S^0 \times D^2))$ for $i = 0, 1$.

Since $g_0$ and $g_1$ are isotopic, the diffeomorphism $g_1^{-1}g_0: \partial Q_0 \to \partial Q_1$ extends to a diffeomorphism $\varphi: Q_0 \approx Q_1$ (by extending the isotopy over the collar). The theorem then follows from Theorem 8.2.2 (isotopic gluing diffeomorphisms yield diffeomorphic adjunction spaces). $\square$
