---
role: proof
locale: en
of_concept: ccc-implies-weak-distributive-law
source_book: gtm008
source_chapter: "20"
source_section: "20"
---

Let $\{b_{n\xi} \mid n < \omega \land \xi < \omega_{\alpha}\} \subseteq B$ be given. For each $n \in \omega$, consider the set $\{\,b_{n\xi} \mid \xi < \omega_{\alpha}\,\} \subseteq B$. Since $B$ satisfies the countable chain condition, the Boolean sum $\sum_{\xi < \omega_{\alpha}} b_{n\xi}$ can be expressed as the supremum of a countable subset. Consequently, for each $n \in \omega$ there exists a countable set $A_n \subseteq \omega_{\alpha}$ such that

$$\sum_{\xi < \omega_{\alpha}} b_{n\xi} = \sum_{\xi \in A_n} b_{n\xi}.$$

Define $\eta = \sup \bigcup_{n < \omega} A_n$. Since each $A_n$ is countable, their union $\bigcup_{n < \omega} A_n$ is a countable subset of $\omega_{\alpha}$. Because $\mathrm{cf}(\omega_{\alpha}) > \omega$, every countable subset of $\omega_{\alpha}$ is bounded; hence $\eta < \omega_{\alpha}$.

Now define a function $f \in \omega_{\alpha}^{\omega}$ by setting $f(n) = \sup A_n$ for each $n < \omega$. Since $A_n \subseteq \eta + 1$, we have $f(n) \leq \eta < \omega_{\alpha}$, so indeed $f \in \omega_{\alpha}^{\omega}$.

Then we compute:

$$\prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi} = \prod_{n < \omega} \sum_{\xi \in A_n} b_{n\xi} \leq \prod_{n < \omega} \sum_{\xi \leq f(n)} b_{n\xi} \leq \sum_{g \in \omega_{\alpha}^{\omega}} \prod_{n < \omega} \sum_{\xi \leq g(n)} b_{n\xi}.$$

The reverse inequality

$$\sum_{g \in \omega_{\alpha}^{\omega}} \prod_{n < \omega} \sum_{\xi \leq g(n)} b_{n\xi} \leq \prod_{n < \omega} \sum_{\xi < \omega_{\alpha}} b_{n\xi}$$

holds trivially for any complete Boolean algebra, since for any fixed $g \in \omega_{\alpha}^{\omega}$, each term $\sum_{\xi \leq g(n)} b_{n\xi}$ is bounded above by $\sum_{\xi < \omega_{\alpha}} b_{n\xi}$. Therefore $B$ satisfies the $(\omega, \omega_{\alpha})$-weak distributive law.
