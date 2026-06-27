---
role: proof
locale: en
of_concept: mobius-transformation-derivative
source_book: gtm041
source_chapter: "2"
source_section: "2.1"
---

From the difference formula
$$f(w) - f(z) = \frac{(ad-bc)(w-z)}{(cw+d)(cz+d)},$$
divide both sides by $w-z$:
$$\frac{f(w) - f(z)}{w-z} = \frac{ad-bc}{(cw+d)(cz+d)}.$$
Taking the limit as $w \to z$ gives
$$f'(z) = \lim_{w \to z} \frac{f(w) - f(z)}{w-z} = \frac{ad-bc}{(cz+d)^2}.$$
Since $ad-bc \neq 0$, we have $f'(z) \neq 0$ at every $z \neq -d/c$ (i.e., at every point where $f$ is analytic).
