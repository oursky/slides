from typing import overload

@overload
def inc(seq: List[int]) -> List[int]: ...
@overload
def inc(seq: Mapping[str, int]) -> Mapping[str, int]: