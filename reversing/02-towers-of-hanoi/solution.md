# Towers of Hanoi

**Flag:** `CSCOSU{166589903787325219380851695350896256250980509594874862046961683989710}`

Although the game is "broken", it is still possible to load a winning saved-game state, which will automatically win and
print the flag.

Such a state would consist of all rings being on the same pole, and none being on any other pole. Such a state can be
constructed and displayed by adding the following code anywhere in the game's main method:

```java
ArrayList<BigInteger> win = new ArrayList<BigInteger>();
for (int i = 0; i < GAME_SIZE; i++) {
    win.add(BigInteger.valueOf(i));
}
System.out.println(win);
System.out.println(createSavedPoleInformation(win));
```

This prints the saved pole state for a pole with all 40 rings on it. We still need the saved pole state for the other
two empty rings. According to the game's internal representation, the saved pole state for an empty pole is just `1`.

Now, starting up the game and "loading" 2 empty poles and the winning pole will print the flag!
