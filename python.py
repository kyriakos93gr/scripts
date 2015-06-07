import binascii

input = 'd'
output = ''
# hex to text
def hex_to_txt ( str ):
    out = binascii.unhexlify ( str )
    return out

# text to hex
def txt_to_hex ( str ):
    out = binascii.hexlify ( str )
    return out

# text to bin
def txt_to_bin ( str ):
    out = bin ( int ( binascii.hexlify ( str ), 16 ) )
    out = out [2 : ]
    return out

# bin to text
def bin_to_txt ( str ):
    out = bin ( int ( binascii.hexlify ( str ), 16 ) )
    out = out [2 : ]
    return out


output=text_to_bin ( input )

print output
