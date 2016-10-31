# Utility to produce a bmp image by replacing header in encrypted file
# with that of the original file
#
# Author: Nishant Rodrigues
# Date: 10/10/2016

import argparse
import sys

NUM_BYTES_IN_HEADER = 54

def main():
  parser = argparse.ArgumentParser()

  # Add arguments to the argument parser
  parser.add_argument("original", help="filename of the original image",
                      type=str)
  parser.add_argument("encrypted", help="filename of the encrypted image",
                      type=str)
  parser.add_argument("-o", "--output", help="filename of the result",
                      type=str, nargs='?', default="out.bmp")

  # Parse the arguments provided by the user
  args = parser.parse_args()
  
  # Replace the header and produce output
  replace_header(args.original, args.encrypted, args.output)

def replace_header(original, encrypted, output):
  # Open the three files
  f_orig = open(original, 'rb')
  f_enc = open(encrypted, 'rb')
  f_out = open(output, 'wb')
  
  # Read the first 54 header bytes
  for i in range(NUM_BYTES_IN_HEADER):
    orig_byte = f_orig.read(1)
    enc_byte = f_enc.read(1)
    # Write the original byte to output
    f_out.write(orig_byte)
    
  # Write the remaining encrypted bytes to output
  enc_byte = f_enc.read(1)
  while enc_byte:
    f_out.write(enc_byte)
    enc_byte = f_enc.read(1)
  
  f_orig.close()
  f_enc.close()
  f_out.close()

if __name__ == "__main__":
  main()
