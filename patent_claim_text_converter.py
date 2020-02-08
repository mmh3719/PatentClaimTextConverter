import json


def convert_claim_text(claim_text: str) -> json:
    """
    This method takes the text of the patent claims and then converts them into a dictionary where the keys are the
    claim numbers and the values are a list of strings.  Each item in the list is a clause of the patent claim, and the
    clauses are listed in the order in which they are provided by the claim.  The dictionary is then loaded into a JSON
    object that is passed to the frontend for processing.
    :param claim_text: String containing the full text of a patent's claims
    :return: JSON object with the patent claims by order of claim number and claim as a list of clauses
    """
    # Dictionary object to store the claims
    claim_text_dict = {}
    claim_number_positions = find_claim_numbers(claim_text)
    for i in range(len(claim_number_positions)):
        current_claim_number = str(i+1)

        # We slice the text starting after the number where the text starts up to the next number.
        if i != len(claim_number_positions) - 1:
            claim_text_dict[current_claim_number] = claim_text[claim_number_positions[i] + len(current_claim_number) + 2
                                                               :claim_number_positions[i+1]].split(';')

        # To prevent an index error for the last claim we slice to the remainder of the text
        else:
            claim_text_dict[current_claim_number] = claim_text[claim_number_positions[i] + len(current_claim_number) + 2
                                                               :].split(';')

    return json.dumps(claim_text_dict)


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
