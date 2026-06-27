---
role: proof
locale: en
of_concept: kernel-cokernel-exact-sequence
source_book: gtm004
source_chapter: "III"
source_section: "5"
---

# Proof of Kernel-Cokernel Exact Sequence (Lemma 5.1)

Let the following commutative diagram have exact rows:

$$
\begin{array}{cccccc}
A' & \xrightarrow{\mu'} & B' & \xrightarrow{\varepsilon'} & C' & \rightarrow & 0 \\
\downarrow \alpha & & \downarrow \beta & & \downarrow \gamma & & \\
A & \xrightarrow{\mu} & B & \xrightarrow{\varepsilon} & C & \rightarrow & 0
\end{array}
$$

It is very easy to see that the final sentence holds and that we have exact sequences

$$
\ker \alpha \xrightarrow{\mu_*} \ker \beta \xrightarrow{\varepsilon_*} \ker \gamma,
$$

$$
\operatorname{coker} \alpha \xrightarrow{\mu_*'} \operatorname{coker} \beta \xrightarrow{\varepsilon_*'} \operatorname{coker} \gamma.
$$

It therefore remains to show that there exists a homomorphism $\omega : \ker \gamma \rightarrow \operatorname{coker} \alpha$ "connecting" these two sequences. In fact, $\omega$ is defined as follows.

Let $c \in \ker \gamma$, choose $b \in B$ with $\varepsilon b = c$. Since

$$
\varepsilon' \beta b = \gamma \varepsilon b = \gamma c = 0,
$$

there exists $a' \in A'$ with $\beta b = \mu' a'$. Define $\omega(c) = [a']$, the coset of $a'$ in $\operatorname{coker} \alpha$.

One verifies that $\omega$ is well-defined (independent of the choice of $b$) and that with this definition the sequence (5.1)

$$
\ker \alpha \xrightarrow{\mu_*} \ker \beta \xrightarrow{\varepsilon_*} \ker \gamma \xrightarrow{\omega} \operatorname{coker} \alpha \xrightarrow{\mu_*'} \operatorname{coker} \beta \xrightarrow{\varepsilon_*'} \operatorname{coker} \gamma
$$

is exact. If $\mu$ is monomorphic, so is $\mu_*$; if $\varepsilon'$ is epimorphic, so is $\varepsilon_*'$.

For an elegant proof using Lemma 3.1, see Exercise 5.1.
