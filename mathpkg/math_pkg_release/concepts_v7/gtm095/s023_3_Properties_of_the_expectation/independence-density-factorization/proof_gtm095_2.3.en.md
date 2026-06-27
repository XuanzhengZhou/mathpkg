---
role: proof
locale: en
of_concept: independence-density-factorization
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Independence Criterion via Density Factorization

**Proposition.** When there is a two-dimensional density $f_{\xi,\eta}(x,y)$, the variables $\xi$ and $\eta$ are independent if and only if

$$f_{\xi,\eta}(x,y) = f_{\xi}(x) f_{\eta}(y) \tag{56}$$

(where the equation is to be understood in the sense of holding almost everywhere with respect to two-dimensional Lebesgue measure).

*Proof.* **Sufficiency.** If (56) holds, then by Fubini's theorem,

$$F_{\xi,\eta}(x,y) = \int_{(-\infty,x] \times (-\infty,y]} f_{\xi,\eta}(u,v) \, du \, dv = \int_{(-\infty,x] \times (-\infty,y]} f_{\xi}(u) f_{\eta}(v) \, du \, dv$$
$$= \int_{-\infty}^x f_{\xi}(u) \, du \cdot \int_{-\infty}^y f_{\eta}(v) \, dv = F_{\xi}(x) F_{\eta}(y),$$

which is the necessary and sufficient condition for independence of $\xi$ and $\eta$ (by the theorem of Section 5).

**Necessity.** If $\xi$ and $\eta$ are independent, then $F_{\xi,\eta}(x,y) = F_{\xi}(x) F_{\eta}(y)$ for all $(x,y) \in \mathbb{R}^2$. Differentiating both sides (or using the fact that the joint density, when it exists, is uniquely determined by the joint distribution function), we obtain $f_{\xi,\eta}(x,y) = f_{\xi}(x) f_{\eta}(y)$ almost everywhere. $\square$
