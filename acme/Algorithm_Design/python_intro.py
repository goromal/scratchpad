"""Solutions for the ACME Intro to Python lab.

Run this file with ``python python_intro.py`` to print a greeting and
demonstrate the sphere volume function.
"""


def sphere_volume(r):
    """Return the volume of a sphere of radius r using pi = 3.14159."""
    return 4 / 3 * 3.14159 * r**3


def isolate(a, b, c, d, e):
    """Print five values with wide spacing before the third value."""
    print(a, b, c, sep=" " * 5, end=" ")
    print(d, e, sep=" ")


def first_half(text):
    """Return the first half of a string, excluding a middle character."""
    return text[:len(text) // 2]


def backward(text):
    """Return the characters of a string in reverse order."""
    return text[::-1]


def list_ops():
    """Perform the six list operations from the lab and return the list."""
    items = ["bear", "ant", "cat", "dog"]
    items.append("eagle")
    items[2] = "fox"
    items.pop(1)
    items.sort(reverse=True)
    items[items.index("eagle")] = "hawk"
    items[-1] += "hunter"
    return items


def pig_latin(word):
    """Translate a word using the vowel and consonant rules in the lab."""
    if word[0].lower() in "aeiou":
        return word + "hay"
    return word[1:] + word[0] + "ay"


def palindrome():
    """Return the largest palindrome made from two three-digit factors."""
    largest = 0
    for a in range(999, 99, -1):
        for b in range(a, 99, -1):
            product = a * b
            if product <= largest:
                break
            if str(product) == str(product)[::-1]:
                largest = product
    return largest


def alt_harmonic(n):
    """Sum the first n terms of the alternating harmonic series."""
    return sum([(-1)**(k + 1) / k for k in range(1, n + 1)])


if __name__ == "__main__":
    print("Hello, world!")
    print("Volume of a unit sphere:", sphere_volume(1))
