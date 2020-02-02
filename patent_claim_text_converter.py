import json


def convert_claim_text(claim_text: str):
    # TODO: Complete the method
    converted_string = json.dumps(claim_text)
    pass


def find_claim_numbers(claim_text: str) -> list:
    """
    Method to find starting positions of the claims in the claim text.  Done by going through the text and doing string
    matches against text that matches the start of a claim.
    :param claim_text: String containing the full text of a patent's claims.
    :return: A list of integers with the positions in the string of the start of each claim.
    """
    size = len(claim_text)
    positions = []
    current = 0
    claim_no = 1
    claim_marker = create_claim_marker(claim_no)
    while current < size:
        if claim_text[current: current + len(claim_marker)] == claim_marker:
            positions.append(current)
            claim_no += 1
            claim_marker = create_claim_marker(claim_no)
        current += 1
    return positions


def create_claim_marker(claim_no: int) -> str:
    """
    Creates the string that matches the start of a specific claim according the place in which it is given.  For
    example, '1.' would be the string for the the first claim.
    :param claim_no: The place of the claim in the list of claims of the patent.
    :return: The string that matches the placement of that claim in the text of a patent's claims document.
    """
    return str(claim_no) + '.'
