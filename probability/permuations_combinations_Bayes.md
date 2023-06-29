Everyone knows learning math is so boring. I dont know how I manage to persuade that math is not difficult and interesting.
Maybe just because ,emmm,I am an intp which is like a robot character. I think I like programmers.
I copy their notes and I hate taking notes(I don;t know how they manage to say so many words about math or cs.They must have no requirements to work overtime).
But anyway,I have learned it and I need to leave some footprints.
Somtimes I think when I am 35,I bet I can understand most papers I am interested in.
But whenever I see something all English and filled with math and cs,I think it is pretty cool.
### Combinations
Sometimes, we want to count all of the possible ways that a single set of objects can be selected - without regard to the order in which they are selected.

In general, n objects can be arranged in n(n - 1)(n - 2) ... (3)(2)(1) ways. This product is represented by the symbol n!, which is called n factorial. (By convention, 0! = 1.)
A combination is a selection of all or part of a set of objects, without regard to the order in which they were selected. This means that XYZ is considered the same combination as ZYX.
The number of combinations of n objects taken r at a time is denoted by nCr.
Rule 1. The number of combinations of n objects taken r at a time is

nCr = n(n - 1)(n - 2) ... (n - r + 1)/r! = n! / r!(n - r)!

Example 1
How many different ways can you select 2 letters from the set of letters: X, Y, and Z? (Hint: In this problem, order is NOT important; i.e., XY is considered the same selection as YX.)

Solution: One way to solve this problem is to list all of the possible selections of 2 letters from the set of X, Y, and Z. They are: XY, XZ, and YZ. Thus, there are 3 possible combinations.

Rule 1 tells us that the number of combinations is n! / r!(n - r)!. We have 52 cards in the deck so n = 52. And we want to arrange them in groups of 5, so r = 5. Thus, the number of combinations is:

52C5 = 52! / 5!(52 - 5)! or 52! / 5!47! = 2,598,960
### Permutations
A permutation is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. This means that XYZ is considered a different permutation than ZYX.
The number of permutations of n objects taken r at a time is denoted by nPr.
Rule 2. The number of permutations of n objects taken r at a time is

nPr = n(n - 1)(n - 2) ... (n - r + 1) = n! / (n - r)!
In horse racing, a trifecta is a type of bet. To win a trifecta bet, you need to specify the horses that finish in the top three spots in the exact order in which they finish. If eight horses enter the race, how many different ways can they finish in the top three spots?

Solution: Rule 2 tells us that the number of permutations is n! / (n - r)!. We have 8 horses in the race. so n = 8. And we want to arrange them in groups of 3, so r = 3. Thus, the number of permutations is 8! / (8 - 3)! or 8! / 5!. This is equal to (8)(7)(6) = 336 distinct trifecta outcomes. With 336 possible permutations, the trifecta is a difficult bet to win.

8P3 = 8! / (8 - 3)! or 8! / 5! = (8)(7)(6) = 336
Home
>
Probability tutorial
>
This page
Combinations and Permutations
The solution to many statistical experiments involves being able to count the number of points in a sample space. Counting points can be hard, tedious, or both.

Fortunately, there are ways to make the counting task easier. This lesson focuses on three rules of counting that can save both time and effort - combinations, permutations, and event multiples.

Combinations
Sometimes, we want to count all of the possible ways that a single set of objects can be selected - without regard to the order in which they are selected.

In general, n objects can be arranged in n(n - 1)(n - 2) ... (3)(2)(1) ways. This product is represented by the symbol n!, which is called n factorial. (By convention, 0! = 1.)
A combination is a selection of all or part of a set of objects, without regard to the order in which they were selected. This means that XYZ is considered the same combination as ZYX.
The number of combinations of n objects taken r at a time is denoted by nCr.
Rule 1. The number of combinations of n objects taken r at a time is

nCr = n(n - 1)(n - 2) ... (n - r + 1)/r! = n! / r!(n - r)!

Example 1
How many different ways can you select 2 letters from the set of letters: X, Y, and Z? (Hint: In this problem, order is NOT important; i.e., XY is considered the same selection as YX.)

Solution: One way to solve this problem is to list all of the possible selections of 2 letters from the set of X, Y, and Z. They are: XY, XZ, and YZ. Thus, there are 3 possible combinations.

