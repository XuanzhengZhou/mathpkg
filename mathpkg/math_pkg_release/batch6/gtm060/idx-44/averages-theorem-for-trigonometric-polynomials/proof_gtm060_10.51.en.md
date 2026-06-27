---
role: proof
locale: en
of_concept: averages-theorem-for-trigonometric-polynomials
source_book: gtm060
source_chapter: "10"
source_section: "51"
---

Both the time average and space average are linear operations:

- Space average: $\overline{\alpha f + \beta g} = \alpha \bar{f} + \beta \bar{g}$
- Time average: $(\alpha f + \beta g)^* = \alpha f^* + \beta g^*$ (when the limits exist)

For a trigonometric polynomial $f = \sum_{|k| < N} f_k e^{i(k, \varphi)}$, we compute term by term. By Lemma 1, for each $k$ we have

$$\left(e^{i(k, \cdot)}\right)^* = \overline{e^{i(k, \cdot)}}.$$

Applying linearity,

$$f^* = \sum_{|k| < N} f_k \left(e^{i(k, \cdot)}\right)^* = \sum_{|k| < N} f_k \overline{e^{i(k, \cdot)}} = \overline{\sum_{|k| < N} f_k e^{i(k, \cdot)}} = \bar{f}.$$

Thus the equality of time and space averages holds for all trigonometric polynomials.
