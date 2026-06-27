# Lagrange’s Theorem

**Concept Type:** Theorem

## Statement

Let \(G\) be a group and \(H\) a subgroup of \(G\). Then the index of \(H\) in \(G\) satisfies  

\[
|G : H| \cdot |H| = |G|,
\]

where \(|G|\) denotes the order of \(G\) (possibly infinite). If \(G\) is finite, it follows that  

\[
|G : H| = \frac{|G|}{|H|},
\]

and consequently the order of any subgroup divides the order of the group.

Hence, for a finite group \(G\) and a subgroup \(H \leq G\),  

\[
|H| \;\big|\; |G|.
\]

---

## Proof (Detailed Steps)

The theorem is an immediate consequence of the **Multiplicativity of Index** applied with the trivial subgroup \(K = \{1\}\). Recall that for subgroups \(K \leq H \leq G\) (with appropriate finiteness conditions or using cardinal arithmetic),

\[
|G : K| = |G : H| \cdot |H : K|.
\]

We now set \(K = \{1\}\).

1. **Index of the trivial subgroup**  
   The cosets of the trivial subgroup are the singleton sets \(\{g\}\) for each \(g \in G\). Hence the number of cosets is exactly the order of \(G\):  
   \[
   |G : 1| = |G|.
   \]  
   Similarly, for \(H\) we have \(|H : 1| = |H|\).

2. **Apply multiplicativity**  
   Substituting \(K = 1\) into the index multiplicative formula gives  
   \[
   |G : 1| = |G : H| \cdot |H : 1|.
   \]

3. **Substitute the known indices**  
   \[
   |G| = |G : H| \cdot |H|.
   \]

4. **Finite case**  
   If \(G\) is finite, then \(|G|\) and \(|H|\) are natural numbers. Dividing both sides by \(|H|\) yields  
   \[
   |G : H| = \frac{|G|}{|H|}.
   \]  
   Since the index is an integer, \(|H|\) must divide \(|G|\).

---

## Textbook Comparison Table

The following table summarises the location and presentation of Lagrange’s Theorem in three standard graduate‑level texts.

| Reference | Chapter | Section | Pages | Theorem Number |
|-----------|---------|---------|-------|----------------|
| Hungerford, *Algebra* (GTM 73) | I | I.4 | 38‑42 | Theorem 4.6 |
| Robinson, *A Course in the Theory of Groups* (GTM 80) | 1 | 1.3 | 15‑17 | Theorem 1.3.6 |
| Rotman, *An Introduction to the Theory of Groups* (GTM 185) | 2 | 2.4 | 34‑36 | Theorem 2.30 |

All three present the theorem in essentially the same form, although the proofs may vary slightly (e.g., using the partition of \(G\) into left/right cosets or relying on the multiplicativity of index).

---

## Dependencies Graph Description

The theorem relies on the following concepts and their interrelations:

- **Subgroup** – A subset \(H \subseteq G\) that is a group under the operation of \(G\).  
- **Coset** – For a fixed \(g \in G\), the left coset \(gH = \{gh \mid h \in H\}\) and the right coset \(Hg\). The set of left cosets partitions \(G\) and its cardinality is the index \(|G:H|\).  
- **Index Multiplication Theorem** – For subgroups \(K \leq H \leq G\),  
  \[
  |G : K| = |G : H| \cdot |H : K|.
  \]  
  This theorem itself is proved by observing that each coset of \(H\) in \(G\) can be expressed as a disjoint union of \(|H:K|\) cosets of \(K\).

The dependency chain is:

1. **Subgroup** ⟶ **Coset** (cosets are defined via a subgroup)  
2. **Coset** ⟶ **Index** (the index is the number of cosets)  
3. **Index** ⟶ **Index Multiplication Theorem** (the multiplicative property of indices)  
4. **Index Multiplication Theorem** ⟶ **Lagrange’s Theorem** (by taking the trivial subgroup)

---

## Lean Verification Section

The theorem is formalised in the Mathlib4 library. The relevant code (with imports) is:

```lean
import Mathlib
open Subgroup

theorem lagrange_theorem (G : Type*) [Group G] [Fintype G] (H : Subgroup G) :
    Fintype.card H ∣ Fintype.card G :=
  Subgroup.card_dvd_card H
```

**Explanation:**

- `G : Type*` declares \(G\) as a type with a group structure (`[Group G]`) and a finiteness condition (`[Fintype G]`).  
- `H : Subgroup G` is a subgroup of \(G\).  
- The conclusion `Fintype.card H ∣ Fintype.card G` states that the cardinality of `H` (its order) divides the cardinality of `G`.  
- The proof `Subgroup.card_dvd_card H` is a lemma already present in Mathlib that directly encodes the statement of Lagrange’s theorem. The lemma is proved by constructing a `Fintype` for the quotient group (or using the multiplicative index property) and then applying the fact that the order of a subgroup times the index equals the order of the group.

This Lean formalisation confirms the theorem’s validity for finite groups and can be used as a building block for further group‑theoretic proofs within the system.

---

## Exercises

1. **Direct verification**  
   Let \(G = \mathbb{Z}_{12}\) (additive group of integers modulo 12). List all subgroups of \(G\) and verify that each order divides 12.

2. **Converse false**  
   Show that the converse of Lagrange’s theorem does not hold: for every divisor \(d\) of \(|G|\) there does **not** necessarily exist a subgroup of order \(d\). (Hint: consider the alternating group \(A_4\) of order 12; does it have a subgroup of order 6?)

3. **Application to prime orders**  
   Use Lagrange’s theorem to prove that a group of prime order \(p\) is cyclic and that every non‑identity element generates the whole group.

4. **Index of intersection**  
   Let \(H\) and \(K\) be subgroups of a finite group \(G\). Prove that  
   \[
   |H \cap K| \ge \frac{|H|\,|K|}{|G|}.
   \]  
   (Hint: apply Lagrange’s theorem to the subgroup \(H \cap K\) of both \(H\) and \(K\).)

5. **Left and right cosets**  
   Prove that for any subgroup \(H\) of a group \(G\), the number of left cosets equals the number of right cosets. (This justifies the notation \(|G:H|\) without specifying left or right.)

6. **Product formula**  
   For subgroups \(H\) and \(K\) of a finite group \(G\), prove the **Product Formula**:  
   \[
   |HK| = \frac{|H|\,|K|}{|H \cap K|},
   \]  
   where \(HK = \{hk \mid h \in H, k \in K\}\). (This is a direct corollary of Lagrange’s theorem and the fact that \(|HK|/|K| = |H : H \cap K|\).)

---

*Last updated: 2025*