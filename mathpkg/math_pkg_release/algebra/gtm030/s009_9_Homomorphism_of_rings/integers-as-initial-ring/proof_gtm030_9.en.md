---
role: proof
locale: en
of_concept: integers-as-initial-ring
source_book: gtm030
source_chapter: "2"
source_section: "9. Homomorphism of rings"
---

Let $$I = \mathbb{Z}$$ be the ring of integers. Define the map $$n \mapsto ne$$ where $$e = 1$$ is the identity of $$\mathfrak{A}$$. Since

$$(n + m)e = ne + me, \qquad (nm)e = (nm)e^2 = (ne)(me),$$

this correspondence is a ring homomorphism from $$I$$ into $$\mathfrak{A}$$. The image set $$Ie$$ is a subring of $$\mathfrak{A}$$ containing $$1e = e = 1_{\mathfrak{A}}$$. Hence $$Ie = \mathfrak{A}$$, and $$\mathfrak{A}$$ is a homomorphic image of $$I$$.

By the Fundamental Theorem of Ring Homomorphisms, $$\mathfrak{A} \cong I/\ker(\eta)$$. The kernel of the map $$n \mapsto ne$$ is an ideal of $$I$$; every ideal of $$\mathbb{Z}$$ is of the form $$(m)$$ for some $$m \geq 0$$. Therefore $$\mathfrak{A} \cong \mathbb{Z}/(m)$$.

If $$m = 0$$, then $$\mathfrak{A} \cong \mathbb{Z}$$ is infinite. If $$m > 0$$, then $$\mathfrak{A}$$ is finite with $$m$$ elements and is isomorphic to the finite ring $$\mathbb{Z}/(m)$$.
