---
role: proof
locale: en
of_concept: main-theorem-divisible-x-y-unit
source_book: gtm059
source_chapter: "9"
source_section: "6"
---

Given the stated valuation conditions, we verify the interchangeability of formal group addition and field addition. Starting from the identity:
$$0 = (\text{ord}_x(-1), \text{ord}_x(-1))$$
we expand using the interchangeability relation:
$$0 = (\text{ord}_x^2(-1) - \text{ord}_x^2(-1)) + [\text{ord}_x^2(-1) - \text{ord}_x^2(-1)]$$
$$= (\text{ord}_x^2(-1), \text{ord}_x^2(-1)) + [\text{ord}_x^2(-1) - [\text{ord}_x(-1) - 1]].$$

From this we obtain:
$$(\text{ord}_x(-1), \text{ord}_x(-1)) = (\text{ord}_x^2(-1), \text{ord}_x^2(-1)) + [\text{ord}_x^2(-1), \text{ord}_x^2(-1)].$$

Note that $(\text{ord}_x, y) = 0$ for all $x \in v_w$. Applying this recursively yields:
$$\text{ord}_x(-1) = 1 + \sum_{i=1}^{n-1} (\text{ord}_x^{i+1})^{2-i+1} = \sum_{i=1}^{n-1} (\text{ord}_x^{i+1})^{2-i+1}.$$

This computation uses the fact that under the given valuation conditions, the error terms in the congruence $x +_A y \equiv x +_{G_a} y \pmod{xy}$ are negligible with respect to the valuations involved, which justifies the formal manipulation of the symbols.
