---
role: proof
locale: en
of_concept: turing-computable-implies-partial-turing-computable
source_book: gtm037
source_chapter: "5"
source_section: "1"
---

If $f$ is Turing computable, then by Definition 3.1 there is a Turing machine $M$ that computes $f$ on all inputs. The same machine $M$ witnesses that $f$ is partial Turing computable according to Definition 5.1, with the domain of $f$ being all of ${}^m\omega$.

Conversely, if $f$ is partial Turing computable and total (i.e., $\text{Dmn } f = {}^m\omega$), then condition (ii) of Definition 5.1 holds for every $m$-tuple, so the machine $M$ halts on all inputs and produces the value $f(x_0, \ldots, x_{m-1})$. Thus $f$ satisfies the definition of a Turing computable function.
