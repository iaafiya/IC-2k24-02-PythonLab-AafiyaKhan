# Part C - Short Reasoning Answers

1. `d2 = d` does not copy a dictionary; it makes `d2` another reference to the same object. Therefore, a change through either name is visible through the other. `d.copy()` makes a shallow copy: the outer dictionary is new, but nested dictionaries/lists are still shared. `copy.deepcopy(d)` recursively copies nested objects too. For the student database, use `deepcopy` when an independent snapshot/backup is needed because each student contains a nested `marks` dictionary. For ordinary updates to one student's marks, direct access to the original nested dictionary is intended.

2. Dictionary keys must be hashable so Python can calculate a stable hash and find the key efficiently. `[1, 2]` is not hashable; `(1, 2)` is hashable because its elements are hashable; `{1, 2}` is not hashable; `"12"` is hashable. Thus, `(1, 2)` and `"12"` can be keys.

3. Use `d[key]` when the key is expected to exist and a missing key should be an error, such as reading `students[roll]["name"]` after checking that the roll number exists. Use `d.get(key)` when a missing key is normal and `None` is an acceptable result, such as `contacts.get(name)` during a search. Use `d.get(key, default)` when a useful fallback is needed, such as `counts.get(word, 0) + 1` in the word counter.

4. `d[key] = value` assigns one key-value pair. `.update()` adds/replaces multiple key-value pairs from another dictionary or iterable of pairs (or keyword arguments). `.update()` is cleaner when several fields/values need to be merged at once, for example `record.update({"email": email, "city": city})`.

5. In Q2, creating a new dictionary with a comprehension preserves the original employee data, making it possible to compare before/after values, undo the calculation, or use the original elsewhere. In-place modification is better when the change is meant to become the permanent current state and no original snapshot is required; it also avoids creating another dictionary.

6. Deleting a key during direct dictionary iteration changes the dictionary's size while its iterator is active, so Python raises `RuntimeError`. Safe methods include: (a) iterate over a separate list of keys, e.g. `for key in list(d): ...`; (b) build a new dictionary with a comprehension containing only the entries to keep.

7. The original library data is book -> record -> list of member IDs. To invert it, loop through every book and each member in `issued_to`, then append the book ISBN to `member_books.setdefault(member, [])`. A list is needed because one member may hold multiple different books; a single value would lose earlier book information.

8. Dictionary key lookup is average-case O(1), while searching a list of records is O(n) because records may need to be checked one by one. In Q5, a number -> name dictionary allows reverse lookup directly by phone number, instead of scanning every contact and every phone number each time. Building the reverse dictionary costs O(total phone numbers), then each lookup is average-case O(1).
