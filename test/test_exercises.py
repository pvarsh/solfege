from solfege.exercises.exercises import ascending, ascending_thirds_ascending, ascending_triads_ascending, ascending_triads_descending, descending, descending_thirds_descending, descending_triads_ascending, descending_triads_descending, down_to_root, three_ascending_notes_descending, three_descending_notes_ascending, three_notes_ascending, three_notes_descending, up_to_root

def test_ascending():
    assert ascending(3)._steps == [0, 1, 2, 3]

def test_descending():
    assert descending(3)._steps == [3, 2, 1, 0]

def test_down_to_root():
    assert down_to_root(3)._steps == [0, 1, 0, 2, 1, 0, 3, 2, 1, 0]

def test_up_to_root():
    assert up_to_root(3)._steps == [3, 2, 3, 1, 2, 3, 0, 1, 2, 3]

def test_three_notes_ascending():
    assert three_notes_ascending(3)._steps == [0, 1, 2, 1, 2, 3, 2, 3, 4, 3]

def test_three_notes_descending():
    assert three_notes_descending(3)._steps == [3, 2, 1, 2, 1, 0, 1, 0, -1, 0]

def test_three_descending_notes_ascending():
    assert three_descending_notes_ascending(3)._steps == [2, 1, 0, 3, 2, 1, 4, 3, 2, 3]

def test_three_ascending_notes_descending():
    assert three_ascending_notes_descending(3)._steps == [3, 4, 5, 2, 3, 4, 1, 2, 3, 0]

def test_ascending_thirds_ascending():
    assert ascending_thirds_ascending(3)._steps == [0, 2, 1, 3, 2, 4, 3]

def test_descending_thirds_descending():
    assert descending_thirds_descending(3)._steps == [3, 1, 2, 0, 1, -1, 0]

def test_descending_triads_descending():
    assert descending_triads_descending(3)._steps == [3, 1, -1, 2, 0, -2, 1, -1, -3, 0]

def test_ascending_triads_ascending():
    assert ascending_triads_ascending(3)._steps == [0, 2, 4, 1, 3, 5, 2, 4, 6, 3]

def test_ascending_triads_descending():
    assert ascending_triads_descending(3)._steps == [3, 5, 7, 2, 4, 6, 1, 3, 5, 0]

def test_descending_triads_ascending():
    assert descending_triads_ascending(3)._steps == [4, 2, 0, 5, 3, 1, 6, 4, 2, 3]
