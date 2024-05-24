## Introduction

The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is `GA-DE-RY-PO-LU-KI`.

```
 G => A
 g => a
 a => g
 A => G
 D => E
  etc.
```

The letters, which are not on the list of substitutes, stays in the encrypted text without changes.

## Task

Your task is to help scouts to encrypt and decrypt thier messages. Write the `encode()` and `decode()` functions.

The input string consists of lowercase and uperrcase characters and spaces. The substitution should be case-sensitive.

## Example
```
 encode("ABCD")          // => GBCE 
 encode("Ava has a cat") // => Gug hgs g cgt 
 encode("gaderypoluki"); // => agedyropulik
 decode("Gvg hgs g cgt") // => Ava has a cat 
 decode("agedyropulik")  // => gaderypoluki
 decode("GBCE")          // => ABCD
```