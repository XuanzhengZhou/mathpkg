---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

When random variables $\xi$ and $\eta$ possess a joint density, their individual (marginal) densities are obtained by integrating out the other variable. This is a direct consequence of Fubini's theorem: for any Borel set $A$, $P(\xi \in A) = P((\xi,\eta) \in A \times \mathbb{R}) = \int_A [\int_{\mathbb{R}} f_{\xi,\eta}(x,y) \, dy] \, dx$, which identifies the inner integral as the marginal density $f_\xi(x)$.
