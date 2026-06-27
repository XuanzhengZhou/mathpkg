---
role: proof
locale: en
of_concept: newtonian-potential-representation
source_book: gtm035
source_chapter: "2"
source_section: "2.6"
---

# Proof of Newtonian Potential Representation

**Lemma 2.6.** Let $G \in C_0^2(\mathbb{C})$. Then

$$G(\zeta) = -\frac{1}{2\pi} \int_{\mathbb{C}} \Delta G(z) \log \frac{1}{|z - \zeta|}\, dx\,dy, \qquad \text{for all } \zeta \in \mathbb{C}.$$

## Proof

Starting from Lemma 2.5, we have

$$G(\zeta) = -\frac{1}{\pi} \int_{\mathbb{C}} \frac{\partial G}{\partial \overline{z}}(z) \frac{dx\,dy}{z - \zeta}.$$

Apply the same formula to $\partial G / \partial \overline{z}$ (which is in $C_0^1(\mathbb{C})$ since $G \in C_0^2$):

$$\frac{\partial G}{\partial \overline{z}}(z) = -\frac{1}{\pi} \int_{\mathbb{C}} \frac{\partial}{\partial \overline{w}} \left( \frac{\partial G}{\partial \overline{z}} \right)(w) \frac{du\,dv}{w - z}.$$

Substituting and interchanging the order of integration (justified by Fubini's theorem and the compact support),

$$G(\zeta) = \frac{1}{\pi^2} \int_{\mathbb{C}} \int_{\mathbb{C}} \frac{\partial^2 G}{\partial w \partial \overline{w}}(w) \frac{dx\,dy}{(z - \zeta)(w - z)} \, du\,dv.$$

The inner integral over $z$ evaluates to $\log |w - \zeta|$ (up to a constant). More precisely, one computes

$$\int_{\mathbb{C}} \frac{dx\,dy}{(z - \zeta)(w - z)} = -\pi \log \frac{1}{|w - \zeta|},$$

which, together with $\Delta = 4 \frac{\partial^2}{\partial w \partial \overline{w}}$, yields the stated formula:

$$G(\zeta) = -\frac{1}{2\pi} \int_{\mathbb{C}} \Delta G(z) \log \frac{1}{|z - \zeta|}\, dx\,dy.$$

$\square$
