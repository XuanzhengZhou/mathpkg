---
role: proof
locale: en
of_concept: derivative-of-vector-product-lemma
source_book: gtm060
source_chapter: "2"
source_section: "7"
---

This follows directly from the definition of the derivative:
$$\frac{d}{dt}[a,b] = \lim_{h \to 0} \frac{[a(t+h), b(t+h)] - [a(t), b(t)]}{h}$$
$$= \lim_{h \to 0} \left( \left[\frac{a(t+h)-a(t)}{h}, b(t+h)\right] + \left[a(t), \frac{b(t+h)-b(t)}{h}\right] \right)$$
$$= [\dot{a}, b] + [a, \dot{b}].$$
