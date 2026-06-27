---
role: proof
locale: en
of_concept: convenient-number-primality-conditions
source_book: gtm050
source_chapter: "7"
source_section: "7.10"
---

Assume without loss of generality that $a = p_1 p_2 \cdots p_n$ is odd. Then $ak$ is the norm of a principal divisor of the form $(p_1, *)(p_2, *)\cdots(p_n, *)A$.

Under the hypothesis that each genus contains only one class, the divisor class group has the property that every genus is a single class. The conditions (1)-(3) then characterize when the divisor of $x + y\sqrt{-ab}$ is prime, which is equivalent to $k = ax^2 + by^2$ being prime.

The sufficiency proof: if $k$ satisfies conditions (1)-(3) but were composite, then its divisor would factor nontrivially, contradicting the genus hypothesis. The necessity is direct from the definition of primality of the norm.

More concretely: if $k$ is not prime, then the divisor of $x + y\sqrt{-ab}$ factors as $A_1 A_2$ with $A_1, A_2$ relatively prime, or as a power of a prime divisor $(p, u)^n$ with $n > 1$. In either case, one derives a contradiction with condition (3), using that each genus contains only one class, so distinct equivalent divisors must be principal multiples of one another.
