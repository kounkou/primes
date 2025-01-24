
def generateBinary(input):
    """
    generateBinary returns the binary representation of the input number

    Args:
        input(integer): provided number
    
    Returns:
        str: 32-bit binary representation
    """
    if input < 0:
        raise ValueError("Please provide a positive integers.")
    return bin(input)[2:].zfill(32)