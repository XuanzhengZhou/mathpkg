---
role: proof
locale: en
of_concept: logarithmic-derivative-of-zeta
source_book: gtm059
source_chapter: "16"
source_section: "Applications to the Fermat Curve"
---

**Note:** The source text for this section is severely degraded by OCR. The following proof reconstructs the standard argument.

From the definition $Z(V,T) = \exp\left(\sum_{\nu=1}^{\infty} N_\nu \frac{T^\nu}{\nu}\right)$, take the logarithm of both sides:

$$\log Z(V,T) = \sum_{\nu=1}^{\infty} N_\nu \frac{T^\nu}{\nu}.$$

Differentiating term by term with respect to $T$ gives

$$\frac{Z'(V,T)}{Z(V,T)} = \sum_{\nu=1}^{\infty} N_\nu \, T^{\nu-1}.$$

Multiplying both sides by $T$ yields the equivalent form

$$T \frac{Z'(V,T)}{Z(V,T)} = \sum_{\nu=1}^{\infty} N_\nu \, T^{\nu}.$$
