---
role: proof
locale: en
of_concept: fundamental-region-existence
source_book: gtm041
source_chapter: "2"
source_section: "2.3"
---

**Proof.** Let $\omega_1' = 1$, $\omega_2' = \tau'$ and apply Lemma 1 to the set of periods $\Omega = \{m + n\tau' : m, n \text{ integers}\}$. Then there exists a fundamental pair $(\omega_1, \omega_2)$ equivalent to $(1, \tau')$ with
$$\begin{pmatrix} \omega_2 \\ \omega_1 \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} \tau' \\ 1 \end{pmatrix}, \quad ad - bc = 1,$$
and satisfying $|\omega_2| \geq |\omega_1|$ and $|\omega_1 \pm \omega_2| \geq |\omega_2|$. Let $\tau = \omega_2/\omega_1$. Then $\tau \in H$ and
$$\tau = \frac{a\tau' + b}{c\tau' + d},$$
so $\tau$ is equivalent to $\tau'$ under $\Gamma$. Moreover, the inequalities on $\omega_1, \omega_2$ become
$$|\tau| \geq 1, \quad |\tau + 1| \geq |\tau|, \quad |\tau - 1| \geq |\tau|.$$

To show that no two distinct interior points of the fundamental region $R_{\Gamma}$ are equivalent under $\Gamma$, suppose both $\tau$ and $\tau'$ are equivalent interior points of $R_{\Gamma}$. Then
$$\tau' = \frac{a\tau + b}{c\tau + d} \quad \text{and} \quad \tau = \frac{d\tau' - b}{-c\tau' + a}.$$

If $\tau \in R_{\Gamma}$ and $c \neq 0$ we have
$$|c\tau + d|^2 = (c\tau + d)(c\bar{\tau} + d) = c^2\tau\bar{\tau} + cd(\tau + \bar{\tau}) + d^2 > c^2 - |cd| + d^2.$$
If $d = 0$ we find $|c\tau + d|^2 > c^2 \geq 1$. If $d \neq 0$ we have
$$c^2 - |cd| + d^2 = (|c| - |d|)^2 + |cd| \geq |cd| \geq 1$$
so again $|c\tau + d|^2 > 1$. Therefore $c \neq 0$ implies $|c\tau + d|^2 > 1$ and hence $\operatorname{Im}(\tau') < \operatorname{Im}(\tau)$. In other words, every element $A$ of $\Gamma$ with $c \neq 0$ decreases the ordinate of each point $\tau$ in $R_{\Gamma}$.

If $c \neq 0$ we would have both $\operatorname{Im}(\tau') < \operatorname{Im}(\tau)$ and $\operatorname{Im}(\tau) < \operatorname{Im}(\tau')$, a contradiction. Therefore $c = 0$, so $ad = 1$, $a = d = \pm 1$, and
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} \pm 1 & b \\ 0 & \pm 1 \end{pmatrix} = T^{\pm b}.$$
But then $b = 0$ since both $\tau$ and $\tau'$ are in $R_{\Gamma}$, so $\tau = \tau'$. This proves that no two distinct points of $R_{\Gamma}$ are equivalent under $\Gamma$. $\square$
