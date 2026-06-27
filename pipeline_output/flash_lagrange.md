# Lagrange's Theorem

## Overview

**Lagrange's Theorem** is a fundamental result in group theory that establishes a crucial relationship between the order of a finite group and the orders of its subgroups. Named after the Italian-French mathematician Joseph-Louis Lagrange, the theorem states that for any finite group $G$ and any subgroup $H$ of $G$, the order of $H$ divides the order of $G$. This seemingly simple result has profound implications throughout algebra, providing constraints on possible subgroup structures and serving as a cornerstone for classifying finite groups.

## Statement

**Theorem (Lagrange's Theorem).** Let $G$ be a group and $H$ a subgroup of $G$. Then:

$$|G| = |G : H| \cdot |H|$$

where $|G : H|$ denotes the index of $H$ in $G$ (the number of left cosets of $H$ in $G$). If $G$ is finite, then:

$$|G : H| = \frac{|G|}{|H|}$$

Consequently, the order of any subgroup $H$ of a finite group $G$ divides the order of $G$.

## Proof

### Detailed Proof

**Step 1: Coset Decomposition.** Let $H$ be a subgroup of $G$. The left cosets of $H$ in $G$ partition $G$. That is:

$$G = \bigcup_{i \in I} g_i H$$

where $\{g_i H\}_{i \in I}$ is a collection of distinct left cosets, and $I$ is an index set.

**Step 2: Bijection Between Cosets and $H$.** For any $g \in G$, define the map $\varphi_g: H \to gH$ by $\varphi_g(h) = gh$. This map is:
- **Injective:** If $gh_1 = gh_2$, then by left cancellation, $h_1 = h_2$.
- **Surjective:** For any $gh \in gH$, we have $\varphi_g(h) = gh$.

Thus $|gH| = |H|$ for every coset $gH$.

**Step 3: Counting Elements.** Since the cosets partition $G$ and each has size $|H|$, we have:

$$|G| = (\text{number of cosets}) \times |H| = |G : H| \cdot |H|$$

**Step 4: Finite Case.** If $G$ is finite, then $|G|$, $|H|$, and $|G : H|$ are all finite positive integers. From $|G| = |G : H| \cdot |H|$, we obtain:

$$|G : H| = \frac{|G|}{|H|}$$

Since $|G : H|$ is an integer, $|H|$ must divide $|G|$.

### Alternative Proof via Index Multiplication

The theorem can also be derived from the **Multiplicativity of Index** property. For subgroups $K \leq H \leq G$, we have $|G : K| = |G : H| \cdot |H : K|$. Setting $K = \{e\}$ (the trivial subgroup) gives:

$$|G : \{e\}| = |G : H| \cdot |H : \{e\}|$$

Since $|G : \{e\}| = |G|$ and $|H : \{e\}| = |H|$, we obtain $|G| = |G : H| \cdot |H|$.

## Corollaries and Consequences

1. **Order of Elements:** For any $g \in G$, the order of $g$ divides $|G|$. This follows because $\langle g \rangle$ is a subgroup of $G$ with order equal to the order of $g$.

2. **Prime Order Groups:** If $|G| = p$ where $p$ is prime, then $G$ is cyclic and has no nontrivial proper subgroups. Any non-identity element generates the entire group.

3. **Fermat's Little Theorem:** For any integer $a$ not divisible by prime $p$, $a^{p-1} \equiv 1 \pmod{p}$. This follows from applying Lagrange's theorem to the multiplicative group $\mathbb{Z}_p^\times$.

4. **Converse is False:** The converse of Lagrange's theorem does not hold in general. For example, the alternating group $A_4$ has order 12 but has no subgroup of order 6.

## Textbook Comparison

| Textbook | Reference | Approach | Notable Features |
|----------|-----------|----------|------------------|
| Hungerford (GTM073) | Ch. I, §I.4, pp. 38-42, Thm 4.6 | Coset decomposition | Emphasizes index multiplicativity |
| Robinson (GTM080) | Ch. 1, §1.3, pp. 15-17, Thm 1.3.6 | Coset partition | Includes infinite group case |
| Rotman (GTM185) | Ch. 2, §2.4, pp. 34-36, Thm 2.30 | Coset counting | Discusses converse and counterexamples |

## Dependencies Graph

The proof of Lagrange's theorem relies on the following concepts:

```
Group
  ├── Subgroup
  │     └── Coset (left/right)
  │           ├── Partition of G
  │           ├── Bijection to H
  │           └── Index [G:H]
  └── Index Multiplication Theorem
        └── Lagrange's Theorem
```

**Key Dependencies:**
- **Subgroup:** A subset $H \subseteq G$ closed under the group operation, containing identity and inverses
- **Coset:** For $g \in G$, the set $gH = \{gh : h \in H\}$ forms a left coset
- **Index:** $|G : H|$ is the number of distinct left (or right) cosets of $H$ in $G$
- **Index Multiplication:** For $K \leq H \leq G$, $|G : K| = |G : H| \cdot |H : K|$

## Lean Verification

The theorem is formalized in Mathlib4 as follows:

```lean
import Mathlib
open Subgroup

theorem lagrange_theorem (G : Type*) [Group G] [Fintype G] (H : Subgroup G) :
    Fintype.card H ∣ Fintype.card G :=
  Subgroup.card_dvd_card H
```

**Explanation:**
- `Fintype.card H` returns the order of subgroup $H$
- `Fintype.card G` returns the order of group $G$
- The `∣` symbol denotes divisibility
- `Subgroup.card_dvd_card` is the pre-proven lemma in Mathlib4 that encapsulates Lagrange's theorem

The Lean proof is concise because the library already contains the necessary coset theory and cardinality arguments as lemmas.

## Exercises

### Basic Exercises

1. **Direct Application:** Let $G$ be a group of order 24. What are the possible orders of subgroups of $G$?

2. **Element Orders:** Show that in a group of order 35, every non-identity element has order 5 or 7.

3. **Index Calculation:** If $G$ is a group of order 60 and $H$ is a subgroup of order 12, what is $|G : H|$?

### Intermediate Exercises

4. **Prime Power Groups:** Prove that every group of order $p^2$ (where $p$ is prime) is abelian. (Hint: Use Lagrange's theorem to analyze the center.)

5. **Converse Counterexample:** Show that $A_4$ has order 12 but no subgroup of order 6. (This demonstrates the converse of Lagrange's theorem is false.)

6. **Intersection of Subgroups:** If $H$ and $K$ are subgroups of a finite group $G$, prove that $|H \cap K|$ divides $\gcd(|H|, |K|)$.

### Advanced Exercises

7. **Cauchy's Theorem:** Use Lagrange's theorem to prove that if a prime $p$ divides $|G|$, then $G$ contains an element of order $p$. (Note: This is actually a deeper result requiring more than just Lagrange's theorem.)

8. **Group Actions:** Let $G$ act on a set $X$. For $x \in X$, prove that the size of the orbit $|G \cdot x|$ divides $|G|$.

9. **Normal Subgroups:** If $H$ is a subgroup of index 2 in $G$, prove that $H$ is normal in $G$.

10. **Classification Problem:** Classify all groups of order 6 using Lagrange's theorem and the properties of cyclic groups.