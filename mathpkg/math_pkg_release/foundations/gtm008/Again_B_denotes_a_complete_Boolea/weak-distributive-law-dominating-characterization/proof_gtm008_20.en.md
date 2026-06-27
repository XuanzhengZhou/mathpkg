---
role: proof
locale: en
of_concept: weak-distributive-law-dominating-characterization
source_book: gtm008
source_chapter: "20"
source_section: "20"
---

We prove both directions, analogous to the cofinality characterization.

**($\Rightarrow$)** Assume $B$ satisfies the $(\omega, \omega)$-WDL. Let $\{b_{nm} \mid n, m < \omega\} \subseteq B$ be given, and define a name $g$ for a function $\check{\omega} \to \check{\omega}$ by setting

$$\llbracket g(\check{n}) = \check{m} \rrbracket = b_{nm}$$

for each $n, m < \omega$, with the elements $\{b_{nm} \mid m < \omega\}$ pairwise disjoint for each fixed $n$ (by taking an appropriate refinement). Then

$$\prod_{n < \omega} \sum_{m < \omega} b_{nm} = 1.$$

By the $(\omega, \omega)$-WDL, we have

$$1 = \prod_{n < \omega} \sum_{m < \omega} b_{nm} = \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm}.$$

Now observe that

$$\prod_{n < \omega} \sum_{m \leq f(n)} b_{nm} = \prod_{n < \omega} \llbracket g(\check{n}) \leq \check{f}(\check{n}) \rrbracket = \llbracket (\forall n < \check{\omega}) [g(n) \leq \check{f}(n)] \rrbracket.$$

Summing over $f \in \omega^{\omega}$ yields

$$1 = \sum_{f \in \omega^{\omega}} \llbracket (\forall n < \check{\omega}) [g(n) \leq \check{f}(n)] \rrbracket = \llbracket (\exists f \in (\omega^{\omega})^{\vee}) (\forall n < \check{\omega}) [g(n) \leq f(n)] \rrbracket.$$

**($\Leftarrow$)** Conversely, assume that for every name $g$ for a function $\check{\omega} \to \check{\omega}$,

$$\llbracket (\exists f \in (\omega^{\omega})^{\vee}) (\forall n < \check{\omega}) [g(n) \leq f(n)] \rrbracket = 1.$$

Let $\{b_{nm} \mid n, m < \omega\} \subseteq B$ be given. Define $g$ as above by $\llbracket g(\check{n}) = \check{m} \rrbracket = b_{nm}$. Then

$$1 = \llbracket (\exists f \in (\omega^{\omega})^{\vee}) (\forall n < \check{\omega}) [g(n) \leq f(n)] \rrbracket = \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm}.$$

Since $\prod_{n < \omega} \sum_{m < \omega} b_{nm} = 1$ holds in any case, we obtain

$$\prod_{n < \omega} \sum_{m < \omega} b_{nm} = \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm},$$

which is precisely the $(\omega, \omega)$-weak distributive law.
