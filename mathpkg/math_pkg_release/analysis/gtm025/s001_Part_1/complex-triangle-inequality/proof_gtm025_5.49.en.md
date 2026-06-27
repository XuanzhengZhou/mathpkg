---
role: proof
locale: en
of_concept: complex-triangle-inequality
source_book: gtm025
source_chapter: "5"
source_section: "5.49"
---

Applying (5.47) and (5.48), we write
$$|z + w|^2 = (z + w)(\bar{z} + \bar{w}) = z\bar{z} + w\bar{w} + z\bar{w} + \bar{z}w = |z|^2 + |w|^2 + 2\operatorname{Re}(z\bar{w}) \leq |z|^2 + |w|^2 + 2|z\bar{w}| = |z|^2 + |w|^2 + 2|z||w| = (|z| + |w|)^2.$$
This shows $|z + w| \leq |z| + |w|$. Equality holds iff $\operatorname{Re}(z\bar{w}) = |z\bar{w}|$, i.e., iff $z\bar{w}$ is a nonnegative real number, which is equivalent to the stated condition.
