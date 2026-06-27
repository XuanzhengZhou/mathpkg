---
role: proof
locale: en
of_concept: weak-distributive-law-cofinality-equivalence
source_book: gtm008
source_chapter: "20"
source_section: "20"
---

We prove both directions.

**($\Rightarrow$)** Assume $B$ satisfies the $(\omega, \omega_{\alpha})$-WDL. To show $\llbracket \mathrm{cf}((\omega_{\alpha})^{\vee}) > \check{\omega} \rrbracket = 1$, it suffices to show that for every $f \in V^{(B)}$ with $\llbracket f : \check{\omega} \to (\omega_{\alpha})^{\vee} \rrbracket = 1$, we have $\llbracket (\exists \eta < (\omega_{\alpha})^{\vee}) (\forall n < \check{\omega}) [f(n) \leq \eta] \rrbracket = 1$.

Take any such $f$ and define, for each $n \in \omega$ and $\xi < \omega_{\alpha}$,

$$b_{n\xi} = \llbracket f(\check{n}) = \check{\xi} \rrbracket.$$

Then for each $n \in \omega$, since $f(\check{n})$ is forced to be an ordinal below $(\omega_{\alpha})^{\vee}$, we have $\sum_{\xi < \omega_{\alpha}} b_{n\xi} = 1$, and the elements $\{b_{n\xi} \mid \xi < \omega_{\alpha}\}$ are pairwise disjoint for fixed $n$.

Now compute the Boolean value of the boundedness statement:

$$\llbracket (\exists \eta < (\omega_{\alpha})^{\vee}) (\forall n < \check{\omega}) [f(n) \leq \eta] \rrbracket = \sum_{\eta < \omega_{\alpha}} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi}.$$

On the other hand,

$$\prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi} = \prod_{n < \omega} 1 = 1.$$

Applying the $(\omega, \omega_{\alpha})$-WDL to the family $\{b_{n\xi}\}$ (in the equivalent form with $\prod_n \sum_\xi$ on the left), and noting that the WDL yields

$$\prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi} = \sum_{\eta < \omega_{\alpha}} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi}$$

(because for $f \in \omega_{\alpha}^{\omega}$, the inner product $\prod_{n} \sum_{\xi \leq f(n)} b_{n\xi}$ is dominated by the term with $\eta = \sup_{n} f(n) < \omega_{\alpha}$, using $\mathrm{cf}(\omega_{\alpha}) > \omega$ as noted in the Remark after Definition 20.1). Hence

$$1 = \prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi} = \sum_{\eta < \omega_{\alpha}} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi} = \llbracket (\exists \eta < (\omega_{\alpha})^{\vee}) (\forall n < \check{\omega}) [f(n) \leq \eta] \rrbracket.$$

Thus $\llbracket \mathrm{cf}((\omega_{\alpha})^{\vee}) > \check{\omega} \rrbracket = 1$.

**($\Leftarrow$)** Conversely, assume $\llbracket \mathrm{cf}((\omega_{\alpha})^{\vee}) > \check{\omega} \rrbracket = 1$. Let $\{b_{n\xi} \mid n < \omega \land \xi < \omega_{\alpha}\} \subseteq B$ be given. Define $f \in V^{(B)}$ with domain

$$\mathcal{D}(f) = \{\langle \check{n}, \check{\xi} \rangle^{(B)} \mid n \in \omega \land \xi < \omega_{\alpha}\}$$

and for each $n \in \omega$, set

$$f(\check{n}) = \sum_{\xi < \omega_{\alpha}} \check{\xi} \cdot b_{n\xi}$$

where the mixed Boolean sum is interpreted in $V^{(B)}$ (i.e., the element whose Boolean value of equalling $\check{\xi}$ is $b_{n\xi}$). Then $\llbracket f : \check{\omega} \to (\omega_{\alpha})^{\vee} \rrbracket = 1$, and for each $n$ and $\xi$,

$$\llbracket f(\check{n}) = \check{\xi} \rrbracket = b_{n\xi}.$$

Since $\llbracket \mathrm{cf}((\omega_{\alpha})^{\vee}) > \check{\omega} \rrbracket = 1$, we obtain

$$1 = \llbracket (\exists \eta < (\omega_{\alpha})^{\vee}) (\forall n < \check{\omega}) [f(n) \leq \eta] \rrbracket = \sum_{\eta < \omega_{\alpha}} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi}.$$

Moreover, $\prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi} = 1$ as argued above. Hence

$$\prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi} = \sum_{\eta < \omega_{\alpha}} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi}.$$

By the Remark after Definition 20.1 (since $\mathrm{cf}(\omega_{\alpha}) > \omega$ by hypothesis), the right-hand side equals $\sum_{f \in \omega_{\alpha}^{\omega}} \prod_{n < \omega} \sum_{\xi \leq f(n)} b_{n\xi}$, establishing the $(\omega, \omega_{\alpha})$-WDL.
