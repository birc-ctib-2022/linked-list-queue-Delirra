"""Testing queues."""
from queue import Queue
from random import randint

def test_queue() -> None:
    "Does the function initiate an object?"
    x = Queue()
    assert x

def test_is_empty() -> None:
    """Is the initial object empty (i.e. has None value)
    and return True for the is_empty method?"""
    x = Queue()
    assert x.head.val is None
    assert x.is_empty() is True

def test_enqueue() -> None:
    """Can we add to the queue?
    Does the front method give the first element?
    Is the queue circular?"""
    x = Queue()
    y = randint(0, 100)
    z = randint(0, 100)
    x.enqueue(y)
    x.enqueue(z)
    assert x.front() == y # Test if first element is correct
    assert x.head.prev.val == z # Test if queue is circular

def test_dequeue() -> None:
    """Add elements -> return elements in a
    first-in-first-out order"""
    x = Queue()
    foo, bar, baz = randint(0, 100), randint(0, 100), randint(0, 100)
    x.enqueue(foo)
    x.enqueue(bar)
    x.enqueue(baz)
    assert x.dequeue() == foo
    assert x.dequeue() == bar
    assert x.dequeue() == baz

