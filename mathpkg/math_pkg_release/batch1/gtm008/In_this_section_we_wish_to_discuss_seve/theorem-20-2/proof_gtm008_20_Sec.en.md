---
role: proof
locale: en
of_concept: theorem-20-2
source_book: gtm008
source_chapter: "20"
source_section: "20 Weak Distributive Laws

Again B denotes a complete Boolean a"
---
Let $\{b_{n\xi} \mid n < \omega \land \xi < \omega_{\alpha}\} \subseteq B$. Then by the c.c.c., for each $n \in \omega$ there exists a countable set $C_n \subseteq B$ such that

$$\sum_{\xi < \omega_{\alpha}} b_{n\xi} = \sup C_n.$$

Define $\eta_0 = \sup \{ \xi < \omega_{\alpha} \mid (\exists n \in \omega)[

Define $b_{n\xi} = \llbracket f(\check{n}) = \check{\xi} \rrbracket$, which should be understood as

$$\llbracket (\forall z) [\langle \check{n}, z \rangle \in f \leftrightarrow z = \check{\xi} ] \rrbracket.$$

Then

$$b = \prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi}$$

$$= \sum_{\eta < \omega_{\alpha}} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi} \quad \text{by the } (\omega, \omega_{\alpha})$-WDL

$$= \llbracket (\exists \eta < \omega_{\alpha})^{\vee} (\forall n < \omega) [f(n) \leq \eta] \rrbracket.$$

Since

$$\llbracket cf((\omega_{\alpha})^{\vee}) > \check{\omega} \rrbracket = \llbracket (\forall f) [\text{if } f: \check{\omega} \rightarrow (\omega_{\alpha})^{\vee} \text{ then } (\exists \eta < (\omega_{\alpha})^{\vee}) (\forall n < \check{\omega}) [f(n) \leq \eta] ] \rrbracket,$$

this proves $$\llbracket cf((\omega_{\alpha})^{\vee}) > \check{\omega} \rrbracket = 1.$$

To prove the converse, let $\{b_{n\xi} \mid n < \omega \land \xi < \omega_{\alpha}\} \subseteq B$ and assume $$\llbracket cf((\omega_{\alpha})^{\vee}) > \check{\omega} \rrbracket = 1.$$ Define

$$f \in V^{(B)} \text{ by } \mathcal{D}(f) = \{\langle \check{n}, \check{\xi} \rangle^{(B)} \mid n \in \omega \land \xi < \omega_{\alpha}\},$$

$$(\forall n \in \omega

Then

$$b = \prod_{n < \omega} \sum_{m < \omega} b_{nm}$$

$$= \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm}$$

by the $(\omega, \omega)$-WDL

$$= \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \llbracket g(\check{n}) \leq \check{f}(\check{n}) \rrbracket$$

$$b = \llbracket (\exists f \in (\omega^{\omega})^{\vee}) (\forall n < \check{n}) [g(n) \leq f(n)] \rrbracket.$$

The converse is proved similarly.
