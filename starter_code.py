from argparse import ArgumentParser
from difflib import SequenceMatcher


def compute_difference_between_files(file1_path, file2_path):

  with open(file1_path) as file1:
    file1_contents = file1.read()

  with open(file2_path) as file2:
    file2_contents = file2.read()

  matcher = SequenceMatcher(None, file1_contents, file2_contents)

  chars_shared = 0
  chars_unique_to_file1 = 0
  chars_unique_to_file2 = 0

  for (code, s1_start, s1_end, s2_start, s2_end) in matcher.get_opcodes():
    if code == "equal":
      chars_shared += s2_end - s2_start
    else:
      chars_unique_to_file1 += s1_end - s1_start
      chars_unique_to_file2 += s2_end - s2_start

  return (
    chars_shared,
    chars_unique_to_file1,
    chars_unique_to_file2
  )


if __name__ == "__main__":
  parser = ArgumentParser(description="Determine degree of overlap in contents of files.")
  parser.add_argument("file1", help="Path to a file.")
  parser.add_argument("file2", help="Path to another file.")
  args = parser.parse_args()

  chars_shared, chars_unique_to_file1, chars_unique_to_file2 =\
    compute_difference_between_files(args.file1, args.file2)

  print("# of shared characters:", chars_shared)
  print("# of characters only in file 1:", chars_unique_to_file1)
  print("# of characters only in file 2:", chars_unique_to_file2)
