from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
  result = []
  prev_index = 0

  for index in indexes:
    if index <= prev_index or index > len(s):
      continue
    result.append(s[prev_index:index])
    prev_index = index

  if prev_index <= len(s):
    result.append(s[prev_index:])

  return result
