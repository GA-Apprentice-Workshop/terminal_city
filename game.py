
def hint():
    if hint_count == 1:
        print '''
        To save information you find use the > operator. Example:

        'cat crimescene > newfile.txt'

        This will output the crimescene to a file named newfile in
        the text format.
        '''
    elif hint_count == 2:
        print '''
        You can filter your grep searches. Example:
        'grep some_word file_name | grep some_other_word'

        This will search file_name for some_word given and then search those
        results for some_other_word.

        The pipe character (|) is very, very useful for in-depth searches.
        You should also experiment with grep flags by checking the manual.

        man grep
        '''
