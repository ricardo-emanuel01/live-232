# Uma introdução a testes

[Unittest](https://docs.python.org/3/library/unittest.html)

## Asserts unittest

- assertEqual(a, b) --> a == b
- assertNotEqual(a, b) --> a != b
- assertTrue(x) --> bool(x) is True
- assertFalse(x) --> bool(x) is False
- assertIs(a, b) --> a is b
- assertIsNot(a, b) --> a is not b
- assertIsNotNone(a) --> a is not None
- assertIsNone(a) --> a is None
- assertIn(a, b) --> a in b
- assertIsInstance(a, b) --> isinstance(a, b)
- assertIsNotInstance(a, b) --> not isinstance(a, b)
- assertAlmostEqual(a, b) --> round(a-b, 7) == 0
- assertNotAlmostEqual(a, b) --> round(a-b, 7) != 0
- assertGreater(a, b) --> a > b
- assertGreaterEqual(a, b) --> a >= b
- assertLess(a, b) --> a < b
- assertLessEqual(a, b) --> a <= b
- assertNotRegex(s, r) --> not r.search(s)
- assertCountEqual(a, b) --> a e b tem os mesmos elementos em mesma quantidade mas não precisam estar na mesma ordem

Também existem **asserts** que checam **Exceptions** geradas.
