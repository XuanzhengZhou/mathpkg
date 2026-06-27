---
role: proof
locale: en
of_concept: "suppose-that-for-all-then-if-we-have"
source_book: gtm025
source_chapter: "Further Topics"
source_section: "22.25"
---

It is obvious that $\lim_{n \to \infty} \prod_{k=1}^{n}(1 - \alpha_k)$ exists. For $

$F$ be the set $\bigcap_{n=1}^{\infty} \left( \bigcup_{k=n}^{\infty} E_k \right)$. Then we have

$$\mu(F) = \begin{cases} 
0 \text{ if } \sum_{n=1}^{\infty} \mu_n(E^{(n)}) < \infty, \\
1 \text{ if } \sum_{n=1}^{\infty} \mu_n(E^{(n)}) = \infty.
\end{cases}$$

Proof. The set $F$ plainly satisfies the hypotheses of (22.21), and so $\mu(F)$ must be 0 or 1. The present lemma tells us which. It is clear that

$$\mu(F) \leq \mu \left( \bigcup_{k=n}^{\infty} E_k \right) \leq \sum_{k=n}^{\infty} \mu(E_k)$$

for all $n$; therefore $\mu(F) = 0$ if $\sum_{n=1}^{\infty} \mu_n(E^{(n)}) < \infty$. [A like result holds for $\bigcap_{n=1}^{\infty} \left( \bigcup_{k=n}^{\infty} A_k \right)$ where the $A_k$'s are measurable sets in any measure space.]

To prove the second statement, we need our special sets $E_n$. Observing that $F' = \bigcup_{n=1}^{\infty} \left( \bigcup_{k=n}^{\infty} E_k' \right)$ and that $E_k' = (E^{(k)})' \times T_{k'}$, we have

$$\mu(F') = \lim_{n \to \infty} \mu \left( \bigcap_{k=n}^{\infty} E_k' \right) = \lim_{n \to \infty} \mu \left( \bigcup_{k=n}^{\infty} (E^{(k)})' \times T_1 \times \cdots \times T_{n-1} \right)$$

$$= \lim_{n \to \infty} \prod_{k=n}^{\infty} \mu_k((E^{(k)})') = \lim_{n \to \infty} \prod_{k=n}^{\infty} (1 - \mu_k(E^{(k)}
Graduate Texts
in Mathematics

Edwin Hewitt
Karl Stromberg

Real and Abstract
Analysis

Springer-Verlag

Real and Abstract Analysis

A Modern Treatment of the Theory of Functions of a Real Variable

Springer-Verlag New York Heidelberg Berlin

Edwin Hewitt
University of Washington
Department of Mathematics
Seattle, Washington 98105

Karl Stromberg
Kansas State University
Department of Mathematics
Manhattan, Kansas 66502

Managing Editor

P. R. Halmos
Indiana University
Department of Mathematics
Swain Hall East
Bloomington, Indiana 47401

Editors

F. W. Gehring
University of Michigan
Department of Mathematics
Ann Arbor, Michigan 48104

C. C. Moore
University of California at Berkeley
Department of Mathematics
Berkeley, California 94720

AMS Subject Classifications
28-01, 29A10, 28A20, 28A25, 28A30, 28A35, 46-01

Library of Congress Cataloging in Publication Data

Hewitt, Edwin, 1920-
Real and abstract analysis.
(Graduate texts in mathematics; 25)
Includes bibliographical references and indexes.
1. Functions of real variables. 2. Mathematical analysis. I. Stromberg, Karl Robert, 1931-joint author. II. Title. III. Series.
QA331.5.H38 1975 515'.8 75-9898

Third printing: June, 1975

All rights reserved
No part of this book may be translated or reproduced in any form without written permission from Springer-Verlag

© 1965 by Springer-Verlag Berlin Heidelberg

Printed in the United States of America

ISBN 0-387-90138-8 Springer-Verlag New York Heidelberg Berlin
ISBN 3-540-90138-8 Springer-Verlag Berlin Heidelberg New York

This book is dedicated to
MARSHALL H. STONE
whose precept and example have
taught us both.

This Page Intentionally No Longer Blank

Preface

This book is first of all designed as a text for the course usually called "theory of functions of a real variable". This course is at present customarily offered as a first or second year graduate course in United States universities, although there are signs that this sort of analysis will soon penetrate upper division undergraduate curricula. We have included every topic that we think essential for the training of analysts, and we have also gone down a number of interesting bypaths. We hope too that the book will be useful as a reference for mature mathematicians and other scientific workers. Hence we have presented very general and complete versions of a number of important theorems and constructions. Since these sophisticated versions may be difficult for the beginner, we have given elementary avatars of all important theorems, with appropriate suggestions for skipping. We have given complete definitions, explanations, and proofs throughout, so that the book should be usable for individual study as well as for a course text.

Prerequisites for reading the book are the following. The reader is assumed to know elementary analysis as the subject is set forth, for example, in Tom M. Apostol's Mathematical Analysis [Addison-Wesley Publ. Co., Reading, Mass., 1957], or Walter Rudin's Principles of Mathematical Analysis [2nd Ed., McGraw-Hill Book Co., New York, 1964]. There are no other prerequisites for reading the book: we define practically everything else that we use. Some prior acquaintance with abstract algebra may be helpful. The text A Survey of Modern Algebra, by Garrett Birkhoff and Saunders Mac Lane [3rd Ed., MacMillan Co., New York, 1965] contains far more than the reader of this book needs from the field of algebra.

Modern analysis draws on at least five disciplines. First, to explore measure theory, and even the structure of the real number system, one must use powerful machinery from the abstract theory of sets. Second, as hinted above, algebraic ideas and techniques are illuminating and sometimes essential in studying problems in analysis. Third, set-theoretic topology is needed in constructing and studying measures. Fourth, the theory of topological linear spaces ["functional analysis"] can often be applied to obtain fundamental results in analysis, with surprisingly little effort. Finally, analysis really is analysis. We

bers, is indispensable to the training of every mathematician. All five of these subjects thus find a place in our book. To make the book useful to probabilists, statisticians, physicists, chemists, and engineers, we have included many "applied" topics: Hermite functions; Fourier series and integrals, including PLANCHEREL's theorem and pointwise summability; the strong law of large numbers; a thorough discussion of complex-valued measures on the line. Such applications of the abstract theory are also vital to the pure mathematician who wants to know where his subject came from and also where it may be going.

With only a few exceptions, everything in the book has been taught by at least one of us at least once in our real variables courses, at the Universities of Oregon and Washington. As it stands, however, the book is undoubtedly too long to be covered in a one-year course. We offer the following road map for the instructor or individual reader who wants to get to the center of the subject without pursuing byways, even interesting ones.

Chapter One. Sections 1 and 2 should be read to establish our notation. Sections 3, 4, and 5 can be omitted or assigned as outside reading. What is essential is that the reader should have facility in the use of cardinal numbers, well ordering, and the real and complex number fields.

Chapter Two. Section 6 is of course important, but a lecturer should not succumb to the temptation of spending too much time over it. Many students using this text will have already learned, or will be in the process of learning, the elements of topology elsewhere. Readers who are genuinely pressed for time may omit §6 and throughout the rest of the book replace "locally compact Hausdorff space" by "real line", and "compact Hausdorff space" by "closed bounded subset of the real line". We do not recommend this, but it should at least shorten the reading. We urge everyone to cover §7 in detail, except possibly for the exercises.

Chapter Three. This chapter is the heart of the book and must be studied carefully. Few, if any, omissions appear possible. Chapter Three is essential for all that follows, barring §14 and most of §16.

After Chapter Three has been completed, several options are open. One can go directly to

analysis. Section 15, which is an exercise in classical analysis, should be read by everyone who can possibly find the time. We use Theorem (15.11) in our proof of the LEBESGUE-RADON-NIKODYM theorem [§ 19], but as the reader will see, one can get by with much less. Readers who skip § 15 must read § 16 in order to understand § 19.

Chapter Five. Sections 17 and 18 should be studied in detail. They are parts of classical analysis that every student should learn. Of § 19, only subheads (19.1)—(19.24) and (19.35)—(19.44) are really essential. Of § 20, (20.1)—(20.8) should be studied by all readers. The remainder of § 20, while interesting, is peripheral. Note, however, that subheads (20.55)—(20.59) are needed in the refined study of infinite product measures presented in § 22.

Chapter Six. Everyone should read (21.1)—(21.27) at the very least. We hope that most readers will find time to read our presentation of PLANCHEREL’s theorem (21.31)—(21.53) and of the HARDY-LITTLEWOOD maximal theorems (21.74)—(21.83). Section 22 is optional. It is essential for all students of probability and in our opinion, its results are extremely elegant. However, it can be sacrificed if necessary.

Occasionally we use phrases like “obvious on a little thought”, or “a moment’s reflection shows...”. Such phrases mean really that the proof is not hard but is clumsy to write out, and we think that more writing would only confuse the matter. We offer a very large number of exercises, ranging in difficulty from trivial to all but impossible. The harder exercises are supplied with hints. Heroic readers may of course ignore the hints, although we think that every reader will be grateful for some of them. Diligent work on a fairly large number of exercises is vital for a genuine mastery of

are deeply grateful to Mrs. SHANTI THAYIL, who has typed the entire manuscript with real artistry.

Our thanks are also due to the Universities of Oregon and Washington for exemption from other duties and for financial assistance in the preparation of the manuscript. It is a pleasure to acknowledge the great help given us by Springer-Verlag, in their rapid and meticulous publication of the work.

Seattle, Washington

Edwin Hewitt

Eugene, Oregon

Karl R. Stromberg

Table of Contents

Chapter One: Set Theory and Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

This Page Intentionally No Longer Blank

CHAPTER ONE

Set Theory and Algebra

From the logician’s point of view, mathematics is the theory of sets and its consequences. For the analyst, sets and concepts immediately definable from sets are essential tools, and manipulation of sets is an operation he must carry out continually. Accordingly we begin with two sections on sets and functions, containing few proofs, and intended largely to fix notation and terminology and to form a review for the reader in need of one. Sections 3 and 4, on the axiom of choice and infinite arithmetic, are more serious: they contain detailed proofs and are recommended for close study by readers unfamiliar with their contents.

Plainly one cannot study real- and complex-valued functions seriously without knowing what the real and complex number fields are. Therefore, in §5, we give a short but complete construction of these objects. This section may be read, recalled from previous work, or taken on faith.

This text is not rigorous in the sense of proceeding from the axioms of set theory. We believe in sets, and we believe in the rational numbers. Beyond that, we have tried to prove all we say.

§1. The algebra of sets

(1.1) The concept of a set. As remarked above, we take the notion of set as being already known. Roughly speaking, a set [collection, assemblage, aggregate, class, family] is any identifiable collection of objects of any sort. We identify a set by stating what its members [elements, points] are. The theory of sets has been described axiomatically in terms of the notion “member of”. To build the complete theory of sets from these axioms is a long, difficult process, and it is remote from classical analysis, which is the main subject of the present text. Therefore we shall make no effort to be rigorous in dealing with the concept of sets, but will appeal throughout to intuition and elementary logic. Rigorous treatments of the theory of sets can be found in Naive Set Theory by P. Halmos [Princeton, N. J.: D. Van Nostrand Co. 1960] and in Axiomatic Set Theory by P. Suppes [Princeton, N. J.: D. Van Nostrand Co. 1960].

(1.2) Notation. We will usually adhere to the following

A set is often defined by some property of its elements. We will write $\{x : P(x)\}$ [where $P(x)$ is some proposition about $x$] to denote the set of all $x$ such that $P(x)$ is true. We have done nothing here to sharpen the definition of a set, since "property" and "set" are from one point of view synonymous.

If the object $x$ is an element of the set $A$, we will write $x \in A$; while $x \notin A$ will mean that $x$ is not in $A$.

We write $\varnothing$ for the void [empty, vacuous] set; it has no members at all. Thus $\varnothing = \{x : x$ is a real number and $x^2 < 0\} = \{x : x$ is a unicorn in the Bronx Zoo\}, and so on.

For any object $x$, $\{x\}$ will denote the set whose only member is $x$. Similarly, $\{x_1, x_2, \ldots, x_n\}$ will denote the set whose members are precisely $x_1, x_2, \ldots, x_n$.

Throughout this text we will adhere to the following notations: $N$ will denote the set $\{1, 2, 3, \ldots\}$ of all positive integers; $Z$ will denote the set of all integers; $Q$ will denote the set of all rational numbers; $R$ will denote the set of all real numbers; and $K$ will denote the set of all complex numbers. We assume a knowledge on the part of the reader of the sets $N, Z$, and $Q$. The sets $R$ and $K$ are constructed in § 5.

(1.3) Definitions. Let $A$ and $B$ be sets such that for all $x, x \in A$ implies $x \in B$. Then $A$ is called a subset of $B$ and we write $A \subset B$ or $B \supset A$. If $A \subset B$ and $B \subset A$, then we write $A = B$; $A \neq B$ den

For a set $A$, the family of all subsets of $A$ is a well-defined family of sets which is known as the power set of $A$ and is denoted by $\mathcal{P}(A)$. For example, if $A = \{1, 2\}$, then $\mathcal{P}(A) = \{\varnothing, \{1\}, \{2\}, \{1, 2\}\}$.
