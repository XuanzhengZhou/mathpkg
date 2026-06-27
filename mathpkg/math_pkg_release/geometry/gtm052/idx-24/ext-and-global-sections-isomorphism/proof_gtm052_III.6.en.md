---
role: proof
locale: en
of_concept: ext-and-global-sections-isomorphism
source_book: gtm052
source_chapter: "III"
source_section: "6"
---

The question is local, by (6.2), so we may assume that $X$ is affine. Then $\mathcal{F}$ has a locally free (or even a free) resolution $\mathcal{L}_\bullet \to \mathcal{F} \to 0$, which on the stalks at $x$ gives a free resolution $(\mathcal{L}_\bullet)_x \to \mathcal{F}_x \to 0$. So by (6.5) we can calculate both sides by these resolutions. Since $\mathcal{H}om(\mathcal{L}, \mathcal{G})_x = \mathcal{H}om_{\mathcal{O}_x}(\mathcal{L}_x, \mathcal{G}_x)$ for a locally free sheaf $\mathcal{L}$, and since the stalk functor is exact, we get the equality of the Ext groups.

Note that even the case $i = 0$ is not true without some special hypothesis on $\mathcal{F}$, such as $\mathcal{F}$ being coherent.
