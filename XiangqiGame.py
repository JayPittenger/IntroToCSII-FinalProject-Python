# Author: Jay Pittenger
# Date: 3/3/2020
# Description: Defines classes in order to play XiangqiGame. This includes main XiangqiGame class which initializes
#              the game board and allows moves to be made. Also provides methods for checking game state, and whether
#              or not a particular team is in check. Piece class defines game pieces, which Piece child classes for
#              specific piece types: General, Advisor, Horse, Elephant, Chariot, Soldier, Cannon. Each Piece child
#              class have methods accessed by the XiangqiGame class that define all possible moves that can be made
#              for that particular piece type, and performs validation with the context of the current board layout.


class XiangqiGame:
    """Represents a game of Xiangqi"""
    def __init__(self):
        """Initialize XiangqiGame object with starting team, game_state, and check states for each team"""
        self._current_team = 'red'
        self._game_state = "UNFINISHED"
        self._red_in_check = False
        self._black_in_check = False

        # Instantiate all Piece objects.
        # first character in object name is Piece type, second character is team color, and third is number (if more
        # than one)
        # red team
        self._g_r = General('red', 'e1', 'g_r')
        self._a_r_1 = Advisor('red', 'd1', 'a_r_1')
        self._a_r_2 = Advisor('red', 'f1', 'a_r_2')
        self._e_r_1 = Elephant('red', 'c1', 'e_r_1')
        self._e_r_2 = Elephant('red', 'g1', 'e_r_2')
        self._h_r_1 = Horse('red', 'b1', 'h_r_1')
        self._h_r_2 = Horse('red', 'h1', 'h_r_2')
        self._r_r_1 = Chariot('red', 'a1', 'r_r_1')
        self._r_r_2 = Chariot('red', 'i1', 'r_r_2')
        self._c_r_1 = Cannon('red', 'b3', 'c_r_1')
        self._c_r_2 = Cannon('red', 'h3', 'c_r_2')
        self._s_r_1 = Soldier('red', 'a4', 's_r_1')
        self._s_r_2 = Soldier('red', 'c4', 's_r_2')
        self._s_r_3 = Soldier('red', 'e4', 's_r_3')
        self._s_r_4 = Soldier('red', 'g4', 's_r_4')
        self._s_r_5 = Soldier('red', 'i4', 's_r_5')

        # black team
        self._g_b = General('black', 'e10', 'g_b')
        self._a_b_1 = Advisor('black', 'd10', 'a_b_1')
        self._a_b_2 = Advisor('black', 'f10', 'a_b_2')
        self._e_b_1 = Elephant('black', 'c10', 'e_b_1')
        self._e_b_2 = Elephant('black', 'g10', 'e_b_2')
        self._h_b_1 = Horse('black', 'b10', 'h_b_1')
        self._h_b_2 = Horse('black', 'h10', 'h_b_2')
        self._r_b_1 = Chariot('black', 'a10', 'r_b_1')
        self._r_b_2 = Chariot('black', 'i10', 'r_b_2')
        self._c_b_1 = Cannon('black', 'b8', 'c_b_1')
        self._c_b_2 = Cannon('black', 'h8', 'c_b_2')
        self._s_b_1 = Soldier('black', 'a7', 's_b_1')
        self._s_b_2 = Soldier('black', 'c7', 's_b_2')
        self._s_b_3 = Soldier('black', 'e7', 's_b_3')
        self._s_b_4 = Soldier('black', 'g7', 's_b_4')
        self._s_b_5 = Soldier('black', 'i7', 's_b_5')

        # Initialize board
        self._board = [[self._r_r_1, self._h_r_1, self._e_r_1, self._a_r_1, self._g_r, self._a_r_2, self._e_r_2,
                        self._h_r_2, self._r_r_2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, self._c_r_1, 0, 0, 0, 0, 0, self._c_r_2, 0],
                       [self._s_r_1, 0, self._s_r_2, 0, self._s_r_3, 0, self._s_r_4, 0, self._s_r_5],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [self._s_b_1, 0, self._s_b_2, 0, self._s_b_3, 0, self._s_b_4, 0, self._s_b_5],
                       [0, self._c_b_1, 0, 0, 0, 0, 0, self._c_b_2, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [self._r_b_1, self._h_b_1, self._e_b_1, self._a_b_1, self._g_b, self._a_b_2, self._e_b_2,
                        self._h_b_2, self._r_b_2]]

        # tracking list of in play pieces
        self._in_play = [self._r_r_1, self._h_r_1, self._e_r_1, self._a_r_1, self._g_r, self._a_r_2, self._e_r_2,
                         self._h_r_2, self._r_r_2, self._c_r_1, self._c_r_2, self._s_r_1, self._s_r_2, self._s_r_3,
                         self._s_r_4, self._s_r_5, self._s_b_1, self._s_b_2, self._s_b_3, self._s_b_4, self._s_b_5,
                         self._c_b_1, self._c_b_2, self._r_b_1, self._h_b_1, self._e_b_1, self._a_b_1, self._g_b,
                         self._a_b_2, self._e_b_2, self._h_b_2, self._r_b_2]

    def get_game_state(self):
        """
        Description:
        Method returns current state of game
        Return:
        self._game_state
        """
        return self._game_state

    def get_current_team(self):
        """
        Description:
        Method returns current team turn
        Return:
        self._current_team
        """
        return self._current_team

    def is_in_check(self, team):
        """
        Description:
        returns if team in question is currently in check
        Parameters:
        team - string of team with which to check if in check
        Returns:
        if team == 'red' or if team = 'black, will return true or false depending on whether or not
        that team is currently in check
        """
        if team == 'red' or team == 'black':
            if team == 'red':
                return self._red_in_check
            else:
                return self._black_in_check
        else:
            return False

    def get_board(self):
        """
        Description:
        Method returns current board list
        """
        return self._board

    def print_current_board(self):
        """
        Description:
        Method prints current board for game testing
        """
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[9-i][j] == 0:
                    print(self._board[9-i][j], end='')
                    print("       ", end='')
                elif len(self._board[9-i][j].get_text()) == 3:
                    print(self._board[9-i][j].get_text(), end='')
                    print("     ", end='')
                elif len(self._board[9-i][j].get_text()) == 5:
                    print(self._board[9-i][j].get_text(), end='')
                    print("   ", end='')
            print()

    def make_move(self, src, dest):
        """
        Description:
        Performs move operation of pieces on board if desired move is valid. Updates game_state, board, in_play list,
        whose team it is, is_in_check for each team as required
        Parameters:
        src - algebraic notation string for board location of piece to be moved
        dest - algebraic notation string for board location of destination for piece
        Returns:
        True if move was successful, else returns False
        """
        # Check if game has already been won
        if self._game_state != 'UNFINISHED':
            return False
        # Perform input validation
        if src == dest:
            return False
        src_coord = self._input_validation(src)
        dest_coord = self._input_validation(dest)
        if (src_coord is False) or (dest_coord is False):
            return False
        src_piece = self._board[src_coord[0]][src_coord[1]]
        dest_piece = self._board[dest_coord[0]][dest_coord[1]]
        # if source slot contains no piece to move
        if src_piece == 0:
            return False
        # if the piece at source location does not belong to team whose turn it is
        if src_piece.get_team() != self._current_team:
            return False
        # if piece at destination belongs to team whose turn it currently is
        if dest_piece != 0:
            if dest_piece.get_team() == self._current_team:
                return False

        # check if move is valid for specific Piece class
        valid_list = src_piece.possible_moves(src_coord, self._board)
        validity = False
        # find dest_coord in list of valid move coordinates for that piece type
        for el in valid_list:
            if el == dest_coord:
                validity = True
        if validity is False:
            return False

        # check if move results in general being in check or does not fix check- if so do not execute move
        if dest_piece != 0:
            # remove opponent piece at destination so that it doesnt influence if general is in check
            self._in_play.remove(dest_piece)
        if self._move_in_check(src_coord, dest_coord, self._current_team) is True:
            # move does not fix check
            print("this move results in team's general being in check - return false")
            # restore dest_piece back into in play pieces
            if dest_piece != 0:
                self._in_play.append(dest_piece)
            return False
        else:
            # move made general no longer in check - update check status
            if self._current_team == 'red':
                self._red_in_check = False
            else:
                self._black_in_check = False

        # make move
        if dest_piece != 0:
            # set destination piece to captured by defining board location of piece to False
            dest_piece.update_board_location(False)
        # update moved piece's location to the destination
        src_piece.update_board_location(dest)
        # perform board move
        self._board[dest_coord[0]][dest_coord[1]] = src_piece
        self._board[src_coord[0]][src_coord[1]] = 0

        # update turn to opposing team
        self._current_team = self._change_turn(self._current_team)

        # determine if opposing team is now in check
        if self._move_in_check(src_coord, dest_coord, self._current_team) is True:
            if self._current_team == 'red':
                self._red_in_check = True
            else:
                self._black_in_check = True
            # check if general of opposing team is in checkmate
            if self._current_team == 'red':
                # check all valid moves for red team general
                general_coord = self._input_validation(self._g_r.get_board_location())
                general_mov_list = self._g_r.possible_moves(general_coord, self.get_board())
            else:
                # check all valid moves for black team general
                general_coord = self._input_validation(self._g_b.get_board_location())
                general_mov_list = self._g_b.possible_moves(general_coord, self.get_board())
            rec = True
            for coord in general_mov_list:
                # for each of the valid moves, see if the general will have more valid moves when it gets there
                rec = self._move_in_check(general_coord, coord, self._current_team)
                if rec is False:
                    break
            if rec is True:
                # general is in checkmate - update game state
                if self._current_team == 'red':
                    self._game_state = "BLACK_WON"
                else:
                    self._game_state = "RED_WON"

        # check if opposing team is in stalemate
        for el in self._in_play:
            # for all pieces in play that belong to opposing team
            if el.get_team() == self._current_team:
                # see if piece has valid moves
                piece_coord = self._input_validation(el.get_board_location())
                mov_list = el.possible_moves(piece_coord, self._board)
                # add moves to mov_list_result that don't put general in check
                mov_list_result = []
                for el_mov in mov_list:
                    if self._move_in_check(piece_coord, el_mov, self._current_team) is False:
                        mov_list_result.append(el_mov)
                # return true if one of the pieces has at least one valid move
                if mov_list_result != []:
                    return True
        # team is in stalemate so other team wins
        if self._current_team == 'red':
            self._game_state = "BLACK_WON"
        else:
            self._game_state = "RED_WON"

        return True

    def _move_in_check(self, src_coord, dest_coord, team):
        """
        Description:
        Private method to determine if move causes check condition
        Parameters:
        src_coord - tuple source coord from which move is made
        dest_coord - tuple destination of move
        team - team with which to check is in check or not
        Returns:
        True of general is in check of that team
        False otherwise
        """
        src_piece = self._board[src_coord[0]][src_coord[1]]
        dest_piece = self._board[dest_coord[0]][dest_coord[1]]
        # check if move results in general being in check
        # temporarily move piece out of way and into new location
        self._board[src_coord[0]][src_coord[1]] = 0
        self._board[dest_coord[0]][dest_coord[1]] = src_piece

        # iterate over all pieces currently in play
        for piece in self._in_play:
            # for all pieces of opposing team
            if piece.get_team() != team:
                loc = piece.get_board_location()
                loc_coord = self._input_validation(loc)
                # at the coordinate location of that piece, determine all possible move coordinates and
                # iterate through each one
                all_moves = piece.possible_moves(loc_coord, self.get_board())
                if all_moves != []:
                    for coord in all_moves:
                        # if the piece at this coordinate is the general of the team
                        if team == 'red':
                            if self._board[coord[0]][coord[1]] == self._g_r:
                                self._board[dest_coord[0]][dest_coord[1]] = dest_piece
                                self._board[src_coord[0]][src_coord[1]] = src_piece
                                return True
                        else:
                            if self._board[coord[0]][coord[1]] == self._g_b:
                                self._board[dest_coord[0]][dest_coord[1]] = dest_piece
                                self._board[src_coord[0]][src_coord[1]] = src_piece
                                return True
        # restore proper pieces back to original positions
        self._board[dest_coord[0]][dest_coord[1]] = dest_piece
        self._board[src_coord[0]][src_coord[1]] = src_piece
        return False

    def _input_validation(self, slot):
        """
        Description:
        Private method that checks if slot is a valid slot on the game board and converts from algebraic notation
        to coordinate notation for specific elements within board list
        Parameters:
        slot - string of slot position to be validated eg. a1
        Returns:
        returns Returns tuple of board list coordinates if it is valid input, else returns False
        """
        # if input is 2 characters
        if len(slot) == 2:
            is_num = False
            # check if second character is number
            for i in range(10):
                if slot[1] == str(i):
                    is_num = True
            if is_num is False:
                return is_num
            col_pos = ord(slot[0]) - 97
            row_pos = int(slot[1]) - 1
            # check if col_pos falls in correct board range
            if col_pos > 8 or col_pos < 0:
                return False
            # check if row_pos falls in correct board range
            if row_pos >= 10 or row_pos < 0:
                return False
            board_pos = (row_pos, col_pos)
            return board_pos
        # if input is 3 characters
        elif len(slot) == 3:
            col_pos = ord(slot[0]) - 97
            # ensure values for row pos are equal to 10
            if slot[1] != '1':
                return False
            if slot[2] != '0':
                return False
            # ensure col_pos falls in correct range
            if col_pos > 8 or col_pos < 0:
                return False
            row_pos = 9
            board_pos = (row_pos, col_pos)
            return board_pos
        else:
            return False

    def _change_turn(self, curr_team):
        """
        Description:
        Private method that changes turn by updating self._current_team to team other than curr_team
        Parameter:
        curr_team - string of team to be changed from
        Returns:
        updated self._current_team
        """
        if curr_team == 'red':
            self._current_team = 'black'
        elif curr_team == 'black':
            self._current_team = 'red'
        return self._current_team


class Piece:
    """Represents a Piece in the game Xiangqi"""
    def __init__(self, team, board_loc, text_name):
        """
        Initializes Piece object with team, current board location, and text name
        """
        self._team = team
        self._board_location = board_loc
        self._text_name = text_name

    def get_text(self):
        """
        Description:
        Method returns text name of piece object
        """
        return self._text_name

    def get_team(self):
        """
        Description:
        Method returns team of piece object
        """
        return self._team

    def get_board_location(self):
        """
        Description:
        Method returns current board location
        """
        return self._board_location

    def update_board_location(self, dest):
        """
        Description:
        Method updates current board location to new dest
        Parameters:
        dest - string board slot position, must be valid
        """
        self._board_location = dest

    def is_on_the_board(self, coord):
        """
        Description:
        Method to check if coord is on the board
        Parameters:
        coord - coordinate to be checked against the range of the board
        Returns:
        True if coordinate exists on board, false if not
        """
        # check range for rows
        if (coord[0] > 9) or (coord[0] < 0):
            return False
        # check range for columns
        if (coord[1] > 8) or (coord[1] < 0):
            return False
        return True


class General(Piece):
    """Represents a General Piece"""

    def _is_valid(self, possible_list, board):
        """
        Description:
        Private method that determines if moves are valid for this piece type with the current context of board
        Parameters:
        possible_list: list of tuples of all possible moves for piece type
        board - current board layout with pieces as a list from XiangqiGame method
        Returns:
        valid_list of all valid moves with respect to the board
        """
        team = self.get_team()
        valid_list = []
        result = []
        # valid list will contain only those moves that exist within the castle of team
        for el in possible_list:
            if team == 'black':
                if (el[0] <= 9) and (el[0] >= 7):
                    if (el[1] <= 5) and (el[1] >= 3):
                        valid_list.append(el)
            if team == 'red':
                if (el[0] <= 2) and (el[0] >= 0):
                    if (el[1] <= 5) and (el[1] >= 3):
                        valid_list.append(el)
        for el in valid_list:
            # if destination is empty, add coord to result list
            if board[el[0]][el[1]] == 0:
                result.append(el)
            # if destination has opponent in it, add coord to result list
            elif board[el[0]][el[1]].get_team() != team:
                result.append(el)
        return result

    def possible_moves(self, src_coord, board):
        """
        Description:
        returns a list of tuples of all possible moves that can be made from current location coordinates
        Parameters:
        src_coord - tuple of source board slot coordinates
        board - current board list that contains piece objects
        Returns:
        list of tuples of all possible moves for this Piece class from the src_coord location validated with is_valid
        method
        """
        y = src_coord[0]
        x = src_coord[1]
        possible_list = [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]

        return self._is_valid(possible_list, board)


class Advisor(Piece):
    """Represents an Advisor Piece"""

    def _is_valid(self, possible_list, board):
        """
        Description:
        Private method that determines if moves are valid for this piece type with the current context of board
        Parameters:
        possible_list: list of tuples of all possible moves for piece type
        board - current board layout with pieces as a list from XiangqiGame method
        Returns:
        valid_list of all valid moves with respect to the board
        """
        team = self.get_team()
        valid_list = []
        result = []
        # valid list will contain only those moves that exist within the castle of team
        for el in possible_list:
            if team == 'black':
                if (el[0] <= 9) and (el[0] >= 7):
                    if (el[1] <= 5) and (el[1] >= 3):
                        valid_list.append(el)
            if team == 'red':
                if (el[0] <= 2) and (el[0] >= 0):
                    if (el[1] <= 5) and (el[1] >= 3):
                        valid_list.append(el)
        for el in valid_list:
            # if destination is empty, add coord to result list
            if board[el[0]][el[1]] == 0:
                result.append(el)
            # if destination has opponent in it, add coord to result list
            elif board[el[0]][el[1]].get_team() != team:
                result.append(el)
        return result

    def possible_moves(self, src_coord, board):
        """
        Description:
        returns a list of tuples of all possible moves that can be made from current location coordinates
        Parameters:
        src_coord - tuple of source board slot coordinates
        board - current board list that contains piece objects
        Returns:
        list of tuples of all possible moves for this Piece class from the src_coord location validated with is_valid
        method
        """
        y = src_coord[0]
        x = src_coord[1]
        possible_list = [(y+1, x+1), (y-1, x+1), (y-1, x-1), (y+1, x-1)]

        return self._is_valid(possible_list, board)


class Elephant(Piece):
    """Represents an Elephant Piece"""

    def _is_valid(self, possible_list, board, opp_list, src_coord):
        """
        Description:
        Private method that determines if moves are valid for this piece type with the current context of board
        Parameters:
        possible_list: list of tuples of all possible moves for piece type
        board - current board layout with pieces as a list from XiangqiGame method
        opp_list - list of tuples for coordinates of potential blocking pieces
        src_coord - tuple coordinates for board location
        Returns:
        valid_list of all valid moves with respect to the board
        """
        y = src_coord[0]
        x = src_coord[1]
        team = self.get_team()
        opp_list_ob = []
        result = []
        for el in opp_list:
            on_board = self.is_on_the_board(el)
            if on_board is True:
                # append new list which represents blocking coordinates that are on the board
                opp_list_ob.append(el)

        for el in opp_list_ob:
            # if blocking coordinate has pieces there - remove appropriate valid moves
            if board[el[0]][el[1]] != 0:
                if y > el[0] and x > el[1]:
                    possible_list.remove((y - 2, x - 2))
                elif y < el[0] and x < el[1]:
                    possible_list.remove((y + 2, x + 2))
                elif y < el[0] and x > el[1]:
                    possible_list.remove((y + 2, x - 2))
                elif y > el[0] and x < el[1]:
                    possible_list.remove((y - 2, x + 2))

        # remove any destination coordinates that have pieces of the same team
        for el in possible_list:
            # if the coordinate exists on the board
            # red team
            if team == 'red':
                if self.is_on_the_board(el) is True and (el[0] < 5):
                    # if destination is empty, add coord to result list
                    if board[el[0]][el[1]] == 0:
                        result.append(el)
                    # if destination has opponent in it, add coord to result list
                    elif board[el[0]][el[1]].get_team() != team:
                        result.append(el)
            # black team
            else:
                if self.is_on_the_board(el) is True and (el[0] > 4):
                    # if destination is empty, add coord to result list
                    if board[el[0]][el[1]] == 0:
                        result.append(el)
                    # if destination has opponent in it, add coord to result list
                    elif board[el[0]][el[1]].get_team() != team:
                        result.append(el)
        return result

    def possible_moves(self, src_coord, board):
        """
        Description:
        returns a list of tuples of all possible moves that can be made from current location coordinates
        Parameters:
        src_coord - tuple of source board slot coordinates
        Returns:
        list of tuples of all possible moves for this Piece class from the src_coord location validated with is_valid
        method
        """
        y = src_coord[0]
        x = src_coord[1]
        possible_list = [(y + 2, x + 2), (y + 2, x - 2), (y - 2, x - 2), (y - 2, x + 2)]
        # list of all possible locations where opponents can block move
        opp_list = [(y + 1, x + 1), (y - 1, x + 1), (y - 1, x - 1), (y + 1, x - 1)]
        return self._is_valid(possible_list, board, opp_list, src_coord)


class Horse(Piece):
    """Represents a Horse Piece"""

    def _is_valid(self, possible_list, board, opp_list, src_coord):
        """
        Description:
        Private method that determines if moves are valid for this piece type with the current context of board
        Parameters:
        possible_list: list of tuples of all possible moves for piece type
        board - current board layout with pieces as a list from XiangqiGame method
        src_coord - tuple that represents board coordinate
        opp_list - list of tuples for coordinates of potential blocking pieces
        Returns:
        valid_list of all valid moves with respect to the board
        """
        y = src_coord[0]
        x = src_coord[1]
        team = self.get_team()
        opp_list_ob = []
        result = []
        for el in opp_list:
            on_board = self.is_on_the_board(el)
            if on_board is True:
                # append new list which represents blocking coordinates that are on the board
                opp_list_ob.append(el)

        for el in opp_list_ob:
            # if blocking coordinate has pieces there - remove appropriate valid moves
            if board[el[0]][el[1]] != 0:
                if y > el[0]:
                    possible_list.remove((y - 2, x - 1))
                    possible_list.remove((y - 2, x + 1))
                elif y < el[0]:
                    possible_list.remove((y + 2, x - 1))
                    possible_list.remove((y + 2, x + 1))
                elif x > el[1]:
                    possible_list.remove((y + 1, x - 2))
                    possible_list.remove((y - 1, x - 2))
                elif x < el[1]:
                    possible_list.remove((y + 1, x + 2))
                    possible_list.remove((y - 1, x + 2))

        # remove any destination coordinates that have pieces of the same team
        for el in possible_list:
            # if the coordinate exists on the board
            if self.is_on_the_board(el) is True:
                # if destination is empty, add coord to result list
                if board[el[0]][el[1]] == 0:
                    result.append(el)
                # if destination has opponent in it, add coord to result list
                elif board[el[0]][el[1]].get_team() != team:
                    result.append(el)
        return result

    def possible_moves(self, src_coord, board):
        """
        Description:
        returns a list of tuples of all possible moves that can be made from current location coordinates
        Parameters:
        src_coord - tuple of source board slot coordinates
        Returns:
        list of tuples of all possible moves for this Piece class from the src_coord location validated with is_valid
        method
        """
        y = src_coord[0]
        x = src_coord[1]
        possible_list = [(y + 2, x - 1), (y + 2, x + 1), (y + 1, x + 2), (y - 1, x + 2),
                         (y - 2, x - 1), (y - 2, x + 1), (y + 1, x - 2), (y - 1, x - 2)]
        # list of all possible locations where opponents can block move
        opp_list = [(y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1)]
        return self._is_valid(possible_list, board, opp_list, src_coord)


class Chariot(Piece):
    """Represents a Chariot (rook) Piece"""

    def _is_valid(self, start_list, board, src_coord):
        """
        Description:
        Private method that determines if moves are valid for this piece type with the current context of board
        Parameters:
        start_list: list of tuples of all possible moves for piece type
        board - current board layout with pieces as a list from XiangqiGame method
        src_coord - tuple that represents board coordinate
        Returns:
        valid_list of all valid moves with respect to the board
        """
        y = src_coord[0]
        x = src_coord[1]
        team = self.get_team()
        result = []
        start_list_val = []
        for el in start_list:
            # if the coordinate exists on the board
            if self.is_on_the_board(el) is True:
                # if destination is empty, add coord to start_list_val
                if board[el[0]][el[1]] == 0:
                    start_list_val.append(el)
                    result.append(el)
                # if destination has opponent in it, add coord to result list
                elif board[el[0]][el[1]].get_team() != team:
                    result.append(el)
        # for each element in the list that contains the starter coordinate for each direction
        for el in start_list_val:
            for i in range(10):
                j = i + 1

                # depending on starting direction coordinate, define curr_coordinate which is next in line
                if el[0] > y:
                    curr_coord = (el[0] + j, el[1])
                elif el[0] < y:
                    curr_coord = (el[0] - j, el[1])
                elif el[1] < x:
                    curr_coord = (el[0], el[1] - j)
                elif el[1] > x:
                    curr_coord = (el[0], el[1] + j)
                else:
                    curr_coord = (-1, 0)

                # if this next coordinate in the line is not on the board, break and don't add it to list
                if self.is_on_the_board(curr_coord) is False:
                    break

                # if this next coordinate is occupied
                if board[curr_coord[0]][curr_coord[1]] != 0:
                    # if this next coordinate in line is filled by team member, break and don't add to list
                    if board[curr_coord[0]][curr_coord[1]].get_team() == team:
                        break
                    elif board[curr_coord[0]][curr_coord[1]].get_team() != team:
                        result.append(curr_coord)
                        break
                # next coordinate is empty
                else:
                    result.append(curr_coord)
        return result

    def possible_moves(self, src_coord, board):
        """
        Description:
        returns a list of tuples of all possible moves that can be made from current location coordinates
        Parameters:
        src_coord - tuple of source board slot coordinates
        board - current board list that contains piece objects
        Returns:
        list of tuples of all possible moves for this Piece class from the src_coord location validated with is_valid
        method
        """
        y = src_coord[0]
        x = src_coord[1]
        start_list = [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]

        return self._is_valid(start_list, board, src_coord)


class Cannon(Piece):
    """Represents a Cannon Piece"""

    def _is_valid(self, start_list, board, src_coord):
        """
        Description:
        Private method that determines if moves are valid for this piece type with the current context of board
        Parameters:
        possible_list: list of tuples of all possible moves for piece type
        board - current board layout with pieces as a list from XiangqiGame method
        src_coord - tuple that represents board coordinate
        Returns:
        valid_list of all valid moves with respect to the board
        """
        y = src_coord[0]
        x = src_coord[1]
        team = self.get_team()
        result = []
        start_list_val = []
        jump_left = 0
        jump_right = 0
        jump_up = 0
        jump_down = 0
        mov_up = False
        mov_down = False
        mov_left = False
        mov_right = False
        for el in start_list:
            # tracker for direction on board relative to source coordinate
            if el[0] > y:
                mov_up = True
            elif el[0] < y:
                mov_down = True
            elif el[1] < x:
                mov_left = True
            elif el[1] > x:
                mov_right = True
            # if the coordinate exists on the board
            if self.is_on_the_board(el) is True:
                # if destination is empty, add coord to start_list_val and result
                if board[el[0]][el[1]] == 0:
                    start_list_val.append(el)
                    result.append(el)
                # if destination has piece in it, add to start_list_val but not result
                elif board[el[0]][el[1]].get_team() != team:
                    # track that a jump has been performed
                    if mov_up is True:
                        jump_up = 1
                    if mov_down is True:
                        jump_down = 1
                    if mov_left is True:
                        jump_left = 1
                    if mov_right is True:
                        jump_right = 1
                    start_list_val.append(el)
        # for each element in the list that contains the starter coordinate for each direction
        for el in start_list_val:
            for i in range(10):
                mov_up = False
                mov_down = False
                mov_left = False
                mov_right = False
                j = i + 1

                # tracker for direction on board relative to source coordinate
                if el[0] > y:
                    curr_coord = (el[0] + j, el[1])
                    mov_up = True
                elif el[0] < y:
                    curr_coord = (el[0] - j, el[1])
                    mov_down = True
                elif el[1] < x:
                    curr_coord = (el[0], el[1] - j)
                    mov_left = True
                elif el[1] > x:
                    curr_coord = (el[0], el[1] + j)
                    mov_right = True
                else:
                    curr_coord = (-1, 0)

                # if this next coordinate in the line is not on the board, break and don't add it to list
                if self.is_on_the_board(curr_coord) is False:
                    break

                # if this next coordinate is occupied and direction is up from src_coord
                elif board[curr_coord[0]][curr_coord[1]] != 0 and (mov_up is True):
                    # if this next coordinate in line is filled by team member, break and don't add to list
                    if board[curr_coord[0]][curr_coord[1]].get_team() == team and (jump_up == 1):
                        break
                    elif board[curr_coord[0]][curr_coord[1]].get_team() != team and (jump_up == 1):
                        result.append(curr_coord)
                        break
                    elif jump_up == 0:
                        # record that a jump has taken place in this direction
                        jump_up = 1

                # if this next coordinate is occupied and direction is down from src_coord
                elif board[curr_coord[0]][curr_coord[1]] != 0 and (mov_down is True):
                    # if this next coordinate in line is filled by team member, break and don't add to list
                    if board[curr_coord[0]][curr_coord[1]].get_team() == team and (jump_down == 1):
                        break
                    elif board[curr_coord[0]][curr_coord[1]].get_team() != team and (jump_down == 1):
                        result.append(curr_coord)
                        break
                    elif jump_down == 0:
                        # record that jump has taken place in this direction
                        jump_down = 1

                # if this next coordinate is occupied and direction is left from src_coord
                elif board[curr_coord[0]][curr_coord[1]] != 0 and (mov_left is True):
                    # if this next coordinate in line is filled by team member, break and don't add to list
                    if board[curr_coord[0]][curr_coord[1]].get_team() == team and (jump_left == 1):
                        break
                    elif board[curr_coord[0]][curr_coord[1]].get_team() != team and (jump_left == 1):
                        result.append(curr_coord)
                        break
                    elif jump_left == 0:
                        # record that jump has taken place in this direction
                        jump_left = 1

                # if this next coordinate is occupied and direction is right from src_coord
                elif board[curr_coord[0]][curr_coord[1]] != 0 and (mov_right is True):
                    # if this next coordinate in line is filled by team member, break and don't add to list
                    if board[curr_coord[0]][curr_coord[1]].get_team() == team and (jump_right == 1):
                        break
                    elif board[curr_coord[0]][curr_coord[1]].get_team() != team and (jump_right == 1):
                        result.append(curr_coord)
                        break
                    elif jump_right == 0:
                        # record that jump has taken place in this direction
                        jump_right = 1

                # next coordinate is empty
                else:
                    result.append(curr_coord)
        return result

    def possible_moves(self, src_coord, board):
        """
        Description:
        returns a list of tuples of all possible moves that can be made from current location coordinates
        Parameters:
        src_coord - tuple of source board slot coordinates
        board - current board list that contains piece objects
        Returns:
        list of tuples of all possible moves for this Piece class from the src_coord location validated with is_valid
        method
        """
        y = src_coord[0]
        x = src_coord[1]
        start_list = [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]

        return self._is_valid(start_list, board, src_coord)


class Soldier(Piece):
    """Represents a Soldier Piece"""

    def _is_valid(self, possible_list, board):
        """
        Description:
        Private method that determines if moves are valid for this piece type with the current context of board
        Parameters:
        possible_list: list of tuples of all possible moves for piece type
        board - current board layout with pieces as a list from XiangqiGame method
        Returns:
        valid_list of all valid moves with respect to the board
        """
        team = self.get_team()
        result = []
        for el in possible_list:
            # if the coordinate exists on the board
            if self.is_on_the_board(el) is True:
                # if destination is empty, add coord to result list
                if board[el[0]][el[1]] == 0:
                    result.append(el)
                # if destination has opponent in it, add coord to result list
                elif board[el[0]][el[1]].get_team() != team:
                    result.append(el)
        return result

    def possible_moves(self, src_coord, board):
        """
        Description:
        returns a list of tuples of all possible moves that can be made from current location coordinates
        Parameters:
        src_coord - tuple of source board slot coordinates
        board - current board list that contains piece objects
        Returns:
        list of tuples of all possible moves for this Piece class from the src_coord location validated with is_valid
        method
        """
        y = src_coord[0]
        x = src_coord[1]
        if self.get_team() == 'red':
            # read team soldier movement
            possible_list = [(y + 1, x)]
            # if the solider is past the river, add orthogonal movements
            if y > 4:
                possible_list.append((y, x-1))
                possible_list.append((y, x+1))
        else:
            # black team soldier movement
            possible_list = [(y - 1, x)]
            # if the solider is past the river, add orthogonal movements
            if y < 5:
                possible_list.append((y, x-1))
                possible_list.append((y, x+1))

        return self._is_valid(possible_list, board)

#submitted version does not have any of the below code
#game = XiangqiGame()

# print("initial board")
# game.print_current_board()
# print()
# print()
#
#
#
# game.make_move('e1', 'e2')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('e10', 'e9')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('e2', 'e3')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('e9', 'e8')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('e3', 'f3')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('e8', 'd8')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('f3', 'f3')
# game.print_current_board()
# print(game.get_current_team())
#
# #advisor test
#
# game.make_move('f1', 'e2')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('d10', 'e9')
# game.print_current_board()
# print(game.get_current_team())
#
# # test if general is blocked by advisor
# game.make_move('f3', 'f2')
# game.print_current_board()
# print(game.get_current_team())
#
# #test check scenario with cannon
# game.make_move('b8', 'b2')
# game.print_current_board()
# print(game.get_current_team())
#
# print(game.is_in_check('red'))
#
# #move out of check
# game.make_move('f2', 'f3')
# game.print_current_board()
# print(game.get_current_team())
#
# print(game.is_in_check('red'))
#
# game.make_move('b2', 'f2')
# game.print_current_board()
# print(game.get_current_team())
#
# print(game.is_in_check('red'))
#
# game.make_move('f3', 'f2')
# game.print_current_board()
# print(game.get_current_team())
#
# print(game.is_in_check('red'))
#
# #soldier moves
# game.make_move('i7', 'i6')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('i4', 'i5')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('i6', 'i5')
# game.print_current_board()
# print(game.get_current_team())
#
# #cannon move to set up for horse test
# game.make_move('h3', 'h9')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('i5', 'h5')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('a4', 'a5')
# game.print_current_board()
# print(game.get_current_team())
#
# #rook test
# game.make_move('i10', 'i2')
# game.print_current_board()
# print(game.get_current_team())
#
# print(game.is_in_check('red'))
#
# game.make_move('i1', 'i2')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('a10', 'a9')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('h9', 'h5')
# game.print_current_board()
# print(game.get_current_team())
#
# #horse block test
# game.make_move('h10', 'i8')
# game.print_current_board()
# print(game.get_current_team())
# #
#
# game.make_move('i2', 'g2')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('e9', 'd10')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('e4', 'e5')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('c10', 'a8')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('e2', 'f3')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('a9', 'f9')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('c1', 'a3')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('c7', 'c6')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('a5', 'a6')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('c6', 'c5')
# game.print_current_board()
# print(game.get_current_team())
#
# game.make_move('f3', 'e2')
# game.print_current_board()
# print(game.get_current_team())
#
# print(game.get_game_state())








#
# #cannon test
# print("cannon test")
# print(game.make_move('h8', 'h1'))
#
# game.print_current_board()
# print(game.get_current_team())
#
# #elephant test
# print("elephant test")
# print(game.make_move('g1', 'g2'))
#
# print("elephant test")
# print(game.make_move('g1', 'h3'))
#
# print("elephant test")
# print(game.make_move('g1', 'f3'))
#
# print("elephant test")
# print(game.make_move('g1', 'e3'))
#
# game.print_current_board()
# print(game.get_current_team())
#
# print("elephant test")
# print(game.make_move('c10', 'a8'))
#
# game.print_current_board()
# print(game.get_current_team())
#
# print("elephant test")
# print(game.make_move('e3', 'g5'))
#
# game.print_current_board()
# print(game.get_current_team())
#
# print("elephant test")
# print(game.make_move('a8', 'c6'))
#
# game.print_current_board()
# print(game.get_current_team())
#
# print("elephant test")
# print(game.make_move('g5', 'e7'))
#
# game.print_current_board()
# print(game.get_current_team())
#
# #checkmate test
# print("check test")
# print(game.make_move('b3', 'b6'))
#
# game.print_current_board()
# print(game.get_current_team())
#
# print(game.make_move('a7', 'a6'))
#
# game.print_current_board()
# print(game.get_current_team())
# #print(game.is_in_check('black'))
# #print(game.make_move('b6', 'e6'))
#
# #game.print_current_board()
# #print(game.get_current_team())
# print(game.is_in_check('black'))
# print(game.get_game_state())
#
# #horse test
# print(game.make_move('b1', 'c3'))
#
# game.print_current_board()
# print(game.get_current_team())

# game = XiangqiGame()
# move_result = game.make_move('c1', 'e3')
# game.print_current_board()
# black_in_check = game.is_in_check('black')
# print(black_in_check)
# game.make_move('e7', 'e6')
# game.print_current_board()
# state = game.get_game_state()
# print(state)

