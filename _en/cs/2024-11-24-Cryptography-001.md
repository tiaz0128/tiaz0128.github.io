---
title: "Symmetric and Asymmetric Keys"
description: "An intuitive explanation of how encryption works and how it's used, from what symmetric and asymmetric keys are and how they differ to a real-world example (GitHub SSH)."
subtitle: "The basics of cryptography! Symmetric and asymmetric keys"
ref-link:
  - type: youtube
    url: 'https://youtu.be/MR4sCU82tgo?si=TVrWz4WguRCkEL1O'
    title: 'Saenghwal Coding: Cryptography 1 - 4.1. Two-Way Encryption - Asymmetric Keys (Public-Key Method) (Korean)'
  - type: youtube
    url: "https://youtu.be/itlJrSUNSMw?si=Wn5ADjLjP779FUUo&t=583"
    title: 'Sparta Institute: "Able to Hack the Whole World" With Quantum Computers ... | Prof. Kim Beom-jun (Korean)'
---

## The Three Pillars of Information Security

To understand cryptography, you first need to know the 'three pillars of information security', commonly called the 'CIA' triad.

- Confidentiality : secret information known only to authorized users.
- Integrity : information that hasn't been altered from the original, or that is changed only by authorized means.
- Availability : guaranteeing that authorized users can use the information without disruption whenever they need it.

The purpose of cryptography is to guarantee 'confidentiality' by encrypting data, and additionally to provide 'integrity', a guarantee about whether data has been changed.

## Encryption and Decryption

We said that 'the purpose of cryptography is encrypting data'. So what exactly is encryption?

![Encryption and decryption](/assets/img/content/cs/Cryptography/001.webp)

`> Encryption and decryption`{:.img-caption}

'Encryption' means taking plaintext, an ordinary message, and using an encryption algorithm to turn it into a coded message, ciphertext, that can't be understood.

Conversely, 'decryption' means turning the ciphertext back into plaintext.

## Types of Ciphers

Ciphers can be broadly divided into 'two-way ciphers' and 'one-way ciphers'. 'Direction' here refers to encryption and decryption: two-way ciphers can both encrypt and decrypt, while one-way ciphers can only encrypt.

![Types of ciphers](/assets/img/content/cs/Cryptography/002.webp){:.img-m}

`> Symmetric and asymmetric keys are two-way ciphers.`{:.img-caption}

## Confusion and Diffusion

The basic techniques behind all encryption can be broadly divided into 'confusion' and 'diffusion'.

![Caesar cipher, Scytale cipher](/assets/img/content/cs/Cryptography/003.webp)

`> Caesar cipher, Scytale cipher`{:.img-caption}

### Confusion

Confusion means replacing the characters of the plaintext with other letters, numbers, signs or symbols. The classic example is the `Caesar` technique.

Used by the Roman emperor Julius Caesar, this method writes A as D, B as E and so on; to read it, you shift each letter back by three to recover the original plaintext.

### Diffusion

Diffusion is a technique that changes the positions of the letters. The classic example is the `Scytale` technique.

You wrap a strip of paper around a rod of a certain diameter and write the plaintext across it; when you unwind the paper, the letters are rearranged and the message can't be read. Wrap it around a rod of the same diameter again and you can read the plaintext.

## Key Management

- In the `Caesar` technique, the agreement to shift each letter by three
- In the `Scytale` technique, the diameter of the rod

These are the keys needed to turn the ciphertext back into plaintext.

You could say the most important thing in encryption is 'building a strong algorithm'. But no matter how strong an encryption algorithm is, it's useless if someone knows the key used for it.

So it's fair to say that **'how to manage the key safely'** is also at the heart of encryption.

## Symmetric-key Cryptography

A typical cipher encrypts plaintext with a key and decrypts the ciphertext with the same key, which is what we call a 'symmetric key'. 'Symmetric key' means the same key is used for both encryption and decryption.

![Symmetric-key encryption](/assets/img/content/cs/Cryptography/006.webp)

`> Symmetric key: the black key used for encryption is used again for decryption`{:.img-caption}

Following the usual convention in cryptography, we'll call 'sender A' Alice and 'receiver B' Bob.

Imagine the two of them communicating with encryption using the same key. Alice encrypts the plaintext with the key and sends it, and Bob decrypts the ciphertext with the same key, so they can communicate securely.

But there's a basic prerequisite for the two of them to communicate this way.

> 'To communicate with encryption, the sender and receiver must share the same key.'

This is where the problem comes in.

## Sharing the Key

![The key distribution problem](/assets/img/content/cs/Cryptography/007.webp)

`> Risk of the key being stolen through eavesdropping (the key distribution problem)`{:.img-caption}

