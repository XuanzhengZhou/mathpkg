---
role: proof
locale: en
of_concept: joint-density-marginal-formula
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Marginal Densities from Joint Density

**Proposition.** Let $(\xi, \eta)$ have a two-dimensional density $f_{\xi,\eta}(x,y)$. Then the one-dimensional distributions for $\xi$ and $\eta$ have densities $f_{\xi}(x)$ and $f_{\eta}(y)$, where

$$f_{\xi}(x) = \int_{-\infty}^{\infty} f_{\xi,\eta}(x,y) \, dy \quad \text{and} \quad f_{\eta}(y) = \int_{-\infty}^{\infty} f_{\xi,\eta}(x,y) \, dx. \tag{55}$$

*Proof.* If $A \in \mathcal{B}(\mathbb{R})$, then by Fubini's theorem,

$$P(\xi \in A) = P((\xi,\eta) \in A \times \mathbb{R}) = \int_{A \times \mathbb{R}} f_{\xi,\eta}(x,y) \, dx \, dy = \int_A \left[ \int_{\mathbb{R}} f_{\xi,\eta}(x,y) \, dy \right] dx.$$

The right-hand side expresses $P(\xi \in A)$ as the integral over $A$ of the function $\int_{\mathbb{R}} f_{\xi,\eta}(x,y) \, dy$, which is exactly the defining property of a density for the distribution of $\xi$. Thus

$$f_{\xi}(x) = \int_{-\infty}^{\infty} f_{\xi,\eta}(x,y) \, dy$$

is a density for $\xi$. The second formula for $f_{\eta}(y)$ is established similarly by considering $P(\eta \in B) = P((\xi,\eta) \in \mathbb{R} \times B)$. $\square$
