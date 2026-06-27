---
role: proof
locale: en
of_concept: congruence-kummer-equivalence
source_book: gtm050
source_chapter: "4"
source_section: "4.3"
---

Since $\alpha \equiv k \pmod{h(\alpha)}$ and congruences can be added and multiplied, we have $f(\alpha) \equiv f(k) \pmod{h(\alpha)}$ for any cyclotomic integer $f(\alpha)$. Similarly, $g(\alpha) \equiv g(k) \pmod{h(\alpha)}$.

Now $f(k)$ and $g(k)$ are ordinary integers. An integer $m$ is divisible by $h(\alpha)$ if and only if $m \equiv 0 \pmod{p}$, because $h(\alpha)$ divides $p = Nh(\alpha)$. More generally, for two integers $a, b$, we have $a \equiv b \pmod{h(\alpha)}$ if and only if $a \equiv b \pmod{p}$.

Applying this to $a = f(k)$ and $b = g(k)$, we obtain

$$f(k) \equiv g(k) \pmod{h(\alpha)} \iff f(k) \equiv g(k) \pmod{p}.$$

Combining with $f(\alpha) \equiv f(k) \pmod{h(\alpha)}$ and $g(\alpha) \equiv g(k) \pmod{h(\alpha)}$, transitivity yields the desired equivalence:

$$f(\alpha) \equiv g(\alpha) \pmod{h(\alpha)} \iff f(k) \equiv g(k) \pmod{p}.$$