If Alice doesn't send the key to Bob, Bob can't decrypt the ciphertext he receives from her into plaintext. But if she does try to send the key, a hacker waiting for it could steal the key and decrypt the ciphertext.

This is fatal to 'confidentiality', the most important property of encryption. "We need to share the key, but we can't even send it." This is called the **'key distribution problem'**{:.orange}.

And we can't make every communication channel 100% secure, either. So how can we share a key safely over an 'insecure communication channel'?

## Asymmetric-key Cryptography

There are a few ways to solve the 'key distribution problem'. The best known is 'asymmetric-key encryption'.

In this approach, there is one key for encryption and a separate key for decryption. Because the keys used for encryption and decryption differ, it's called 'asymmetric'. The two keys are:

- 'A key anyone can see' = 'public key'
- 'A key only you hold' = 'private key'

There's one more important thing to remember. Anything encrypted with the private key or the public key can only be decrypted with the other key.

- What's encrypted with the public key can only be decrypted with the private key
- What's encrypted with the private key can only be decrypted with the public key

In other words, both keys can be used for encryption/decryption, but **only the opposite key can undo what the other did.**{:.orange}

![Asymmetric-key encryption](/assets/img/content/cs/Cryptography/014.webp){:.img-m}

`> Asymmetric key : encrypting and decrypting with two keys`{:.img-caption}

The basic flow looks like this:

1. Alice uses 'Bob's public key' to 'encrypt' the plaintext.
2. Bob 'decrypts' the received ciphertext using 'Bob's private key'.

Because of this idea of a public key, it's also called 'public-key cryptography'.

## When to Use Symmetric vs. Asymmetric Keys

So does all the encryption we use rely only on asymmetric keys? That's half right and half wrong.

**Asymmetric keys** rely on a heavy computation, 'prime factorization'. That's why **they aren't well suited to encrypting large amounts of data.**{:.orange} Symmetric keys, on the other hand, encrypt and decrypt much faster.

> "Wait, what? Then if they're not for encrypting data, what are they for?"

Of course, there are plenty of cases where asymmetric keys are used on their own. When encrypting data isn't the goal, they're a perfectly good fit, and many technologies already use them. The classic case is the 'digital signature'. Its goal isn't to encrypt data; **its main purpose is to verify integrity (whether the data has been tampered with)**{:.orange}.

## Using Asymmetric Keys for Symmetric Keys

Let's sum up the pros and cons of symmetric and asymmetric keys once more.

|   | Pros | Cons |
|----------|
| Symmetric key | Fast and efficient | Hard to share the key|
| Asymmetric key | Secure key sharing | High computational cost|

Neither one seems quite enough on its own. So in practice, **the two approaches are often combined.**{:.orange}

## Example : GitHub SSH Setup

{% include template/link.html
  type="note"
  about="GitHub SSH setup"
  url="/GitHub/1"
  title="Connecting to GitHub over SSH"
%}

Think about setting up SSH for GitHub. You create an asymmetric key pair yourself, keep the private key, and register the public key with GitHub.

- The public key on the GitHub server
- The private key that only you hold

![GitHub public key setup](/assets/img/content/cs/Cryptography/013.webp){:.img-m}

`> Anyone can see the public key a user registered with GitHub`{:.img-caption}

### Initial Connection Setup (Using Asymmetric Keys)

1. The user creates an asymmetric key pair, keeps the private key and registers the public key with GitHub
2. The user and GitHub generate the same symmetric key (session key) to use for SSH (Diffie-Hellman key exchange)
3. The user creates a signature with the private key and sends it to the GitHub server
4. The GitHub server verifies the signature by decrypting it with the public key

![Asymmetric key](/assets/img/content/cs/Cryptography/015.webp){:.img-m}

`> The symmetric key is encrypted with the asymmetric key and delivered safely.`{:.img-caption}

If the private key isn't the pair of the public key registered with GitHub, authentication fails. Only someone with the right private key can get through, right?

### Subsequent Communication (Using the Symmetric Key)

Since both sides now share the same session key, all further communication can safely encrypt/decrypt data with this symmetric key. This is a common pattern used not only in SSH but in many security protocols, including HTTPS.

![Using the symmetric key](/assets/img/content/cs/Cryptography/016.webp){:.img-m}

## Wrapping Up

That's our look at symmetric and asymmetric keys. Let's sum it up. 😊

- Symmetric keys have the 'key distribution problem'.
- Asymmetric keys aren't suited to encrypting data.
- The two are combined so each one's strengths cover the other's weaknesses

## References

The videos below explain the basic principle of public keys and how they work through 'prime factorization' really well, so I recommend giving them a watch! (Note: the videos are in Korean.)

{% include template/ref.html refs=page.ref-link %}
