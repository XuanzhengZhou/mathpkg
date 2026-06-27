---
role: proof
locale: en
of_concept: kleisli-composition-law
source_book: gtm026
source_chapter: "3"
source_section: "3.14"
---

$$\alpha \circ \beta = \alpha \circ (\beta.\mathrm{id}_{CT}) = \alpha \circ \beta^{\#}.\mathrm{id}_{CT} = \alpha.\beta T.\mathrm{id}_{CT} = \alpha.(\beta T.\mathrm{id}_{CTT}) \circ \mathrm{id}_{CT} = \alpha.(\beta T^{\#}.\mathrm{id}_{CTT}) \circ \mathrm{id}_{CT} = \alpha.(\beta T^{\#}.C\mu) = \alpha.\beta T.C\mu.$$
