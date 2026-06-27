---
role: proof
locale: en
of_concept: canonical-isomorphism-inner-product-dual
source_book: gtm023
source_chapter: "7"
source_section: "4. Duality in an inner product space"
---

For each \(x \in E\), the map \(y \mapsto (x, y)\) is a linear functional on \(E\) by the bilinearity of the inner product. Define \(\tau : E \to E^*\) by \(\langle \tau x, y \rangle = (x, y)\). The map \(\tau\) is linear since

$$\langle \tau(\lambda x_1 + \mu x_2), y \rangle = (\lambda x_1 + \mu x_2, y) = \lambda (x_1, y) + \mu (x_2, y) = \lambda \langle \tau x_1, y \rangle + \mu \langle \tau x_2, y \rangle.$$

Since the inner product is positive definite, \(\tau x = 0\) implies \((x, y) = 0\) for all \(y\), so in particular \((x, x) = 0\) and thus \(x = 0\). Hence \(\tau\) is injective. Since \(\dim E = \dim E^*\), \(\tau\) is an isomorphism.

Define the inner product on \(E^*\) by \((x^*, y^*) = (\tau^{-1} x^*, \tau^{-1} y^*)\). This is positive definite because the original inner product is.

To show \(\tau\) is self-dual, recall that \(\tau^* : E^{**} \to E^*\) is defined (under \(E^{**} \cong E\)) by \(\langle \tau^* y, x \rangle = \langle y, \tau x \rangle\). But

$$\langle \tau x, y \rangle = (x, y) = (y, x) = \langle \tau y, x \rangle.$$

Thus \(\langle \tau^* y, x \rangle = \langle y, \tau x \rangle = \langle \tau x, y \rangle = (x, y) = (y, x) = \langle \tau y, x \rangle\), which holds for all \(x\). Hence \(\tau^* y = \tau y\) for all \(y\), so \(\tau^* = \tau\).