Another approach is to use Rule 1. Rule 1 tells us that the number of combinations is n! / r!(n - r)!. We have 3 distinct objects so n = 3. And we want to arrange them in groups of 2, so r = 2. Thus, the number of combinations is:

3C2 = 3! / 2!(3 - 2)! = 3! /2!1! = (3)(2)(1)/(2)(1)(1) = 3

Advertisement

Example 2
Five-card stud is a poker game, in which a player is dealt 5 cards from an ordinary deck of 52 playing cards. How many distinct poker hands could be dealt? (Hint: In this problem, the order in which cards are dealt is NOT important; For example, if you are dealt the ace, king, queen, jack, ten of spades, that is the same as being dealt the ten, jack, queen, king, ace of spades.)

Solution: For this problem, it would be impractical to list all of the possible poker hands. However, the number of possible poker hands can be easily calculated using Rule 1.

Rule 1 tells us that the number of combinations is n! / r!(n - r)!. We have 52 cards in the deck so n = 52. And we want to arrange them in groups of 5, so r = 5. Thus, the number of combinations is:

52C5 = 52! / 5!(52 - 5)! or 52! / 5!47! = 2,598,960

Hence, there are 2,598,960 distinct poker hands.

Combination and Permutation Calculator
Use Stat Trek's Combination and Permutation Calculator to (what else?) compute combinations and permutations. The calculator is free and easy to use. You can find the Combination and Permutation Calculator in Stat Trek's main menu under the Stat Tools tab. Or you can tap the button below.

Combinations and Permutations
Permutations
Often, we want to count all of the possible ways that a single set of objects can be arranged. For example, consider the letters X, Y, and Z. These letters can be arranged a number of different ways (XYZ, XZY, YXZ, etc.) Each of these arrangements is a permutation.

A permutation is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. This means that XYZ is considered a different permutation than ZYX.
The number of permutations of n objects taken r at a time is denoted by nPr.
Rule 2. The number of permutations of n objects taken r at a time is

nPr = n(n - 1)(n - 2) ... (n - r + 1) = n! / (n - r)!

Example 1
How many different ways can you arrange the letters X, Y, and Z? (Hint: In this problem, order is important; i.e., XYZ is considered a different arrangement than YZX.)

Solution: One way to solve this problem is to list all of the possible permutations of X, Y, and Z. They are: XYZ, XZY, YXZ, YZX, ZXY, and ZYX. Thus, there are 6 possible permutations.

Another approach is to use Rule 2. Rule 2 tells us that the number of permutations is n! / (n - r)!. We have 3 distinct objects so n = 3. And we want to arrange them in groups of 3, so r = 3. Thus, the number of permutations is:

3P3 = 3! / (3 - 3)! = 3! / 0! = (3)(2)(1)/1 = 6

Example 2
In horse racing, a trifecta is a type of bet. To win a trifecta bet, you need to specify the horses that finish in the top three spots in the exact order in which they finish. If eight horses enter the race, how many different ways can they finish in the top three spots?

Solution: Rule 2 tells us that the number of permutations is n! / (n - r)!. We have 8 horses in the race. so n = 8. And we want to arrange them in groups of 3, so r = 3. Thus, the number of permutations is 8! / (8 - 3)! or 8! / 5!. This is equal to (8)(7)(6) = 336 distinct trifecta outcomes. With 336 possible permutations, the trifecta is a difficult bet to win.

8P3 = 8! / (8 - 3)! or 8! / 5! = (8)(7)(6) = 336

Conclusion: With 336 possible permutations, the trifecta is a difficult bet to win.

How are combinations and permutations related?
Combinations and permutations are related according to the following formulas:

nPr = nCr * r!      and      nCr = nPr / r!

### Event Multiples
The third rule of counting deals with event multiples. An event multiple occurs when two or more independent events are grouped together. The third rule of counting helps us determine how many ways an event multiple can occur.

Rule 3. Suppose we have k independent events. Event 1 can be performed in n1 ways; Event 2, in n2 ways; and so on up to Event k (which can be performed in nk ways). The number of ways that these events can be performed together is equal to n1n2 . . . nk ways.

Example 1
How many sample points are in the sample space when a coin is flipped 4 times?

Solution: Each coin flip can have one of two outcomes - heads or tails. Therefore, the four coin flips can land in (2)(2)(2)(2) = 16 ways.
