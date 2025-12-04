def get_num_words(text):
  words = text.split()
  return len(words)

def get_chars_dict(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_on(items):
  return items["num"]


def chars_dict_to_sorted_list(dict):
  char_list = []
  for ch in dict:
    char_list.append({"char": ch, "num": dict[ch]})
  char_list.sort(reverse=True, key=sort_on)
  return char_list
